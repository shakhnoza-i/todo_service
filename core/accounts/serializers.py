from accounts.models import User
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def save(self):

        password = self.validated_data['password']

        account = User(email=self.validated_data['email'])
        account.set_password(password)
        account.save()

        return account
