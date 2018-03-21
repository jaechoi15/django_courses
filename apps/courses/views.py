# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Course

# Create your views here.

def index(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request, "courses/index.html", context)


def create(request):
    name = request.POST['name']
    description = request.POST['description']

    errors = Course.objects.basic_validator(request.POST)

    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    Course.objects.create(name=name, description=description)
    return redirect('/')


def show(request, course_id):
    context = {
        "course": Course.objects.get(id=course_id)
    }
    return render(request, "courses/show.html", context)


def destroy(request, course_id):
    c = Course.objects.get(id=course_id)
    c.delete()
    return redirect('/')