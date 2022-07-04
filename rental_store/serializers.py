from rest_framework import serializers
from .models import (
    Actor,
    Address,
    Category,
    City,
    Country,
    Customer,
    Film,
    FilmActor,
    FilmCategory,
    Inventory,
    Language,
    Payment,
    Rental,
    Staff,
    Store
)


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = (
            'actor_id',
            'first_name',
            'last_name',
            'last_update'
        )


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'address_id',
            'address',
            'address2',
            'district',
            'city_id',
            'postal_code',
            'phone',
            'last_update'
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'category_id',
            'name',
            'last_update'
        )


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = (
            'city_id',
            'city',
            'country_id',
            'last_update'
        )


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = (
            'country_id',
            'country',
            'last_update'
        )


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'customer_id',
            'store_id',
            'first_name',
            'last_name',
            'email',
            'address_id',
            'activebool',
            'active',
            'create_date',
            'last_update'
        )


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = (
            'film_id',
            'title',
            'description',
            'release_year',
            'language_id',
            'rental_duration',
            'rental_rate',
            'length',
            'replacement_cost',
            'special_features',
            'fulltext',
            'last_update'
        )


class FilmActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmActor
        fields = (
            'actor_id',
            'film_id',
            'last_update'
        )


class FilmCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmCategory
        fields = (
            'film_id',
            'category_id',
            'last_update'
        )


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = (
            'inventory_id',
            'film_id',
            'store_id',
            'last_update'
        )


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = (
            'language_id',
            'name',
            'last_update'
        )


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'payment_id',
            'customer_id',
            'staff_id',
            'rental_id',
            'amount',
            'payment_date'
        )


class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = (
            'rental_id',
            'rental_date',
            'inventory_id',
            'customer_id',
            'return_date',
            'staff_id',
            'last_update'
        )


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = (
            'staff_id',
            'first_name',
            'last_name',
            'address_id',
            'email',
            'store_id',
            'active',
            'username',
            'password',
            'picture',
            'last_update'
        )


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = (
            'store_id',
            'manager_staff_id',
            'address_id',
            'last_update'
        )
