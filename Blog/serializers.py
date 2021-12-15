from rest_framework import serializers
from .models import Comment, Post, Category , Like, PostView

class LikeSerilalizer(serializers.ModelSerializer):
    # user=serializers.StringRelatedField()
    user_id = serializers.IntegerField()
    # post = serializers.StringRelatedField()
    post_id = serializers.IntegerField()
    class Meta:
        model = Like
        fields =('post_id','user_id')
        
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField()
    post = serializers.StringRelatedField()
    post_id = serializers.IntegerField()
    class Meta:
        model = Comment
        fields = ('id','user','user_id','post','post_id','time_stamp','content')



class PostSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField()
    class Meta:
        model = Post
        fields =('id','user','user_id','category','category_id','title','content','image','publish_date',
                 'last_update','status','slug','comment_count','like_count','postview_count')


class CategorySerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Category
        fields ='__all__'
        
class PostviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostView
        fields = '__all__'