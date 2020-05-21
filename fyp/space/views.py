import mimetypes
import os
import re
import threading
from datetime import time
from wsgiref.util import FileWrapper

import self as self
from django.shortcuts import render, render_to_response, redirect
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, StreamingHttpResponse, HttpResponseServerError
from django.template import RequestContext
from django.contrib import auth
from django.views.decorators import gzip
import pafy
from .models import User, Feedback,Location
import cv2
import pdb
import numpy as np
import time
'''
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture('static/empty.mp4')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret, image = self.video.read()

        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@gzip.gzip_page
def index(request):
    return StreamingHttpResponse(gen(VideoCamera()), content_type="multipart/x-mixed-replace;boundary=frame")

'''


def login(request):
    if request.method == "POST":
        uf = UserFormLogin(request.POST)
        if uf.is_valid():

            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            userResult = User.objects.filter(username=username, password=password)
            # pdb.set_trace()
            if (len(userResult) > 0):
                request.session['username'] = username
                Location.objects.create(parkName="EPL parking", address="125 S Prospect Ave Elmhurst, IL 60126").save()
                return redirect('parkselect')
            else:
                return render_to_response('userlogin.html', {'fail': "This user not exist, Please try again"})
    else:
        uf = UserFormLogin()
    return render_to_response("userlogin.html", {'uf': uf})


def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            filterResult = User.objects.filter(username=username)
            if len(filterResult) > 0:
                return render_to_response('register.html', {"errors": "This user already exist"})
            else:

                password1 = uf.cleaned_data['password1']
                password2 = uf.cleaned_data['password2']
                errors = []
                if (password2 != password1):
                    errors.append("Please enter right password")
                    return render_to_response('register.html', {'errors': errors})
                password = password2
                user = User.objects.create(username=username, password=password1)
                user.save()
                return render_to_response('register.html', {'succ': "register successful"})
    else:
        uf = UserForm()
    return render_to_response('register.html', {'uf': uf})


# def feedback(request):
#     if request.method == "POST":
#         ps = CarParkForm(request.POST)
#         if ps.is_valid():
#             parkname = ps.cleaned_data['parkname']
#
#             if parkname == "park1":
#
#                 return render_to_response('success.html', {'no': 10, 'ps': ps, 'hide': "",
#                                                            'link': "fyp.final.avi"})
#             elif parkname == "park2":
#
#                 return render_to_response('success.html', {'no': 20, 'ps': ps, 'hide': "",
#                                                            'link': "https://www.youtube.com/embed/HnJYSWY60nA?autoplay=0&showinfo=0&controls=0"})
#     else:
#         ps = CarParkForm()
#     return render_to_response('success.html', {'ps': ps, 'hide': "none"})

def feedback(request):
    if request.session.get('username'):
        if request.method == "POST":
            ta = textarea(request.POST)
            if ta.is_valid():
                feedb = ta.cleaned_data['Feedback']
                parkname = "EPL Parking"
                username = request.session.get('username')
            fb = Feedback.objects.create(username=username, parkName=parkname,feedbk=feedb)
            fb.save()
            return render(request,'note.html')

        else:
            ta = textarea()
        return render_to_response('feedback.html', {'ta': ta})
    else:
        return HttpResponse("Please login first!")



def parkselect(request):
    if request.session.get('username'):
        return render(request,'success.html')
    else:
        return HttpResponse("Please login first!")


class UserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password Confirm', widget=forms.PasswordInput())


class UserFormLogin(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())


park = [
    ('park1', 'Park1'),
    ('park2', 'Park2'),
]


# class CarParkForm(forms.Form):
#     parkname = forms.CharField(label='Select Car Park: ', widget=forms.Select(choices=park))

class textarea(forms.Form):
    Feedback = forms.CharField(widget=forms.Textarea(attrs={"rows":20, "cols":60}))