from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class Group_serializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']
    def create(self, validated_data):
        return Group.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)

    def delete(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        del instance.name



class User_serializer(serializers.ModelSerializer):
    groups = Group_serializer(many=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']    

    def create(self, validated_data):
        groups_data = validated_data.pop('groups')
        user = User.objects.create(**validated_data)
        for groups_data1 in groups_data:
            Group.objects.create(**groups_data1, user=user)        
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)


# Roles
class Role_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Role
        fields = ['role', 'role_name']

    def create(self, validated_data):
        role = Role.objects.create(**validated_data)
        return role


# Users
class Person_serializer(serializers.ModelSerializer):
    user = User_serializer
    role = Role_serializer
    class Meta:
        model = Person
        fields = ['country', 'city', 'state', 'age', 'sex', 'user_longitude', 'user_latitude', 'user', 'role'] 
    
    def create(self, validated_data):
        person = Person.objects.create(**validated_data)
        return person


class Shipment_type_serializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment_type
        fields = ['id','type_name']


class Payment_type_serializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_type
        fields = ['type_name']


class Product_type_serializer(serializers.ModelSerializer):
    class Meta:
        model = Product_type
        fields = ['type_name'] 


# # Shipments
class Shipment_serializer(serializers.ModelSerializer):
    client_id = User_serializer 
    shipment_type = Shipment_type_serializer
    payment_type = Payment_type_serializer
    product_type = Product_type_serializer
    class Meta:
        model = Shipment
        fields = ['time_created', 'shipping_address', 'billing_address', 'product_type', 'delivery_cost', 'discount', 'final_price', 'shipment_longitude', 'shipment_latitude', 'client_id', 'shipment_type', 'payment_type', 'product_type']



class Product_serializer(serializers.ModelSerializer):
    product_type_id = Product_type_serializer
    class Meta:
        model = Product
        fields = ['product_name', 'product_description', 'unit', 'price_per_unit', 'product_type_id']


class Locations_serializer(serializers.ModelSerializer):
    shipment_id = Shipment_serializer
    user_id = User_serializer
    product_id = Product_serializer
    class Meta:
        model = Locations
        fields = ['driver_id', 'user_long', 'user_lat', 'product_long', 'product_lat', 'driver_long', 'driver_lat', 'shipping_long', 'shipping_lat', 'date_create', 'shipment_id', 'user_id', 'product_id']


class Status_catalog_serializer(serializers.ModelSerializer):
    class Meta:
        model = Status_catalog
        fields = ['status_name']


class Shipment_status_serializer(serializers.ModelSerializer):
    shipment_id = Shipment_serializer
    status_catalog = Status_catalog_serializer
    class Meta:
        model = Shipment_status
        fields = ['status_time', 'notes', 'shipment_id', 'status_catalog']


class Shipment_details_serializer(serializers.ModelSerializer):
    shipment_id = Shipment_serializer
    product_id = Product_serializer
    class Meta:
        model = Shipment_details
        fields = ['quantity', 'price_per_unit', 'price', 'shipment_id', 'product_id']


# # Products
class Stock_serializer(serializers.ModelSerializer):
    product_id = Product_serializer
    class Meta:
        model = Stock
        fields = ['in_stock', 'last_update', 'product_id']


class Product_details_serializer(serializers.ModelSerializer):
    class Meta:
        model = Product_details
        fields = ['product_name', 'product_description', 'type_name', 'unit', 'price_per_unit', 'in_stock', 'product_longitude', 'product_latitude', 'last_update']


# # Payments
class Payment_data_serializer(serializers.ModelSerializer):
    payment_type = Payment_type_serializer
    class Meta:
        model = Payment_data
        fields = ['data_name', 'data_type', 'date_payed', 'payment_type']


class Payment_details_serializer(serializers.ModelSerializer):
    shipment_id = Shipment_serializer
    payment_data = Payment_data_serializer
    class Meta:
        model = Payment_details
        fields = ['shipment_id','payment_data','value']
