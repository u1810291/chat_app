from django.db import models
from django.contrib.auth.models import User


# Roles
class Role(models.Model):
    role = models.IntegerField()
    role_name = models.CharField(max_length=50)


# Users
class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.OneToOneField(Role, on_delete=models.CASCADE, default=10)
    country = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    age = models.CharField(max_length=50, null=True)
    sex = models.CharField(max_length=50, null=True)
    user_longitude = models.DecimalField(decimal_places=9, max_digits=20)
    user_latitude = models.DecimalField(decimal_places=9, max_digits=20)


class Shipment_type(models.Model):
    type_name = models.CharField(max_length=255)


class Payment_type(models.Model):
    type_name = models.CharField(max_length=250)


class Product_type(models.Model):
    type_name = models.CharField(max_length=200)


# Shipments
class Shipment(models.Model):
    client_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_type = models.ForeignKey(Product_type, on_delete=models.CASCADE)
    shipment_type = models.ForeignKey(Shipment_type, on_delete=models.CASCADE)
    payment_type = models.ForeignKey(Payment_type, on_delete=models.CASCADE)
    time_created = models.DateTimeField()
    shipping_address = models.CharField(max_length=250)
    billing_address = models.CharField(max_length=250)
    delivery_cost = models.DecimalField(decimal_places=9, max_digits=20)
    discount = models.DecimalField(decimal_places=9, max_digits=20)
    final_price = models.DecimalField(decimal_places=9, max_digits=20)
    shipment_longitude = models.DecimalField(decimal_places=9, max_digits=20)
    shipment_latitude = models.DecimalField(decimal_places=9, max_digits=20)




class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_description = models.CharField(max_length=255)
    product_type_id = models.ForeignKey(Product_type, on_delete=models.CASCADE)
    unit = models.CharField(max_length=50)
    price_per_unit = models.DecimalField(decimal_places=9, max_digits=20)


class Locations(models.Model):
    shipment_id = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    driver_id = models.IntegerField()
    user_long = models.DecimalField(decimal_places=9, max_digits=20)
    user_lat = models.DecimalField(decimal_places=9, max_digits=20)
    product_long = models.DecimalField(decimal_places=9, max_digits=20)
    product_lat = models.DecimalField(decimal_places=9, max_digits=20)
    driver_long = models.DecimalField(decimal_places=9, max_digits=20)
    driver_lat = models.DecimalField(decimal_places=9, max_digits=20)
    shipping_long = models.DecimalField(decimal_places=9, max_digits=20)
    shipping_lat = models.DecimalField(decimal_places=9, max_digits=20)
    date_create = models.DateTimeField()


class Status_catalog(models.Model):
    status_name = models.CharField(max_length=255)


class Shipment_status(models.Model):
    shipment_id = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    status_catalog = models.ForeignKey(Status_catalog, on_delete=models.CASCADE)
    status_time = models.DateTimeField()
    notes = models.TextField()


class Shipment_details(models.Model):
    shipment_id = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(decimal_places=9, max_digits=20)
    price_per_unit = models.DecimalField(decimal_places=9, max_digits=20)
    price = models.DecimalField(decimal_places=9, max_digits=20)


# Products
class Stock(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, primary_key=True)
    in_stock = models.DecimalField(decimal_places=9, max_digits=20)
    last_update = models.DateTimeField()


class Product_details(models.Model):
    product_name = models.CharField(max_length=200)
    product_description = models.CharField(max_length=200)
    type_name = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    price_per_unit = models.DecimalField(decimal_places=9, max_digits=20)
    in_stock = models.DecimalField(decimal_places=9, max_digits=20)
    product_longitude = models.DecimalField(decimal_places=9, max_digits=20)
    product_latitude = models.DecimalField(decimal_places=9, max_digits=20)
    last_update = models.DateTimeField()


# Payments
class Payment_data(models.Model):
    payment_type = models.ForeignKey(Payment_type, on_delete=models.CASCADE)
    data_name = models.CharField(max_length=255)
    data_type = models.CharField(max_length=255)
    date_payed = models.DateTimeField()


class Payment_details(models.Model):
    shipment_id = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    payment_data = models.ForeignKey(Payment_data, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)


class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    chat_description = models.CharField(max_length=200)
    chat_type = models.CharField(max_length=200)
    chat_text = models.TextField()
    date_message = models.DateTimeField()
    user_first_name_from = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    user_first_name_to = models.IntegerField(default='')


class Groups(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_description = models.CharField(max_length=200)
    group_type = models.CharField(max_length=200)
    group_text = models.TextField()
    group_date_message = models.DateTimeField('date send')


class Smiles(models.Model):
    smile_id = models.AutoField(primary_key=True)
    smile_img = models.ImageField(upload_to='images/')
    smile_date_message = models.DateTimeField('date send')
