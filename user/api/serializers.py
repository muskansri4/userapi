from rest_framework import serializers
from .models import Permission,Role,User

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'
class RoleSerializer(serializers.ModelSerializer):
    class Meta:

        model = Role
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Try to use strong password',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    class Meta:
        model = User
        fields = '__all__'
