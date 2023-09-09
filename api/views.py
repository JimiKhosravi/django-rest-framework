from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import UserProfileSerializer, CreateUserProfileSerializer
from api.models import UserProfile

# Create your views here.


@api_view(['GET', 'POST'])
def user_profile(request):
    if request.method == 'GET':
        data = UserProfile.objects.all()
        serializer_data = UserProfileSerializer(data, many=True)
        return Response(serializer_data.data)

    if request.method == 'POST':
        req_data = request.data
        serializer = CreateUserProfileSerializer(data=req_data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=201)
        # else:
        #     return Response(serializer.errors, status=400)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
