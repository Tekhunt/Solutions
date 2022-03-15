from rest_framework import serializers
from db.models.user_model import User
import bcrypt

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= "__all__"
        extra_kwargs = {   #made sure we can only write but not view                 
            'password':{'write_only':True}     
        }

    #hashing the password
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode()
        instance=self.Meta.model(**validated_data, password=hashed)
        instance.save()
        print(hashed)

        return instance  

    
    
   