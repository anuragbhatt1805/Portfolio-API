from rest_framework import serializers
from blog.models import Blog, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['name', 'comment']
        # read_only_fields = ['name', ]

    def save(self, blog, **kwargs):
        if "name" not in self.validated_data.keys() or self.validated_data['name'] == '':
            self.validated_data['name'] = 'Anonymous'
        comment = Comment(blog=blog,
                        name = self.validated_data['name'],
                        comment=self.validated_data['comment'])
        comment.save()
        return comment


class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Blog
        fields = ['id', 'title', 'body', 'picture', 'likes', 'comments']
        read_only_fields = ['id', 'title', 'body', 'picture', 'likes']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        comments = Comment.objects.all().filter(blog=representation.get('id'))
        if comments.exists():
            representation['comments'] = CommentSerializer(comments, many=True).data
        return representation