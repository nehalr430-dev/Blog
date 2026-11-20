from django.shortcuts import render

contents = [
    {
        'author' : 'Nehal Rahman',
        'title' : '1st Blog',
        'content' : 'This is my frist blog',
        'date' : 'May 24,2020'
    },
    {
        'author' : 'Khalid Rahman',
        'title' : '2nd Blog',
        'content' : 'This is my second blog',
        'date' : 'May 2,2020'
    }
]

def home(request):
    context = {
        'contents' : contents
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'about'})
