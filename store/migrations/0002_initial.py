# Generated by Django 3.2.7 on 2021-10-29 05:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('addressCollection', '0002_address_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='wish_list',
            name='User_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='return_items',
            name='CompletedOrders_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.completedorders'),
        ),
        migrations.AddField(
            model_name='orders',
            name='Address_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addressCollection.address'),
        ),
        migrations.AddField(
            model_name='orders',
            name='Customers_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='orders',
            name='Items_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.items'),
        ),
        migrations.AddField(
            model_name='items',
            name='Belongs_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.belongs'),
        ),
        migrations.AddField(
            model_name='completedorders',
            name='Address_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addressCollection.address'),
        ),
        migrations.AddField(
            model_name='completedorders',
            name='Customers_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='completedorders',
            name='Items_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.items'),
        ),
        migrations.AddField(
            model_name='completed_return_items',
            name='Return_Items_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.return_items'),
        ),
        migrations.AddField(
            model_name='cart',
            name='Items_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.items'),
        ),
        migrations.AddField(
            model_name='cart',
            name='User_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='belongs',
            name='Categorie_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.categorie'),
        ),
    ]
