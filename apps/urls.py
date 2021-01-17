# python
# django
from django.urls import path, include
# project

from django.contrib.auth import views as auth_views

urlpatterns = [
     #auth
    path('alimentos/', include('apps.alimentos.urls')),
    path('receitas/', include('apps.receitas.urls')),
    path('login/', auth_views.LoginView.as_view(),{'template_name': 'registration/Login.html', 'redirect_authenticard_user': True}, name='login'),
    path('logout/', auth_views.logout_then_login, name='logout'),
    #troca senha
    path('trocarsenha/', auth_views.PasswordChangeView.as_view(template_name= 'auth/password_change.html'), name='password_change'),
    path('trocarsenha/sucesso/', auth_views.PasswordChangeDoneView.as_view(template_name= 'auth/password_change_done.html'), name='password_change_done'),
    #Reset senha
    path('esqueciminhasenha/', auth_views.PasswordResetView.as_view(template_name= 'auth/password_reset.html'), name='password_reset'),
    path('esqueciminhasenha/emailenviado/', auth_views.PasswordResetDoneView.as_view(template_name= 'auth/password_reset_done.html'), name='password_reset_done'),
    path('esqueciminhasenha/novasenha/(<uidb64>[0-9A-Za-z_\-]+)/(<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', auth_views.PasswordResetConfirmView.as_view(template_name= 'auth/password_reset_confirm.html'), name='password_reset_confirm'),
    path('esqueciminhasenha/feito/', auth_views.PasswordResetCompleteView.as_view(template_name= 'auth/password_reset_complete.html'), name='password_reset_complete'),

]