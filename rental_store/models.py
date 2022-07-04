from django.db import models
from datetime import datetime


class Actor(models.Model):
    actor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField(default=datetime.now())

    class Meta:
        managed = False
        db_table = 'actor'

    def save(self, *args, **kwargs):
        if not Actor.objects.count():
            self.actor_id = 200
        elif Actor.objects.get(pk=self.actor_id):
            self.first_name = self.first_name
            self.last_name = self.last_name
            self.last_update = self.last_update
        else:
            self.actor_id = Actor.objects.last().actor_id + 1
        super(Actor, self).save(*args, **kwargs)


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=20)
    city_id = models.SmallIntegerField()
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=20)
    last_update = models.DateTimeField(default=datetime.now())

    class Meta:
        managed = False
        db_table = 'address'

    def save(self, *args, **kwargs):
        if not Address.objects.count():
            self.address_id = 605
        elif Address.objects.get(pk=self.address_id):
            self.address = self.address
            self.address2 = self.address2
            self.district = self.district
            self.city_id = self.city_id
            self.postal_code = self.postal_code
            self.phone = self.phone
            self.last_update = self.last_update
        else:
            self.address_id = Address.objects.last().address_id + 1
        super(Address, self).save(*args, **kwargs)


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    last_update = models.DateTimeField(default=datetime.now())

    class Meta:
        managed = False
        db_table = 'category'

    def save(self, *args, **kwargs):
        if not Category.objects.count():
            self.category_id = 16
        elif Category.objects.get(pk=self.category_id):
            self.name = self.name
            self.last_update = self.last_update
        else:
            self.category_id = Category.objects.last().category_id + 1
        super(Category, self).save(*args, **kwargs)


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50)
    country_id = models.SmallIntegerField()
    last_update = models.DateTimeField(default=datetime.now())

    class Meta:
        managed = False
        db_table = 'city'

    def save(self, *args, **kwargs):
        if not City.objects.count():
            self.city_id = 600
        elif City.objects.get(pk=self.city_id):
            self.city = self.city
            self.country_id = self.country_id
            self.last_update = self.last_update
        else:
            self.city_id = City.objects.last().city_id + 1
        super(City, self).save(*args, **kwargs)


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50)
    last_update = models.DateTimeField(default=datetime.now())

    class Meta:
        managed = False
        db_table = 'country'

    def save(self, *args, **kwargs):
        if not Country.objects.count():
            self.country_id = 109
        elif Country.objects.get(pk=self.country_id):
            self.country = self.country
            self.last_update = self.last_update
        else:
            self.country_id = Country.objects.last().country_id + 1
        super(Country, self).save(*args, **kwargs)


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    store_id = models.SmallIntegerField()
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=50, blank=True, null=True)
    address_id = models.SmallIntegerField()
    activebool = models.BooleanField()
    create_date = models.DateField(default=datetime.now())
    last_update = models.DateTimeField(blank=True, null=True, default=datetime.now())
    active = models.IntegerField(blank=True, null=True, default=1)

    class Meta:
        managed = False
        db_table = 'customer'

    def save(self, *args, **kwargs):
        if not Customer.objects.count():
            self.customer_id = 599
        elif Customer.objects.get(pk=self.customer_id):
            self.store_id = self.store_id
            self.first_name = self.first_name
            self.last_name = self.last_name
            self.email = self.email
            self.address_id = self.address_id
            self.activebool = self.activebool
            self.create_date = self.create_date
            self.active = self.active
            self.last_update = self.last_update
        else:
            self.customer_id = Customer.objects.last().customer_id + 1
        super(Customer, self).Customer(*args, **kwargs)


class Film(models.Model):
    film_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    release_year = models.SmallIntegerField(blank=True, null=True)
    language_id = models.SmallIntegerField()
    rental_duration = models.SmallIntegerField()
    rental_rate = models.DecimalField(max_digits=4, decimal_places=2)
    length = models.SmallIntegerField(blank=True, null=True)
    replacement_cost = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.TextField(blank=True, null=True)  # This field type is a guess.
    last_update = models.DateTimeField(default=datetime.now())
    special_features = models.TextField(blank=True, null=True)  # This field type is a guess.
    fulltext = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'film'

    def save(self, *args, **kwargs):
        if not Film.objects.count():
            self.film_id = 1000
        elif Film.objects.get(pk=self.film_id):
            self.title = self.title
            self.description = self.description
            self.release_year = self.release_year
            self.language_id = self.language_id
            self.rental_duration = self.rental_duration
            self.rental_rate = self.rental_rate
            self.length = self.length
            self.replacement_cost = self.replacement_cost
            self.rating = self.rating
            self.special_features = self.special_features
            self.fulltext = self.fulltext
            self.last_update = self.last_update
        else:
            self.film_id = Film.objects.last().film_id + 1
        super(Film, self).save(*args, **kwargs)


class FilmActor(models.Model):
    actor_id = models.SmallIntegerField()
    film_id = models.SmallIntegerField()
    last_update = models.DateTimeField(default=datetime.now())

    class Meta:
        managed = False
        db_table = 'film_actor'


class FilmCategory(models.Model):
    film_id = models.SmallIntegerField()
    category_id = models.SmallIntegerField()
    last_update = models.DateTimeField(default=datetime.now())

    class Meta:
        managed = False
        db_table = 'film_category'


class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    film_id = models.SmallIntegerField()
    store_id = models.SmallIntegerField()
    last_update = models.DateTimeField(default=datetime.now())

    class Meta:
        managed = False
        db_table = 'inventory'

    def save(self, *args, **kwargs):
        if not Inventory.objects.count():
            self.inventory_id = 4581
        elif Inventory.objects.get(pk=self.inventory_id):
            self.first_name = self.first_name
            self.last_name = self.last_name
            self.last_update = self.last_update
        else:
            self.inventory_id = Inventory.objects.last().inventory_id + 1
        super(Inventory, self).save(*args, **kwargs)


class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_update = models.DateTimeField(default=datetime.now())

    class Meta:
        managed = False
        db_table = 'language'

    def save(self, *args, **kwargs):
        if not Language.objects.count():
            self.language_id = 6
        elif Language.objects.get(pk=self.language_id):
            self.name = self.name
            self.last_update = self.last_update
        else:
            self.language_id = Language.objects.last().language_id + 1
        super(Language, self).save(*args, **kwargs)


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    customer_id = models.SmallIntegerField()
    staff_id = models.SmallIntegerField()
    rental_id = models.IntegerField()
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    payment_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'payment'

    def save(self, *args, **kwargs):
        if not Payment.objects.count():
            self.payment_id = 32098
        elif Payment.objects.get(pk=self.payment_id):
            self.customer_id = self.customer_id
            self.staff_id = self.staff_id
            self.rental_id = self.rental_id
            self.amount = self.amount
            self.payment_date = self.payment_date
        else:
            self.payment_id = Payment.objects.last().payment_id + 1
        super(Payment, self).save(*args, **kwargs)


class Rental(models.Model):
    rental_id = models.AutoField(primary_key=True)
    rental_date = models.DateTimeField()
    inventory_id = models.IntegerField()
    customer_id = models.SmallIntegerField()
    return_date = models.DateTimeField(blank=True, null=True)
    staff_id = models.SmallIntegerField()
    last_update = models.DateTimeField(default=datetime.now())

    class Meta:
        managed = False
        db_table = 'rental'

    def save(self, *args, **kwargs):
        if not Rental.objects.count():
            self.rental_id = 16049
        elif Rental.objects.get(pk=self.rental_id):
            self.rental_date = self.rental_date
            self.inventory_id = self.inventory_id
            self.customer_id = self.customer_id
            self.return_date = self.return_date
            self.staff_id = self.staff_id
            self.last_update = self.last_update
        else:
            self.rental_id = Rental.objects.last().rental_id + 1
        super(Rental, self).save(*args, **kwargs)


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    address_id = models.SmallIntegerField()
    email = models.CharField(max_length=50, blank=True, null=True)
    store_id = models.SmallIntegerField()
    active = models.BooleanField()
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=40, blank=True, null=True)
    last_update = models.DateTimeField(default=datetime.now())
    picture = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff'

    def save(self, *args, **kwargs):
        if not Staff.objects.count():
            self.staff_id = 2
        elif Staff.objects.get(pk=self.staff_id):
            self.first_name = self.first_name
            self.address_id = self.address_id
            self.email = self.email
            self.store_id = self.store_id
            self.active = self.active
            self.username = self.username
            self.password = self.password
            self.picture = self.picture
            self.last_update = self.last_update
        else:
            self.staff_id = Staff.objects.last().staff_id + 1
        super(Staff, self).save(*args, **kwargs)


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    manager_staff_id = models.SmallIntegerField()
    address_id = models.SmallIntegerField()
    last_update = models.DateTimeField(default=datetime.now())

    class Meta:
        managed = False
        db_table = 'store'

    def save(self, *args, **kwargs):
        if not Store.objects.count():
            self.store_id = 2
        elif Store.objects.get(pk=self.store_id):
            self.manager_staff_id = self.manager_staff_id
            self.address_id = self.address_id
            self.last_update = self.last_update
        else:
            self.store_id = Store.objects.last().store_id + 1
        super(Store, self).save(*args, **kwargs)
