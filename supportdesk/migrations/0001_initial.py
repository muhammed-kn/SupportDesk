# Generated by Django 4.1.4 on 2022-12-19 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('is_completed', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updated', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
