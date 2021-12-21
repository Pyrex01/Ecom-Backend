# Generated by Django 3.2.9 on 2021-12-21 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address_types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address_type', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Phone_number', models.CharField(max_length=13)),
                ('Pincode', models.IntegerField()),
                ('Regein', models.TextField()),
                ('Landmark', models.TextField()),
                ('Town', models.TextField()),
                ('State', models.CharField(choices=[('AP', 'Andhra Pradesh'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar'), ('CT', 'Chhattisgarh'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('HR', 'Haryana'), ('HP', 'Himachal Pradesh'), ('JH', 'Jharkhand'), ('KA', 'Karnataka'), ('KL', 'Kerala'), ('MP', 'Madhya Pradesh'), ('MH', 'Maharashtra'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OR', 'Orissa, Odisha'), ('PB', 'Punjab, Punjab (India)'), ('RJ', 'Rajasthan'), ('SK', 'Sikkim'), ('TN', 'Tamil Nadu, Tamizh Nadu'), ('TG', 'Telangana'), ('TR', 'Tripura'), ('UL', 'Uttarakhand'), ('UP', 'Uttar Pradesh'), ('WB', 'West Bengal'), ('AN', 'Andaman and Nicobar Islands'), ('CH', 'Chandigarh'), ('DN', 'Dadra and Nagar Haveli, Dadra & Nagar Haveli'), ('DD', 'Daman and Diu'), ('DL', 'Delhi, National Capital Territory of Delhi'), ('JK', 'Jammu and Kashmir'), ('LA', 'Ladakh'), ('LD', 'Lakshadweep'), ('PY', 'Pondicherry, Puducherry')], max_length=2)),
                ('Address_type_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addressCollection.address_types')),
            ],
        ),
    ]
