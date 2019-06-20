########################################################################################################
#---------------------------------- import section-----------------------------------------------------#
########################################################################################################
from django.template import loader # for load html templates
from django.shortcuts import render, get_object_or_404 # for rendering / get_object_or_404 is work like this : when post is exist put it in local variable
from django.http import HttpResponse, Http404 # for define http key word
from django.views.decorators.http import require_GET # for allow a host to send GET/POST on an url
from .models import post # models class
########################################################################################################
#-----------------------------------code execution-----------------------------------------------------#
########################################################################################################
@require_GET
def index(request):
    # get and ordering by published parameter increasing for decreasing -published
    latestPostList = post.objects.order_by("published")
    # load templates
    template = loader.get_template("index.html")
    # send data from controller to view
    context = {
        'posts_list' : latestPostList
    }
    return HttpResponse(template.render(context))
@require_GET
def detail(request, post_id):
    # get post_id from URL 
    Post = get_object_or_404(post, pk = post_id)
    # load templates
    template = loader.get_template("detail.html")
    # send data from controller to view
    context = {
        'post' : Post
    }
    return HttpResponse(template.render(context))
@require_GET
def archive(request, year):
    # published__year means published.year
    yearArchivePost = post.objects.filter(published__year = year)
    # send data from controller to view
    context = {
        "posts" : yearArchivePost
    }
    return render(request, "archive.html" ,context=context)