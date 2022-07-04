from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('actor_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'actor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=50)),
                ('address2', models.CharField(blank=True, max_length=50, null=True)),
                ('district', models.CharField(max_length=20)),
                ('city_id', models.SmallIntegerField()),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('phone', models.CharField(max_length=20)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'address',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=50)),
                ('country_id', models.SmallIntegerField()),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'city',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_id', models.AutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=50)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'country',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('store_id', models.SmallIntegerField()),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('address_id', models.SmallIntegerField()),
                ('activebool', models.BooleanField()),
                ('create_date', models.DateField()),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('active', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('film_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('release_year', models.SmallIntegerField(blank=True, null=True)),
                ('language_id', models.SmallIntegerField()),
                ('rental_duration', models.SmallIntegerField()),
                ('rental_rate', models.DecimalField(decimal_places=2, max_digits=4)),
                ('length', models.SmallIntegerField(blank=True, null=True)),
                ('replacement_cost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rating', models.TextField(blank=True, null=True)),
                ('last_update', models.DateTimeField()),
                ('special_features', models.TextField(blank=True, null=True)),
                ('fulltext', models.TextField()),
            ],
            options={
                'db_table': 'film',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FilmActor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_id', models.SmallIntegerField()),
                ('film_id', models.SmallIntegerField()),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'film_actor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FilmCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_id', models.SmallIntegerField()),
                ('category_id', models.SmallIntegerField()),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'film_category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('inventory_id', models.AutoField(primary_key=True, serialize=False)),
                ('film_id', models.SmallIntegerField()),
                ('store_id', models.SmallIntegerField()),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'inventory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('language_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'language',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_id', models.SmallIntegerField()),
                ('staff_id', models.SmallIntegerField()),
                ('rental_id', models.IntegerField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('payment_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'payment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('rental_id', models.AutoField(primary_key=True, serialize=False)),
                ('rental_date', models.DateTimeField()),
                ('inventory_id', models.IntegerField()),
                ('customer_id', models.SmallIntegerField()),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('staff_id', models.SmallIntegerField()),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'rental',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('address_id', models.SmallIntegerField()),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('store_id', models.SmallIntegerField()),
                ('active', models.BooleanField()),
                ('username', models.CharField(max_length=16)),
                ('password', models.CharField(blank=True, max_length=40, null=True)),
                ('last_update', models.DateTimeField()),
                ('picture', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'staff',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('store_id', models.AutoField(primary_key=True, serialize=False)),
                ('manager_staff_id', models.SmallIntegerField()),
                ('address_id', models.SmallIntegerField()),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'store',
                'managed': False,
            },
        ),
    ]
