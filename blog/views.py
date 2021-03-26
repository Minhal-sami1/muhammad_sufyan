from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import *
from .models import *
# Create your views here.

def login_view(request):
    if request.method == "POST":
        if 'username' in request.POST and 'password' in request.POST:
            # Attempt to sign user in
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)

        # Check if authentication successful
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("all_post"))
            else:
                return render(request, "blog/login-form.html", {
                    "message": "Invalid username and/or password."
                })
    else:
        return render(request, "blog/login-form.html")

def add_articles(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = article_form(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                redirect('super-secret-muhammad-sufyan-admin-place/add_articles')
            else:
                return render(request, "blog/addlectures.html",{
                   'form': article_form,
                   'error': 'The form is not valid maybe something is missing'
                })
        return render(request, "blog/addarticles.html",{
            'form': article_form
        })
def add_lectures(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = lecture_form(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                redirect('super-secret-muhammad-sufyan-admin-place/add_lectures')
            else:
                return render(request, "blog/addlectures.html",{
                   'form': lecture_form,
                   'error': 'The form is not valid maybe something is missing'
                })

        return render(request, "blog/addlectures.html",{
            'form': lecture_form
        })
def add_image(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = gallery_form(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                redirect('super-secret-muhammad-sufyan-admin-place/add_image')
            else:
                return render(request, "blog/addlectures.html",{
                   'form': gallery_form,
                   'error': 'The form is not valid maybe something is missing'
                })
        return render(request, "blog/addimage.html",{
            'form' : gallery_form
        })

def edit_post(request, id, type):
    if request.user.is_authenticated:
        if request.method == "POST":
            # updating data 
            if type == "article":
                data = request.POST
                post = Articles.objects.filter(id = id, status = True).update(title = data["title"], details = data["details"])
                return HttpResponseRedirect(reverse("all_post"))
            if type == "lecture":
                data = request.POST
                post = Lectures.objects.filter(id = id, status = True).update(title = data["title"], description = data["details"])
                return HttpResponseRedirect(reverse("all_post"))          
        # get method
        if type == "article":
            post = Articles.objects.filter(id = id, status = True).first()
            return render(request, "blog/edit.html",{
                "post": post,
                "type": type
            })
        if type == "lecture":
            post = Lectures.objects.filter(id = id, status = True).first()
            return render(request, "blog/edit.html",{
                "post": post,
                "type": type
            })

def edit_articles(request):
    if request.user.is_authenticated:
        posta = Articles.objects.filter(status = True)
        postl = Lectures.objects.filter(status = True)
        postg = Gallery.objects.filter(status = True)
        return render(request, "blog/admin-panel.html",{
            "posts": posta,
            "postl": postl,
            "postg": postg
        })

def delete_post(request, id, type):
    if request.user.is_authenticated:
        if request.method == "POST":
            if type == "article":
                post = Articles.objects.filter(id = id).first()
                if post.picture:
                    post.picture.delete()
                post.delete()
                return HttpResponseRedirect(reverse("all_post"))   
            if type == "lecture":
                post = Lectures.objects.filter(id = id).first()
                if post.lecture and post != None:
                    post.lecture.delete()
                post.delete()
                return HttpResponseRedirect(reverse("all_post"))
            if type == "gallery":
                post = Gallery.objects.filter(id = id).first()
                if post.picture:
                    post.picture.delete()
                post.delete()
                return HttpResponseRedirect(reverse("all_post"))
        # get method
        if type == "article":
            post = Articles.objects.filter(id = id).first()
            return render(request, "blog/delete.html",{
                "post": post,
                "type": type
            })
        if type == "lecture":
            post = Lectures.objects.filter(id = id).first()
            return render(request, "blog/delete.html",{
                "post": post,
                "type": type
            })
        if type == "gallery":
            post = Gallery.objects.filter(id = id).first()
            return render(request, "blog/delete.html",{
                "post": post,
                "type": type
            })

def article_view(request):
    posta = Articles.objects.all()
    counta = Articles.objects.count()
    countl = Lectures.objects.count()
    countg = Gallery.objects.count()
    return render(request, "blog/index.html",{
        "posts": posta,
        "counta": counta,
        "countl":countl,
        "countg": countg
    })

def lecture_view(request):
    posts = Lectures.objects.all()
    counta = Articles.objects.count()
    countl = Lectures.objects.count()
    countg = Gallery.objects.count()

    return render(request, "blog/alllectures.html",{
        "posts": posts,
        "counta": counta,
        "countl":countl,
        "countg": countg
    })

def gallery_view(request):
    posts = Gallery.objects.all()
    return render(request, "blog/gallery.html",{
        "posts": posts
    })

def post_view(request, id, type):
    counta = Articles.objects.count()
    countl = Lectures.objects.count()
    countg = Gallery.objects.count()
    if type == "article":
        post = Articles.objects.filter(id = id).first()
        return render(request, "blog/article.html",{
            "post": post,
            "type": type,
            "counta": counta,
            "countl":countl,
            "countg": countg
        })
    if type == "lecture":
        post = Lectures.objects.filter(id = id).first()
        return render(request, "blog/lecture.html",{
            "post": post,
            "type": type,
            "counta": counta,
            "countl":countl,
            "countg": countg
        })
def search(request):
    if request.method == "POST":
         form_data = request.POST["q"]
         chk = "hello"
         cnt = 0
         lst = []
         entrya = Articles.objects.all()
         entryl = Lectures.objects.all()
         for entry in entrya:
             dicta = entry.title
             if form_data.upper() == dicta.upper():
                 cnt = 999
                 lst.append(entry)
             elif form_data.upper() in dicta.upper():
                 cnt = 555
                 lst.append(entry)
         for entry in entryl:
             dicta = entry.title
             if form_data.upper() == dicta.upper():
                 cnt = 999
                 lst.append(entry)
             elif form_data.upper() in dicta.upper():
                 cnt = 555
                 lst.append(entry)
             
         if cnt == 555 or cnt == 0 or cnt == 999:
             return render(request, "blog/search.html",{
                 "lst" : lst
             })