from .models import Comment
from .serializers import CommentSerializer
from accounts.models import User
from accounts.permissions import IsVerified
from blogs.models import Blog
from django.shortcuts import render
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
            }, status=status.HTTP_404_NOT_FOUND
        )
    return blog


def get_comment(comment_id:str):
    try:
        comment = Comment.objects.get(id=comment_id)
    except Comment.DoesNotExist:
        return Response(
            {
                'success':False,
                'message':'Comment does not exist'
            }, status=status.HTTP_404_NOT_FOUND
        )
    return comment


@api_view(['POST'])
@permission_classes([IsVerified])
def add_comment(request, blog_id:str):
    if request.method == 'POST':
        user = request.user
        blog = get_blog(blog_id=blog_id)
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=user, blog=blog)

            return Response(
                {
                    'success':True,
                    'message':'Comment successfully added',
                    'comment':serializer.data
                }, status=status.HTTP_201_CREATED
            )
        return Response(
            {
                'success':False,
                'message':serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST
        )
        

@api_view(['GET'])
def get_specific_comment(request, comment_id:str):
    if request.method == 'GET':
        comment = get_comment(comment_id=comment_id)
        serializer = CommentSerializer(comment)

        return Response(
            {
                'success':True,
                'comment':serializer.data
            }, status=status.HTTP_200_OK
        )


@api_view(['GET'])
def get_comments_on_blog(request, blog_id:str):
    if request.method == 'GET':
        blog = get_blog(blog_id=blog_id)
        comments = Comment.objects.filter(blog=blog)
        serializer = CommentSerializer(comments, many=True)

        return Response(
            {
                'success':True,
                'comments':serializer.data
            }, status=status.HTTP_200_OK
        )


@api_view(['GET'])
def get_comments_by_user(request, uid:str):
    if request.method == 'GET':
        user = User.objects.get(id=uid)

        if not user:
            return Response(
                {
                    'success':False,
                    'message':'User not found!'
                }, status=status.HTTP_404_NOT_FOUND
            )

        comments = Comment.objects.filter(user=user)
        serializer = CommentSerializer(comments, many=True)

        return Response(
            {
                'success':True,
                'comments':serializer.data
            }, status=status.HTTP_200_OK
        )


@api_view(['DELETE'])
@permission_classes([IsVerified])
def delete_comment(request, comment_id:str):
    if request.method == 'DELETE':
        user = request.user
        comment = get_comment(comment_id=comment_id)

        if user != comment.user and not user.is_staff:
            return Response(
                {
                    'success':False,
                    'message':'You are not authorized to delete this comment'
                }, status=status.HTTP_403_FORBIDDEN
            )

        comment.delete()
        return Response(
            {
                'success':True,
                'message':'Comment deleted!'
            }, status=status.HTTP_204_NO_CONTENT
        )