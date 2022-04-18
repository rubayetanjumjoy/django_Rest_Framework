
from django.urls import path
from djangorestapp.models import Article

from rest_framework.authtoken import views
from djangorestapp.views import ArticleList
from djangorestapp.views import ArticleDetails
 
from .views import *
app_name = 'restapi'
urlpatterns = [
        path('articlelist/',ArticleList.as_view(),name="articlelist"),
        path('articledetails/<int:id>',ArticleDetails.as_view(),name="ArticleDetails"),
        path('regi/',registerUser.some,name='some'),
        path('register/', registerUser.as_view(),name='register'),
        
        
        

]
