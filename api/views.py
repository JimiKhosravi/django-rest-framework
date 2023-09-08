from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import UserProfileSerializer
from api.models import UserProfile

# Create your views here.


@api_view(['GET', 'POST'])
def user_profile(request):
    data = UserProfile.objects.all()
    serializer_data = UserProfileSerializer(data, many=True)
    return Response(serializer_data.data)
