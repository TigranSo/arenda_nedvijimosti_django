from django.contrib import admin
from arenda.models import Owner, Arenda, Sale, Yacht, News, Reservation, Applications, Region, Country, City, Imgmain
from modeltranslation.admin import TranslationAdmin


admin.site.register(Owner)
admin.site.register(Arenda)
admin.site.register(Sale)
admin.site.register(Yacht)
admin.site.register(News)
admin.site.register(Reservation)
admin.site.register(Applications)
admin.site.register(Region)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Imgmain)




# @admin.register(Owner)
# class OwnerAdmin(TranslationAdmin):
#     list_display  = ('name_obj', 'description_2')


# @admin.register(Arenda)
# class ArendaAdmin(TranslationAdmin):
#     list_display  = ('Owner_object', 'name', 'description', 'country', 'region', 'city', 'property_type', 
#             'property_type_2', 'Location', 'private_1', 'private_2', 'private_3', 'private_4', 'private_5', 
#             'private_6', 'private_7', 'private_8', 'private_9', 'private_10', 
#             'description_1')


# @admin.register(Sale)
# class SaleAdmin(TranslationAdmin):
#     list_display  = ('Owner_object', 'name', 'description', 'city', 'Location', 'description_1')


# @admin.register(Yacht)
# class YachtAdmin(TranslationAdmin):
#     list_display  = ('Owner_object', 'name', 'description', 'engine', 'Location', 'description_1')


# @admin.register(News)
# class NewsAdmin(TranslationAdmin):
#     list_display  = ('name', 'description', 'description_1')


# @admin.register(Reservation)
# class ReservationAdmin(TranslationAdmin):
#     list_display  = ('arenda', 'arrival', 'departure', 'full_name', 'preferences')


# @admin.register(Applications)
# class ApplicationsAdmin(TranslationAdmin):
#     list_display  = ('name')


# @admin.register(Country)
# class CountryAdmin(TranslationAdmin):
#     list_display  = ('name')


# @admin.register(Region)
# class RegionAdmin(TranslationAdmin):
#     list_display  = ('name', 'country')


# @admin.register(City)
# class CitynAdmin(TranslationAdmin):
#     list_display  = ('name', 'region')
