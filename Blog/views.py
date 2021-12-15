from .serializers import LikeSerilalizer, PostSerializer , CommentSerializer , CategorySerializer , PostviewSerializer
from rest_framework.viewsets import GenericViewSet , ModelViewSet , mixins
from .models import Like, Post, Comment, Category , PostView
from rest_framework.generics import GenericAPIView , mixins , ListCreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view ,action
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly

class Postview(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class Categoryview(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
   
class Commentview(APIView):
    
    def get(self, request , pk):
        comments = Comment.objects.filter(post_id=pk).order_by('-time_stamp')
        serializer = CommentSerializer(comments, many=True)
        print(request.user)
        return Response(serializer.data)
    
    def post(self,request,pk):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request ,pk):
        comment_item = Comment.objects.filter(id=pk)
        comment_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def likelist(request,post_id,user_id):
    if  request.method == 'GET':
        likes = Like.objects.all().filter(user_id=user_id,post_id=post_id)
        like_count = Like.objects.all().filter(post_id=post_id).count()
        serializer = LikeSerilalizer(likes, many=True)
        return Response([serializer.data,{'like_count':like_count}])
    elif request.method == 'POST':
        serializer = LikeSerilalizer(data=request.data)
        if serializer.is_valid():
            user_id=serializer.validated_data['user_id']
            post_id=serializer.validated_data['post_id']
            likes = Like.objects.all().filter(user_id=user_id,post_id=post_id)
            if bool(likes):
                likes.delete()
            else:
                likes = Like.objects.create(user_id=user_id,post_id=post_id)
                likes.save()
            return Response(serializer.data)

class PostLookCreate(ListCreateAPIView):
    queryset = PostView.objects.all()
    serializer_class = PostviewSerializer