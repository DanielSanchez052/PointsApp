# Generated by Django 4.0.4 on 2022-05-31 02:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, unique=True)),
                ('postal_code', models.CharField(blank=True, max_length=50, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'User City',
                'verbose_name_plural': 'User Cities',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'User Country',
                'verbose_name_plural': 'User Country',
            },
        ),
        migrations.CreateModel(
            name='IdentificationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Identification Type',
                'verbose_name_plural': 'Identification Type',
            },
        ),
        migrations.CreateModel(
            name='ProfileStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Profile status',
                'verbose_name_plural': 'Profile status',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('created_at', models.DateField(auto_now_add=True, verbose_name='created at')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='modified at')),
                ('deleted_at', models.DateField(auto_now=True, verbose_name='deleted at')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('identification', models.CharField(max_length=150, unique=True, verbose_name='identification')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('phone', models.CharField(max_length=50, verbose_name='phone number')),
                ('phone2', models.CharField(blank=True, max_length=50, null=True, verbose_name='phone extra')),
                ('address', models.CharField(blank=True, max_length=250, verbose_name='address')),
                ('postal_code', models.CharField(blank=True, max_length=50)),
                ('auth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.city')),
                ('identification_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='user.identificationtype')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='user.profilestatus')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.country')),
            ],
            options={
                'verbose_name': 'User Department',
                'verbose_name_plural': 'User Departments',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.department'),
        ),
    ]
