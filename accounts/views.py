from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from accounts.models import Profile
from accounts.serializers import ProfilesSerializer
from rest_framework.response import Response
from rest_framework import status


class ProfileView(CreateAPIView):
    """ Creating Profile by authenticated User """
    serializer_class = ProfilesSerializer
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()

    def post(self, request, format=None):

        user = self.request.user
        data = self.request.data

        try:
            exante_account_id = data['exante_account_id']
            token = data['token']
        except Exception as e:
            error = str(e).replace("'", "")
            message = {"message": f"{error} is required!"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        Profile.objects.create(user_account=user, exante_account_id=exante_account_id, token=token)
        return Response(status=status.HTTP_201_CREATED)
