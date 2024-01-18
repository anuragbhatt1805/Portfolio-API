# from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from blog.models import Blog
from blog.serializer import BlogSerializer, CommentSerializer
from rest_framework.response import Response


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    @action(detail=True, methods=['POST'])
    def like(self, request, pk=None):
        blog = self.get_object()
        blog.likes += 1
        blog.save()
        return Response({'status': status.HTTP_200_OK, 'message':'Success'})

    @action(detail=True, methods=['POST'])
    def dislike(self, request, pk=None):
        blog = self.get_object()
        if blog.likes > 0:
            blog.likes -= 1
            blog.save()
            return Response({'status': status.HTTP_200_OK, 'message':'Success'})
        else:
            return Response({'status': status.HTTP_400_BAD_REQUEST, 'message':'Bad Request'})

    @action(detail=True, methods=['POST'])
    def comment(self, request, pk=None):
        blog = self.get_object()
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(blog=blog)
            return Response({'status': status.HTTP_201_CREATED, 'message':'Success'})
        else:
            return Response({'status': status.HTTP_400_BAD_REQUEST, 'message':'Bad Request'})
