from django.urls import path
from api import views


domain_list = views.DomainViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
domain_detail = views.DomainViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
scan_list = views.ScanViewSet.as_view({
    'get': 'list',
})
subscription_detail = views.SubscriptionViewSet.as_view({
    'get': 'retrieve',
})
user_detail = views.UserViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = [
    path('auth/password/change/', views.ChangePasswordView.as_view(), name='change_password'), 
    path('auth/password/request/', views.RequestPasswordResetView.as_view(), name='request_password_reset'), 
    path('auth/password/reset/', views.ResetPasswordView.as_view(), name='password_reset'), 
    path('auth/register/', views.RegisterViewSet.as_view(), name='auth_register'),
    path('auth/email/verify/<str:verify_key>/', views.VerifyEmailView.as_view(), name='verify_email'),
    path('domains/', domain_list, name='domain_list'), 
    path('domains/<int:pk>/', domain_detail, name='domain_detail'), 
    path('domains/<int:pk>/scans/', scan_list, name='scan_list'), 
    path('payment/', views.create_payment_intent, name='create_payment_intent'), 
    path('users/<int:pk>/', user_detail, name='user_detail'),
    path('users/<int:pk>/subscription/', subscription_detail, name='subscription_detail'),
    path('webhook/', views.stripe_webhook, name='webhook'), 
]
