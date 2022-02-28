from django.urls import path
from app import views

urlpatterns = [
   
    path('',views.home,name='home'),
    
    path('blog',views.blog,name='blog'),
    
    path('post_blog',views.post_blog,name='post_blog'),

    # category
    path('category',views.category,name='category'),
    path('categoryname/<str:id>',views.category_name,name='category_name'),


 



    #category api
    path('catcrt/', views.CategoryCreateAPIView.as_view(), name='catcrt'),
    path('catlist/', views.CategoryList, name='catlist'),
    path('catdetail/<str:user_name>/', views.CatDetail, name='catdetail'),
    path('cat_filter/<str:category>/', views.cat_filter, name='cat_filter'),




    # contact api
    path('contactcrt/', views.ContactCreateAPIView.as_view(), name='contactcrt'),
    path('contactlist/', views.ContactList, name='contactlist'),


                        
    #comment
    path('cmt/<str:pk>/',views.comment,name='cmt'),
    
    
    #comment api
    path('cmtcreate/<str:pk>/', views.comment_blog_api, name='cmtcreate'),
    path('cmtlist/', views.CommentList, name='cmtlist'),
    path('commentdetail/<str:pk>/', views.CommentDetail, name='commentdetail'),



    # like
    path('like_post/', views.like_post, name="like_post"),

    
    #like api

    path('likecreate/<str:pk>/', views.LikeCreate, name='likecreate'),

    path('likelist/', views.LikeList, name='likelist'),
    path('likedetail/<str:pk>/', views.LikeDetail, name='likedetail'),


    
    
    #blog api
    
    path('blogcrt/', views.BlogCreateAPIView.as_view(), name='blogcrt'),
    path('bloglist/', views.BlogList, name='bloglist'),
    path('blogdetail/<str:pk>/', views.BlogDetail, name='blogdetail'),
    path('blogupdate/<str:pk>/', views.BlogUpdate, name='blogupdate'),
    path('blogdelete/<str:pk>/', views.BlogDelete, name='blogdelete'),

    path('blogdetail1/<str:user_name>/', views.BlogDetail1, name='blogdetail1'), # deatil using user id

    
    
    # search bar

    path('search/', views.search, name='search'),

    # Quote

    path('quotelist/',views.quoteList,name='quoteList'),

    # Reply on comment api
    
    path('comment_reply/<str:pk>/', views.comment_reply, name='comment_reply'),      
    path('replycmtlist/', views.replycmtList, name='replycmtlist'),
    path('replycmtdetail/<str:pk>/', views.ReplycmtDetail, name='replycmtdetail'),

    # trending post

    path('trending_post/', views.trending_post, name='trending_post'),

    path('trending_post_user/<str:user>/', views.trending_post_user, name='trending_post_user'),

    # recent Post
    
    path('recent_post/', views.recent_post, name='recent_post'),


    # Profile

    path('profilecrt/', views.ProfileCreate.as_view(), name='profilecrt'),
    path('profilelist/', views.ProfileList, name='profilelist'),
    path('profiledetail/<str:username>/', views.ProfileDetail, name='profiledetail'),
    path('profileupdate/<str:pk>/', views.ProfileUpdate, name='profileupdate'),
    path('profilegdelete/<str:pk>/', views.ProfileDelete, name='profilegdelete'),

     path('username/<str:id>',views.user_name,name='username'),
     path('countlike/',views.countlike,name='countlike'),
     path('one_like/<int:pk>',views.one_like,name='one_like'),
     path('likeupdate/<str:blog_id>/<str:user_id>',views.likeupdate,name='likeupdate'),

    path('total_blog/<str:user>/',views.total_blog,name='total_blog'),
    path('total_like/<str:user>/',views.total_like,name='total_like'),
    path('total_comment/<str:user>/',views.total_comment,name='total_comment'),
    path('total_view/<str:user>/',views.total_view,name='total_view'),

    path('mobile_view/',views.mobile_view,name='mobile_view'),

    path('mobileview/<str:pk>',views.mobileview,name='mobileview'),
    path('tabletview/<str:pk>',views.tabletview,name='tabletview'),
    path('desktopview/<str:pk>',views.desktopview,name='desktopview'),
    path('sview/<str:pk>',views.sview,name='sview '),

    path('total_user/',views.total_user,name='total_user'),
    path('check_like/<str:blog_id>/<str:user_id>',views.check_like,name='check_like'),






]

