from django.urls import path
from . import views 

urlpatterns = [
    path('', views.HomeListView.as_view(), name='index'),
    path('arenda_page', views.ArendaPageListView.as_view(), name='arenda_page'),
    path('arenda/<int:pk>/', views.ArendaPageDetailView.as_view(), name='arenda_page_detail'),
    path('arenda/<int:pk>/reserve/', views.handle_reservation, name='handle_reservation'),
    path('contact_page', views.contact_page, name='contact_page'),
    path('post_applications', views.post_applications, name='post_applications'),

    path('about', views.about, name='about'),
    path('search_results', views.search_view, name='search_results'),

    path('news', views.NewsListView.as_view(), name='news'),
    path('news_detail/<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),

    path('sale', views.SaleListView.as_view(), name='sale'),
    path('sale_detail/<int:pk>/', views.SaleDetailView.as_view(), name='sale_detail'),

    path('yacht', views.YachtListView.as_view(), name='yacht'),
    path('yacht_detail/<int:pk>/', views.YachDetailView.as_view(), name='yacht_detail'),
    
]