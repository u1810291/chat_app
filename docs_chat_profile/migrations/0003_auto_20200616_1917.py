# Generated by Django 3.0.7 on 2020-06-16 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docs_chat_profile', '0002_auto_20200606_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docs_chat_profile.Product_type'),
        ),
    ]