# Generated by Django 3.1.7 on 2021-02-24 19:14

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('code', models.CharField(blank=True, max_length=8, null=True)),
                ('symbol', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='MainSliderData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='uploads')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PolicyTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terms_of_use', models.TextField(blank=True, null=True)),
                ('privacy_policy', models.TextField(blank=True, null=True)),
                ('refund_policy', models.TextField(blank=True, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('edited_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PublicMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=150)),
                ('sender_email', models.CharField(max_length=150)),
                ('message', models.TextField()),
                ('received_at', models.DateTimeField(auto_now_add=True)),
                ('read', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSubcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productcategory')),
            ],
        ),
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_uuid', models.CharField(db_index=True, default=uuid.uuid4, max_length=100, unique=True)),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('specifications', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('promotion_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('preview_image', models.ImageField(blank=True, null=True, upload_to='uploads')),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='uploads')),
                ('in_stock', models.BooleanField(default=True)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.productcategory')),
                ('subcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.productsubcategory')),
            ],
        ),
        migrations.CreateModel(
            name='GeneralInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.CharField(blank=True, max_length=150, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=150, null=True)),
                ('facebook_link', models.TextField(blank=True, null=True)),
                ('twitter_link', models.TextField(blank=True, null=True)),
                ('linkedin_link', models.TextField(blank=True, null=True)),
                ('instagram_link', models.TextField(blank=True, null=True)),
                ('street_name', models.CharField(blank=True, max_length=150, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=150, null=True)),
                ('city', models.CharField(blank=True, max_length=150, null=True)),
                ('active', models.BooleanField(default=False)),
                ('currency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.currency')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_uuid', models.CharField(db_index=True, default=uuid.uuid4, max_length=100, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
