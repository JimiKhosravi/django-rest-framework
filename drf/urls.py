from django.contrib import admin
from django.urls import path
from api.views import user_profile, update_and_delete_user_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', user_profile, name='user-profile'),
    path('user/<id>/', update_and_delete_user_profile, name='update-user-profile'),
]
