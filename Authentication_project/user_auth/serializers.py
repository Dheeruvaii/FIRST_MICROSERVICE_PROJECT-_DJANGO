from rest_framework import serializers
from.models import*
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password']
        # extra_kwargs = {
        #     'password':{'write_only':True}           
        # }

    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)

        if(password is not None):
            instance.set_password(password)   #this hashes the password 
        instance.save()
        return instance
    
    
class FavoriteProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteProduct
        fields = '__all__'

       
   