from djangorestapp.models import Article
from rest_framework import fields, serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields='__all__'
            
    def create(self, validated_data):
        user =User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
        
                
    
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model= Article
        fields='__all__'
















"""
class ArticleSerializer(serializers.Serializer):
       title = serializers.CharField(max_length=200)
       authorname=serializers.CharField(max_length=200)
       email = serializers.EmailField(max_length=20)
       date = serializers.DateTimeField()
    
       def create(self,validate_data):
           return Article.objects.create(validate_data)
        
       def update(self,instance,validate_datas):
           instance.title=validate_datas.get('title',instance.title)
           instance.authorname=validate_datas.get('title',instance.title)
           instance.email=validate_datas.get('title',instance.title)
           instance.date=validate_datas.get('title',instance.title)
           instance.save()
           return instance
           """