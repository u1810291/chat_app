from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
# from .views import IndexView
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'roles', views.RoleViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'person', views.PersonViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'shipment', views.ShipmentViewSet)
router.register(r'locations', views.LocationsViewSet)
router.register(r'payment-type', views.PaymentTypeViewSet)
router.register(r'payment-data', views.PaymentDataViewSet)
router.register(r'shipment-type', views.ShipmentTypeViewSet)
router.register(r'status-catalog', views.StatusCatalogViewSet)
router.register(r'shipment-status', views.ShipmentStatusViewSet)
router.register(r'payment-details', views.PaymentDetailsViewSet)
router.register(r'shipment-details', views.ShipmentDetailsViewSet)



urlpatterns = [
    path('', views.index),
    # path('', IndexView.as_view()),
    path('home/', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.view_profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit'),
    path('profile/change_password/', views.change_password, name='change_password'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # path('success/<int:chat_id>/detail', views.detail, name='detail'),

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
