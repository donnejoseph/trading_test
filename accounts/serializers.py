from rest_framework import serializers
from accounts.models import UserAccount, Profile


class UserAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAccount
        fields = ("id", "name", "email")


class ProfilesSerializer(serializers.ModelSerializer):

    user_account = UserAccountSerializer()

    class Meta:

        model = Profile
        fields = ("user_account", "exante_account_id")
