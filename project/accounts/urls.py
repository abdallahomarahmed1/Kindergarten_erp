from django.urls import path
from .views import sinup,profile
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name='accounts'
urlpatterns = [
    path('sinup/', sinup, name="sinup"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path("profile/", profile, name="profile"),
    path('change_password/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('accounts:password_change_done'),template_name='accounts/change_password.html'), name='change_password'),
    path('change_password/done', auth_views.PasswordChangeDoneView.as_view(template_name="accounts/change_password_done.html"), name="password_change_done"),
]