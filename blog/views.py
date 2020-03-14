from django.shortcuts import render
from .models import Post
posts=[
    {
        'author':' Minakshi Kudalkar',
        'title':'Chicas Blog',
        'content':'First blog content is this',
        'date_posted':'August 16,2019'
    },
    {
        'author':'Shashank Gupta',
        'title':'Chicos Blog',
        'content':'Second blog content is this. Hey you!',
        'date_posted':'August 17,2019'
    }
]


def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About Page'})