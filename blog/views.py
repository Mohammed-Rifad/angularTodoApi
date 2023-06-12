from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view,permission_classes
from django.http import  JsonResponse
from .serializers import BlogSerializer
from .models import Blog,Like




@api_view(['POST'])
def create_blog(request):
    print(request.data)
    params=request.data
    try:
        serialized_data = BlogSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return JsonResponse({'statusCode': 201, 'message': 'Blog added successfully'})
        else:
            return JsonResponse({'statusCode': 400, 'message': 'Invalid data', 'errors': serialized_data.errors})
    except Exception as e:
        return JsonResponse({'statusCode': 500, 'message': 'Something went wrong', 'error': str(e)})
    
@api_view(['GET'])
def blog_list(request):
    blogs = Blog.objects.filter(approved=True)
    serializer = BlogSerializer(blogs, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def blog_detail(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    if not blog.approved:
        return JsonResponse({'message': 'Blog not approved'}, status=403)
    serializer = BlogSerializer(blog)
    return JsonResponse(serializer.data)

@api_view(['PUT'])

def update_blog(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    serializer = BlogSerializer(blog, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

@api_view(['DELETE'])

def delete_blog(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    blog.delete()
    return JsonResponse({'message': 'Blog deleted successfully'}, status=204)

@api_view(['PUT'])

def approve_blog(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    blog.approved = True
    blog.save()
    return JsonResponse({'message': 'Blog approved'})

@api_view(['PUT'])

def reject_blog(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    blog.approved = False
    blog.save()
    return JsonResponse({'message': 'Blog rejected'})



@api_view(['POST'])
def like_blog(request, blog_id,user):
    params = request.data 
    # id=int(params['user'])
    print(request)
    blog = get_object_or_404(Blog, id=blog_id)
    
    # Check if the user has already liked the blog
    if Like.objects.filter(user_id =user, blog_id=blog.id).exists():
        return JsonResponse({'message': 'You have already liked this blog.'}, status=400)
    
    # Create a new like instance
    like = Like(user_id =user, blog=blog)
    like.save()
    
    return JsonResponse({'message': 'Blog liked successfully.'}, status=200)


@api_view(['GET'])
def view_user_blogs(request,user):
    params = request.data
    blogs = Blog.objects.filter(author_id = user)
    serializer = BlogSerializer(blogs, many=True)
    return JsonResponse(serializer.data)
