# Generated by Django 4.2 on 2023-04-20 13:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('redirect', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FullLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ShortLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short', models.CharField(max_length=20)),
                ('full_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redirect.fulllink')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]