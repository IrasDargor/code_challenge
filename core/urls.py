from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rental_store.views import (
    ActorViewSet,
    AddressViewSet,
    CategoryViewSet,
    CityViewSet,
    CountryViewSet,
    CustomerViewSet,
    FilmViewSet,
    InventoryViewSet,
    LanguageViewSet,
    PaymentViewSet,
    RentalViewSet,
    StaffViewSet,
    StoreViewSet
)

router = routers.DefaultRouter()
router.register(r'actors', ActorViewSet)
router.register(r'address', AddressViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'cities', CityViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'films', FilmViewSet)
router.register(r'inventories', InventoryViewSet)
router.register(r'languages', LanguageViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'rents', RentalViewSet)
router.register(r'staff', StaffViewSet)
router.register(r'stores', StoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

]
