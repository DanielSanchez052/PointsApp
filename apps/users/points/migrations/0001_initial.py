# Generated by Django 4.0.4 on 2022-05-21 03:21

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='created at')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='modified at')),
                ('deleted_at', models.DateField(auto_now=True, verbose_name='deleted at')),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
            },
        ),
        migrations.CreateModel(
            name='AccountStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, unique=True)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
            ],
            options={
                'verbose_name': 'Account status',
                'verbose_name_plural': 'Account status',
            },
        ),
        migrations.CreateModel(
            name='TransactionStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, unique=True)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
            ],
            options={
                'verbose_name': 'Transaction status',
                'verbose_name_plural': 'Transaction status',
            },
        ),
        migrations.CreateModel(
            name='AccountTransaction',
            fields=[
                ('created_at', models.DateField(auto_now_add=True, verbose_name='created at')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='modified at')),
                ('deleted_at', models.DateField(auto_now=True, verbose_name='deleted at')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('value', models.PositiveIntegerField(blank=True, null=True)),
                ('available_value', models.PositiveIntegerField(blank=True, null=True)),
                ('ExpirationDate', models.DateField(blank=True, default=datetime.datetime(2023, 5, 21, 3, 21, 6, 487176), null=True, verbose_name='Expire at')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='points.account')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='points.transactionstatus')),
            ],
            options={
                'verbose_name': 'Account Transaction',
                'verbose_name_plural': 'Account Transaction',
            },
        ),
        migrations.AddField(
            model_name='account',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='points.accountstatus'),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile'),
        ),
    ]
