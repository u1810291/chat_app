from django.contrib import messages
from django.shortcuts import render, redirect, Http404

from .forms import RegistrationForm, EditProfileForm
from .models import Chat, Person
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

from rest_framework import viewsets
# from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *


# def index(request):
#     if request.method == 'POST':
#         form = SmileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('success')
#     else:
#         form = SmileForm()
#     return render(request, 'index.html', {'form': form})


@login_required()
def home(request):
    args = {}
    return render(request, 'accounts/home.html', args)


@login_required()
def index(request):
    chats = Chat.objects.all()
    to = Chat.user_first_name_to
    return render(request, 'index.html', {'chats': chats})


# class IndexView(APIView):
#     def get(self, request):
#         chat = Chat.objects.all()
#         serializer = ChatSerializer(chat, many=True)
#         return Response({'chat': serializer.data})
#
#     def post(self, request):
#         chat = request.data.get('chat')
#         serializer = ChatSerializer(data=chat)
#         if serializer.is_valid(raise_exception=True):
#             chat_saved = serializer.save()
#             return Response({"success": "Chat ' {} ' created successfully".format(chat.chat_type)})



def register(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data['username']
        password1 = form.cleaned_data['password1']
        user = authenticate(username=username, password1=password1)
        login(request, user)
        return redirect('/accounts')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required()
def register_redirect(request):
    return redirect('accounts')


@login_required()
def login_redirect(request):
    return redirect('/accounts/login')


@login_required()
def view_profile(request):
    per = Person.objects.all()
    person = {'person': per}
    args = {'user': request.user, 'person': person}
    return render(request, 'accounts/profile.html', args)


@login_required()
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit.html', args)


# python -m smtpd -n -c DebuggingServer localhost:1025
@login_required()
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/accounts/profile')
        else:
            return redirect('/accounts/profile/change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change-password.html', args)




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = User_serializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = Group_serializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = Role_serializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = Person_serializer


class ShipmentTypeViewSet(viewsets.ModelViewSet):
    queryset = Shipment_type.objects.all()
    serializer_class = Shipment_type_serializer


class PaymentTypeViewSet(viewsets.ModelViewSet):
    queryset = Payment_type.objects.all()
    serializer_class = Payment_type_serializer


class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = Shipment_serializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = Product_serializer


class LocationsViewSet(viewsets.ModelViewSet):
    queryset = Locations.objects.all()
    serializer_class = Locations_serializer


class StatusCatalogViewSet(viewsets.ModelViewSet):
    queryset = Status_catalog.objects.all()
    serializer_class = Status_catalog_serializer


class ShipmentStatusViewSet(viewsets.ModelViewSet):
    queryset = Shipment_status.objects.all()
    serializer_class = Shipment_status_serializer


class ShipmentDetailsViewSet(viewsets.ModelViewSet):
    queryset = Shipment_details.objects.all()
    serializer_class = Shipment_details_serializer


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = Stock_serializer


class ProductDetailsViewSet(viewsets.ModelViewSet):
    queryset = Product_details.objects.all()
    serializer_class = Product_details_serializer


class PaymentDataViewSet(viewsets.ModelViewSet):
    queryset = Payment_data.objects.all()
    serializer_class = Payment_data_serializer


class PaymentDetailsViewSet(viewsets.ModelViewSet):
    queryset = Payment_details.objects.all()
    serializer_class = Payment_details_serializer
