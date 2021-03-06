# Generated by Django 4.0.2 on 2022-03-13 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Signal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('side', models.CharField(max_length=5)),
                ('symbol', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bot', models.BooleanField(default=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('order_id', models.CharField(max_length=30)),
                ('signal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.signal')),
            ],
        ),
    ]
