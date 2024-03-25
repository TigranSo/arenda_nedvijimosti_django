from django.shortcuts import render, redirect
from arenda.models import Owner, Arenda, Sale, Yacht, News, Reservation, Applications, Country, City, Region, Imgmain
from django.http import HttpResponse, HttpResponseRedirect 
from django.views.generic import ListView, DetailView
from .forms import ReservationForm, ApplicationsForm, SearchForm
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language, activate, gettext
from django.core.mail import send_mail


class HomeListView(ListView):
    model = Arenda
    template_name = 'arenda/index.html'
    ordering = ["-date_created"]
    paginate_by = 3
    context_object_name = 'arenda'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ApplicationsForm() 
        context['form2'] = SearchForm() 
        filtered_arends = Arenda.objects.filter(price_min__gte=15000)[:3]
        context['filtered_arends'] = filtered_arends  
        
        country = Country.objects.all()
        context['country'] = country  
        
        city = City.objects.all()
        context['city'] = city  
        
        region = Region.objects.all()
        context['region'] = region  
        
        img = Imgmain.objects.all()
        context['img'] = img  
        

        return context


def search_view(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            region = form.cleaned_data.get('region')
            property_type_2 = form.cleaned_data.get('property_type_2')
            property_type = form.cleaned_data.get('property_type')
            rooms = form.cleaned_data.get('rooms')
            price_min = form.cleaned_data.get('price_min')
            price_max = form.cleaned_data.get('price_max')

            queryset_arenda = Arenda.objects.all()
            queryset_sale = Sale.objects.all()
            queryset_yacht = Yacht.objects.all()

            if region:
                queryset_arenda = queryset_arenda.filter(region=region)
                queryset_sale = queryset_sale.filter(region=region)
                queryset_yacht = queryset_yacht.filter(region=region)

            if property_type_2:
                queryset_arenda = queryset_arenda.filter(property_type_2=property_type_2)
                queryset_sale = queryset_sale.filter(property_type_2=property_type_2)
                queryset_yacht = queryset_yacht.filter(property_type_2=property_type_2)

            if property_type:
                queryset_arenda = queryset_arenda.filter(property_type=property_type)
                queryset_sale = queryset_sale.filter(property_type=property_type)
                queryset_yacht = queryset_yacht.filter(property_type=property_type)

            if rooms:
                queryset_arenda = queryset_arenda.filter(rooms=rooms)
                queryset_sale = queryset_sale.filter(rooms=rooms)
                queryset_yacht = queryset_yacht.filter(shower_k=rooms) 

            if price_min:
                queryset_arenda = queryset_arenda.filter(price_min__gte=price_min)
                queryset_sale = queryset_sale.filter(price_min__gte=price_min)
                queryset_yacht = queryset_yacht.filter(price_min__gte=price_min)

            # if price_max:
            #     queryset_arenda = queryset_arenda.filter(price__lte=price_max)
            #     queryset_sale = queryset_sale.filter(price__lte=price_max)
            #     queryset_yacht = queryset_yacht.filter(price__lte=price_max)

            context = {
                'form': form,
                'results_arenda': queryset_arenda,
                'results_sale': queryset_sale,
                'results_yacht': queryset_yacht,
            }
            return render(request, 'arenda/search_results.html', context)

    else:
        form = SearchForm()

    context = {
        'form': form,
    }
    return render(request, 'arenda/index.html', context)


class ArendaPageListView(ListView):
    model = Arenda
    template_name = 'arenda/arenda_page.html'
    ordering = ["-date_created"]
    context_object_name = 'arenda'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ApplicationsForm() 
        context['form2'] = SearchForm() 

        return context


class ArendaPageDetailView(DetailView):
    model = Arenda
    template_name = 'arenda/arenda_page_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReservationForm() 
        context['form1'] = ApplicationsForm() 
        context['form2'] = SearchForm() 
        current_arend  = self.get_object()
        region = current_arend.region
        related_arends = Arenda.objects.filter(region=region).exclude(pk=self.object.pk)[:3]
        context['related_arends'] = related_arends  
        return context


def handle_reservation(request, pk):
    arenda = get_object_or_404(Arenda, pk=pk)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.arenda = arenda
            reservation.save()

            messages.success(request, 'Вы забронировали данный объект, скоро свяжемся с Вами, спасибо!')
            return redirect('arenda_page_detail', pk=arenda.pk)
    return redirect('arenda_page_detail', pk=arenda.pk)


def post_applications(request):
    form = ApplicationsForm()
    if request.method == 'POST':
        form = ApplicationsForm(request.POST)
        if form.is_valid():
            post_app = form.save(commit=False)
            post_app.save()
            messages.success(request, 'Вы оставили заявку, скоро свяжемся с Вами, спаибо!')
            
            return redirect('index')
    return redirect('about')


class NewsListView(ListView):
    model = News
    template_name = 'arenda/news.html'
    ordering = ["-date_created"]
    paginate_by = 6
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ApplicationsForm() 

        return context


class NewsDetailView(DetailView):
    model = News
    template_name = 'arenda/news_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ApplicationsForm() 

        return context
    

class SaleListView(ListView):
    model = Sale
    template_name = 'arenda/sale.html'
    ordering = ["-date_created"]
    paginate_by = 6
    context_object_name = 'sale'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ApplicationsForm() 
        context['form2'] = SearchForm() 

        return context


class SaleDetailView(DetailView):
    model = Sale
    template_name = 'arenda/sale_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ApplicationsForm() 
        context['form2'] = SearchForm() 

        return context


class YachtListView(ListView):
    model = Yacht
    template_name = 'arenda/yacht.html'
    ordering = ["-date_created"]
    paginate_by = 6
    context_object_name = 'yacht'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ApplicationsForm() 
        context['form2'] = SearchForm() 

        return context


class YachDetailView(DetailView):
    model = Yacht
    template_name = 'arenda/yacht_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ApplicationsForm() 
        context['form2'] = SearchForm() 

        return context


def contact_page(request):
    form = ApplicationsForm()
    return render(request, 'arenda/contact_page.html', {'form': form})


def about(request):
    form = ApplicationsForm()
    return render(request, 'arenda/about.html', {'form': form})





