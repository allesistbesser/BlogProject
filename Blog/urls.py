from django.contrib import admin
from django.urls import path , include
from rest_framework import routers
from .views import Postview, Commentview , Categoryview , likelist , PostLookCreate

router = routers.DefaultRouter()

router.register('post', Postview)
router.register('category', Categoryview)

urlpatterns = [
   path('', include(router.urls)),
   path('comments/<str:pk>',Commentview.as_view() ),
   path('likelist/<int:post_id>/<int:user_id>',likelist ),
   path('look/',PostLookCreate.as_view() ),
   
      
]