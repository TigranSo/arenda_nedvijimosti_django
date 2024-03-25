from modeltranslation.translator import register, TranslationOptions
from arenda.models import Owner, Arenda, Sale, Yacht, News, Reservation, Applications, Region


@register(Owner)
class OwnerTranslationOptions(TranslationOptions):
    fields = ('name_obj', 'description_2')


@register(Region)
class RegionTranslationOptions(TranslationOptions):
    fields = ('name', 'country')



@register(Arenda)
class ArendaTranslationOptions(TranslationOptions):
    fields = ('Owner_object', 'name', 'description', 'country', 'region', 'city', 'property_type', 
              'property_type_2', 'Location', 'private_1', 'private_2', 'private_3', 'private_4', 'private_5', 
              'private_6', 'private_7', 'private_8', 'private_9', 'private_10', 
              'description_1')


@register(Sale)
class SaleTranslationOptions(TranslationOptions):
    fields = ('Owner_object', 'name', 'description', 'city', 'Location', 'description_1')


@register(Yacht)
class YachtTranslationOptions(TranslationOptions):
    fields = ('Owner_object', 'name', 'description', 'engine', 'Location', 'description_1')


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'description_1')


@register(Reservation)
class ReservationTranslationOptions(TranslationOptions):
    fields = ('arenda', 'arrival', 'departure', 'full_name', 'preferences')


@register(Applications)
class ApplicationsTranslationOptions(TranslationOptions):
    fields = ('name')

