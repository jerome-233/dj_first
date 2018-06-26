from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from users.models import BookInfo


def index(request):
    """
    index视图
    :param request: 包含了请求信息的请求对象
    :return: 响应对象
    """
    books = BookInfo.objects.all()
    context = {
        'message': "hello world I`ll fuck you",
        'books': books
    }
    # return HttpResponse("hello the world!")
    return render(request, 'index.html', context)
