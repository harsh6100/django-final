from rest_framework import serializers

from account.models import Account


# class LoginSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Account
# 		fields = ['email', 'password',]

# 		extra_kwargs = {'password': {'write_only': True}}

# 	def validate(self, data):
# 		password = data.get('password')
# 		email = data.get('email')


class RegistrationSerializer(serializers.ModelSerializer):	

	class Meta:
		model = Account
		fields = ['email', 'username', 'password']

