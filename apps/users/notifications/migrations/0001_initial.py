# Generated by Django 4.0.4 on 2022-05-21 03:20

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
            name='NotificationStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Notification status',
                'verbose_name_plural': 'Notification status',
            },
        ),
        migrations.CreateModel(
            name='NotificationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, unique=True)),
                ('config', models.TextField(max_length=500, verbose_name='config')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Notification Type',
                'verbose_name_plural': 'Notification Type',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('created_at', models.DateField(auto_now_add=True, verbose_name='created at')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='modified at')),
                ('deleted_at', models.DateField(auto_now=True, verbose_name='deleted at')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=150, unique=True)),
                ('description', models.TextField(blank=True, max_length=255)),
                ('config', models.TextField(max_length=500, verbose_name='config')),
                ('notification_status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='notifications.notificationstatus')),
                ('notification_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notifications.notificationtype')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile')),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notification',
            },
        ),
    ]
