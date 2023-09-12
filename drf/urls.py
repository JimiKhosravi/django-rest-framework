from django.contrib import admin
from django.urls import path
# from api.views import user_profile, update_and_delete_user_profile
from api.views import UserProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('user/', user_profile, name='user-profile'),
    # path('user/<id>/', update_and_delete_user_profile, name='update-user-profile'),
    path('user/', UserProfileView.as_view(), name='user-profile'),
    path('user/<id>/', UserProfileView.as_view(), name='update-user-profile'),
]
