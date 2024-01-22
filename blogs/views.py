from .models import Blog
from .serializers import BlogSerializer
from accounts.models import User
from accounts.permissions import IsVerified
from datetime import timedelta
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


def get_blog(blog_id:str):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        return Response(
            {
                'success':False,
                'message':'Blog does not exist'
            }, status=status.HTTP_400_BAD_REQUEST
        )
    return blog


def get_user(uid:str):
    try:
        user = User.objects.get(id=uid)
    except User.DoesNotExist:
        return Response(
            {
                'success':False,
                'message':'User does not exist'
            }, status=status.HTTP_400_BAD_REQUEST
        )
    return user


@api_view(['POST'])
@permission_classes([IsVerified])
def create_blog_view(request):
    if request.method == 'POST':
        user = request.user
        serializer = BlogSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(author=user)

            return Response(
                {
                    'success':True,
                    'message':'Blog created successfully!',
                    'blog':serializer.data
                }, status=status.HTTP_201_CREATED
            )
        return Response(
            {
                'success':False,
                'message':serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET'])
def get_specific_blog_view(request, blog_id:str):
    if request.method == 'GET':
        blog = get_blog(blog_id=blog_id)
        print(blog.author)
        
        serializer = BlogSerializer(blog)

        return Response(
            {
                'success':True,
                'blog':serializer.data
            }, status=status.HTTP_200_OK
        )


@api_view(['GET'])
def get_all_user_blogs_view(request, uid:str):
    if request.method == 'GET':
        user = get_user(uid=uid)
        blogs = Blog.objects.filter(author=user)
        serializer = BlogSerializer(blogs, many=True)

        return Response(
            {
                'success':True,
                'message':f'Below are all the blogs by {user.username}',
                'blogs':serializer.data
            }, status=status.HTTP_200_OK
        )


@api_view(['GET'])
def get_all_blogs_view(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)

        return Response(
            {
                'success':True,
                'blogs':serializer.data
            }, status=status.HTTP_200_OK
        )


@api_view(['GET'])
def get_blogs_within_last_3_months_view(request):
    if request.method == 'GET':
        timeframe = timezone.now() - timedelta(days=90)
        blogs = Blog.objects.filter(created_at__gte=timeframe)
        serializer = BlogSerializer(blogs, many=True)

        return Response(
            {
                'success':True,
                'message':'Below are blogs posted within last 3 months',
                'blogs':serializer.data
            }, status=status.HTTP_200_OK
        )


@api_view(['PUT', 'PATCH'])
@permission_classes([IsVerified])
def update_blog_view(request, blog_id:str):
    if request.method == 'PUT' or request.method == 'PATCH':
        user = request.user
        blog = get_blog(blog_id=blog_id)

        if user != blog.author:
            return Response(
                {
                    'success':False,
                    'message':'You cannot make changes to this blog. You are not the author'
                }, status=status.HTTP_403_FORBIDDEN
            )

        serializer = BlogSerializer(blog, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    'success':True,
                    'message':'Update successful',
                    'blog':serializer.data
                }, status=status.HTTP_200_OK
            )
        return Response(
            {
                'success':True,
                'message':serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['DELETE'])
@permission_classes([IsVerified])
def delete_blog_view(request, blog_id:str):
    if request.method == 'DELETE':
        user = request.user
        blog = get_blog(blog_id=blog_id)

        if user != blog.author and not user.is_staff:
            return Response(
                {
                    'success':False,
                    'message':'You do not have the permission to perform this action. You are not the author'
                }, status=status.HTTP_403_FORBIDDEN
            )

        blog.delete()
        return Response(
            {
                'success':True,
                'message':'Blog deleted successfully'
            }, status=status.HTTP_204_NO_CONTENT
        )
