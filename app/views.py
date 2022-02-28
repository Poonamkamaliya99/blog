from traceback import print_tb
from unicodedata import category
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from .models import Blog,Comment, Contact,Like,Category,Quote,Profile,Replycomment
from user.models import CustomUser
from user.serializers import UserSerializer
from .serializers import BlogSerializer,CommentSerializer,CategorySerializer,LikeSerializer, CategorySerializer, ContactSerializer,QuoteSerializer,ProfileSerializer,ReplycommentSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.decorators import login_required
from django.urls import reverse

from rest_framework.views import APIView
from rest_framework import status

from rest_framework import generics
import time
# Create your views here.

def home(request):
    return render(request, 'home.html')

def blog(request):
    blog=Blog.objects.all()
    user=request.user
    comment=Comment.objects.filter(blog=blog)
    category = Category.objects.all()

  
    
    
    context={
        'blogs':blog,
        'comments':comment,
        'user':user,
        'category':category,
        # 'num_likes':num_likes, 
       
    }
    return render(request, 'blog.html', context)


# blog post view

def post_blog(request):
    if request.method=='POST':

        title=request.POST.get('title')
        thought=request.POST.get('thought')

        desc=request.POST.get('desc')
        desc1=request.POST.get('desc1')

        image = request.FILES.get('image')
        image1=request.FILES.get('image1')

        category=Category.objects.filter()


        blog=Blog(title=title, category=category, thought=thought, desc=desc, desc1=desc1, image=image, image1=image1, user_name=request.user)

        try:
            blog.save()
        except Exception:
            print(blog)
        messages.success(request,'blog has been sent seccessfully')
        return redirect('post_blog')
    return render(request, 'blog_post.html')





# add category in blog


def category(request):
    if request.method=='POST':
        name=request.POST.get('name')
        
        cat=Category(name=name)

        cat.save()
        messages.success(request,'category has been sent seccessfully')
        
        return redirect('category')   
         
    return render(request, 'category.html')

@api_view(['GET'])
def category_name(request,id):
    category=Category.objects.filter(pk=id)
    serializer = CategorySerializer(category, many=True)
    
    return Response(serializer.data)




class CategoryCreateAPIView(CreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer



@api_view(['GET'])
def CategoryList(request):
    category=Category.objects.all()
    serializer=CategorySerializer(category, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def CatDetail( request, user_name):
    category=Category.objects.filter(user=user_name)
    
    
    serializer=CategorySerializer(category, many=True)
    return Response(serializer.data)



# class cat_filter(generics.ListAPIView):
#     serializer_class = BlogSerializer

#     def get_queryset(self):
#         cat = self.request.query_params.get('name')
#         return Blog.objects.filter(category__name__iexact=cat)


@api_view(['GET'])
def cat_filter( request, category):
    cat=Blog.objects.filter(category=category)
    
    
    serializer=BlogSerializer(cat, many=True)
    return Response(serializer.data)




# like on blog post    

@login_required(login_url="/admin/")

def like_post(request):
    
    user = request.user
    
    if request.method=='POST':
        blog_id = request.POST.get('blog_id')
        blog_obj = Blog.objects.get(id = blog_id)

        if user in blog_obj.liked.all():
            blog_obj.liked.remove(user)
        else:
            blog_obj.liked.add(user)
        
        like , created= Like.objects.get_or_create(user=user , blog_id=blog_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like_value = 'Like'

        like.save()

    return redirect('blog')



# Like Serializer

@api_view(['GET','POST'])
def LikeCreate(request, pk):
    try:
        blog = get_object_or_404(Blog, id=pk)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        like = Like.objects.filter(blog=blog)
        serializers = LikeSerializer(like,many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = LikeSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def LikeList(request):
    like=Like.objects.all()
    serializer=LikeSerializer(like, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def LikeDetail( request, pk):
    like=Like.objects.filter(id=pk)
    
    serializer=LikeSerializer(like, many=True)
    return Response(serializer.data)







#comment


@login_required(login_url="/admin/")
def comment(request,pk):
    if request.method=='POST':
        blog=Blog.objects.get(id=pk)
        print(blog)

        content=request.POST.get('content')
        print(content)

        email=request.POST.get('email')
        print(email)

        website=request.POST.get('website')
        print(website)

        cmt=Comment(content=content, email=email, website=website, blog=blog, user=request.user)

        try:
            cmt.save()
            print(cmt)

        except Exception:
            print(cmt)
        messages.success(request,'blog has been sent seccessfully')
        return redirect('blog')
    return render(request, 'comment.html')


#comment serializer



@api_view(['GET','POST'])
def comment_blog_api(request, pk):
    try:
        blog = get_object_or_404(Blog, id=pk)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        comments = Comment.objects.filter(blog=blog)
        serializers = CommentSerializer(comments,many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def CommentList(request):
    cmt=Comment.objects.all().order_by('-id')
    serializer=CommentSerializer(cmt, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def CommentDetail( request, pk):
    cmt=Comment.objects.filter(id=pk).order_by('-id')
    
    serializer=LikeSerializer(cmt, many=True)
    return Response(serializer.data)







# Reply on comment


@login_required(login_url="/admin/")
def replycomment(request,pk):
    if request.method=='POST':
        comment=Comment.objects.get(id=pk)
        reply_body=request.POST.get('reply_body')
    
        cmt_reply=Replycomment(reply_body=reply_body, comment=comment,  user=request.user)
        
        try:
            cmt_reply.save()

        except Exception:
            print(cmt_reply)
        messages.success(request,'reply comment has been sent seccessfully')
        return redirect('blog')
    return render(request, 'reply.html')


# Reply on comment serialize


@api_view(['GET','POST'])
def comment_reply(request, pk):
    try:
        comment = get_object_or_404(Comment, id=pk)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        replies = Replycomment.objects.filter(comment=comment)
        serializers = ReplycommentSerializer(replies,many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ReplycommentSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def replycmtList(request):
    replycmt=Replycomment.objects.all()
    serializer=ReplycommentSerializer(replycmt, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def ReplycmtDetail( request, pk):
    reply=Replycomment.objects.filter(id=pk)
    
    serializer=ReplycommentSerializer(reply, many=True)
    return Response(serializer.data)



#blog serializer

class BlogCreateAPIView(CreateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    

@api_view(['GET'])
def BlogList(request):
    blog=Blog.objects.all()
    b= Blog.objects.values()
    serializer=BlogSerializer(blog, many=True)


    # for i in blog:
    #     print(i[0]['category'])


    return Response(serializer.data)

@api_view(['GET'])
def BlogDetail( request, pk):
    blog=Blog.objects.filter(id=pk)
    c = Blog.objects.filter(id=pk).values()
    count = c[0]['v']
    # time.sleep(15)

    Blog.objects.filter(id=pk).update(v=count+1)
    serializer=BlogSerializer(blog, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def BlogDetail1( request, user_name):
    blog=Blog.objects.filter(user_name=user_name).order_by('-id')
   
    
    serializer=BlogSerializer(blog, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def BlogUpdate( request, pk):
    blog=Blog.objects.get(id=pk)
    serializer=BlogSerializer(instance=blog, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def BlogDelete( request, pk):
    blog=Blog.objects.get(id=pk)
    blog.delete()
    return Response('deleted')





#contact api

class ContactCreateAPIView(CreateAPIView):
    queryset=Contact.objects.all()
    serializer_class=ContactSerializer



@api_view(['GET'])
def ContactList(request):
    contact=Contact.objects.all()
    serializer=ContactSerializer(contact, many=True)
    return Response(serializer.data)










   

# from django.http import HttpResponse
# from user.models import CustomUser
# from user.serializers import UserSerializer
# def username(request):
#     u = request.user
#     username = CustomUser.objects.filter(email=u)
#     print(username)
#     serializer = UserSerializer(username)
    
#     return Response(serializer.data)


    # return HttpResponse("test")




@api_view(['GET'])
def quoteList(request):
    quote=Quote.objects.all()
    serializer=QuoteSerializer(quote, many=True)
    return Response(serializer.data)



# search bar 

@api_view(['GET','POST'])
def search(request):
    query= request.POST['query']
    blogs=Blog.objects.filter(title__icontains=query)
    # print(blogs)
    if not blogs:
        blogs1=Blog.objects.filter(category=query)
        
        
        serializer = BlogSerializer(blogs1,many=True)
        return Response(serializer.data)

    serializer = BlogSerializer(blogs,many=True)
    return Response(serializer.data)


    # params = {'blogs': blogs}
    # return render(request, 'search.html',params)


# trending post

from django.utils import timezone
from datetime import  timedelta


@api_view(['GET'])

def trending_post(request):
    blog=Blog.objects.filter( v__gt=0).order_by('-v')[0:3]
    serializer=BlogSerializer(blog, many=True)
    return Response(serializer.data)


@api_view(['GET'])

def trending_post_user(request,user):
    # user=request.user
    blog=Blog.objects.filter(user_name=user, s_view__gt=0).order_by('-s_view')[0:3]
    serializer=BlogSerializer(blog, many=True)
    return Response(serializer.data)

# recent post


@api_view(['GET'])
def recent_post(request):
    d = timezone.now() - timedelta(days=1000)
    blog=Blog.objects.filter(date_added__gte=d).order_by('-date_added')[0:3]
    serializer=BlogSerializer(blog, many=True)
    return Response(serializer.data)


# profile serializer

class ProfileCreate(CreateAPIView):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer

@api_view(['GET'])
def ProfileList(request):
    p=Profile.objects.all()
    serializer=ProfileSerializer(p, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def ProfileDetail( request, username):
    p=Profile.objects.filter(username=username)
    
    
    serializer=ProfileSerializer(p, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def ProfileUpdate( request, pk):
    p=Profile.objects.get(id=pk)
    serializer=ProfileSerializer(instance=p, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def ProfileDelete( request, pk):
    p=Profile.objects.get(id=pk)
    p.delete()
    return Response('deleted')
 


@api_view(['GET'])
def user_name(request,id):
    u=CustomUser.objects.filter(pk=id)
    serializer = UserSerializer(u, many=True)
    
    return Response(serializer.data)

from django.http import JsonResponse

def one_like(request,pk):
    b = Blog.objects.all().values('id')
    b_list = []
    l_list = []
    l_dic = {}
    for i in b:
        b_list.append(i['id'])
    
  
    l = Like.objects.all().values('blog')
    l1 = Like.objects.all().values('value')

    for i in range(len(l)):
        print(type(l[i]['blog']))
        if l1[i]['value'] == 'Unlike':
            # i=str(i)
            Like.objects.filter(blog=str(l[i]['blog']))

            # print(l1[i])

    for i in l:

        l_list.append(i['blog'])

    

    for i in b_list:

        l_dic[i]=l_list.count(i)

    for i in range(len(l)):
        print(type(l[i]['blog']))
        if l1[i]['value'] == 'Unlike':
            # i=str(i)
            Like.objects.filter(blog=str(l[i]['blog']))

            # print(l_dic[l[i]['blog']])
            

            l_dic[l[i]['blog']] = l_dic[l[i]['blog']]-1

    # print(pk)
    temp = l_dic[pk]

    print(temp)

    return JsonResponse(temp,safe=False)
    

    

@api_view(['GET'])
def countlike(request):
    b = Blog.objects.all().values('id')
    b_list = []
    l_list = []
    l_dic = {}
    for i in b:
        b_list.append(i['id'])
    
  
    l = Like.objects.all().values('blog')
    for i in l:
        l_list.append(i['blog'])

    

    for i in b_list:
        l_dic[i]=l_list.count(i)

    




        # print(i['blog'])
    # blog=Blog.objects.filter(id=pk)
    # c = Blog.objects.filter(id=pk).values()
    # count = c[0]['v']

    # Blog.objects.filter(id=pk).update(v=count+1)
    # serializer=BlogSerializer(blog, many=True)
    return JsonResponse(l_dic)


@api_view(['GET'])
def likeupdate(request,blog_id,user_id):
    l = Like.objects.filter(blog=blog_id,user=user_id).values("value")

    user = request.user

    for i in l:
        print(i['value'])
        if i['value'] == 'Like':
            print("yes")
            Like.objects.filter(blog=blog_id,user=user_id).update(value='Unlike')
            return JsonResponse(i['value'],safe=False)

        
        else:
            Like.objects.filter(blog=blog_id,user=user_id).update(value='Like')


            return JsonResponse(i['value'],safe=False)


from user.models import CustomUser
@api_view(['GET'])
def total_blog(request,user):
    print("The user is: ",user)
    # user = request.user

    b = Blog.objects.filter(user_name=user)


    count = 0
  

    for i in b:
 

        count = count+1
   


    
    
    data={}


    data['total_blog'] = count


    
    return JsonResponse(data,safe=False)


@api_view(['GET'])
def total_like(request,user):
    # user = request.user
    l = Like.objects.filter(user=user).values('value')
    count = 0
    for i in l:
        if i['value'] == 'Like':

            count = count+1

    data={}
    data['total_like'] = count
    
    return JsonResponse(data,safe=False)

@api_view(['GET'])
def total_comment(request,user):
    # user = request.user
    c = Comment.objects.filter(user=user).values('content')
    count = 0
    for i in c:
        count = count+1
    
    data={}
    data['total_comment'] = count
    
    return JsonResponse(data,safe=False)

@api_view(['GET'])
def total_view(request,user):
    print(user)
    # user = request.user
    b = Blog.objects.filter(user_name=user).values('v')
    count = 0
    for i in b:
        count = count+1

    
    data={}
    data['total_view'] = count
    
    return JsonResponse(data,safe=False)

@api_view(['GET'])
def mobile_view(request):
    b = Blog.objects.all().values('mobile_view')
    count = 0
    for i in b:
        count = count+1

    
    return JsonResponse(count,safe=False)

@api_view(['GET'])
def mobileview( request, pk):
    blog=Blog.objects.filter(id=pk)
    c = Blog.objects.filter(id=pk).values()
    count = c[0]['mobile_view']

    Blog.objects.filter(id=pk).update(mobile_view=count+1)
    serializer=BlogSerializer(blog, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def tabletview( request, pk):
    blog=Blog.objects.filter(id=pk)
    c = Blog.objects.filter(id=pk).values()
    count = c[0]['tablet_view']

    Blog.objects.filter(id=pk).update(tablet_view=count+1)
    serializer=BlogSerializer(blog, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def desktopview( request, pk):
    blog=Blog.objects.filter(id=pk)
    c = Blog.objects.filter(id=pk).values()
    count = c[0]['desktop_view']

    Blog.objects.filter(id=pk).update(desktop_view=count+1)
    serializer=BlogSerializer(blog, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def sview( request, pk):
    blog=Blog.objects.filter(id=pk)
    c = Blog.objects.filter(id=pk).values()
    count = c[0]['s_view']

    Blog.objects.filter(id=pk).update(s_view=count+1)
    serializer=BlogSerializer(blog, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def total_user(request):
    u = CustomUser.objects.all()
    count = 0
    for i in u:
        count = count+1
    data={}
    data['total_user'] = count
    return JsonResponse(data,safe=False)


@api_view(['GET'])
def check_like(request,blog_id,user_id):
    # user = request.user
    l = Like.objects.filter(blog=blog_id,user=user_id)
    l1 = Like.objects.filter(blog=blog_id,user=user_id).values("value")
    l2 = Like.objects.filter(blog=blog_id,user=user_id).values("id")




    data = {}

    if not l:
        data ['value'] = "False"
        return JsonResponse(data,safe=False)

    else:
        for i in l1:
            print("This is i",i)
            if i["value"] == "Unlike":
                data ['value'] = "False"
                return JsonResponse(data,safe=False)

            else:
                data ['value'] = "True"
                return JsonResponse(data,safe=False)

