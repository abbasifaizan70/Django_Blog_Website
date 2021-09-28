from django.shortcuts import render
from .models import Post

# posts=[
#     {
#         'author':'Faizan Abbasi',
#         'title':'Blog Post 1',
#         'content':'Testing blog post for me',
#         'date_posted':'22-Sep-2021'
#     }
#     ,
#     {
#         'author':'Usama Ali Qadri',
#         'title':'Blog Post 2',
#         'content':'Testing blog post for Usama',
#         'date_posted':'23-Sep-2021'
#     }
# ]


def home(request):
    context ={
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About Page'})
