from django.shortcuts import render, redirect, HttpResponse
from session_register_app.models import *
from django.contrib import messages
import datetime 
from django.utils import timezone

def isValid(val):
    usuario = Users.objects.filter(id=val)
    if len(usuario) > 0 :
        user = usuario[0]
        if user.active == True:
            return True
    return False

def index(request):
    id=request.session.get('id')
    usuario = Users.objects.filter(id=id)
    if isValid(id):
        user = usuario[0]
        context = {
                'usuario': user,
            }
        return render(request, 'muro.html', context)
    messages.error (request,'Debe iniciar sesión o registrarse primero')
    return redirect('/')


def content(request):
    id=request.session.get('id')
    usuario = Users.objects.filter(id=id)
    if isValid(id):
        user = usuario[0]
        context = {
                'usuario': user,
                'mensajes': Messages.objects.all(),
                'delete':[],
            }

        for m in context['mensajes']:
            if (timezone.now() - m.create_at) < datetime.timedelta(minutes=30):
                print ('mensaje creado hace menos de 30 min', m.create_at)
                context['delete'].append(m.id)
        # print(context['delete'])
        return render(request, 'content.html', context)
    messages.error (request,'Debe iniciar sesión o registrarse primero')
    return redirect('/')


def post_message(request):
    val = request.session.get('id')
    if isValid(val):
        u = Users.objects.get(id=val)
        Messages.objects.create(user=u, message=request.POST.get('post_message'))
        
    return redirect('/muro/content')


def post_comment(request):
    val = request.session.get('id')
    if isValid(val):
        print(request.POST.get('post_msg'))
        u = Users.objects.get(id=val)
        m = Messages.objects.get(id=request.POST.get('id_msg'))
        Comments.objects.create(user=u, message=m, comment=request.POST.get('post_comment'))
        
    return redirect('/muro/content')


def delete_msg(request):
    val = request.session.get('id')
    if isValid(val):
        print(request.POST.get('id_mes'))

        u = Users.objects.get(id=val)
        m = Messages.objects.get(id=request.POST.get('id_mes'))
        # if (timezone.now() - m.create_at) < datetime.timedelta(minutes=30):
        m.delete()
        
    return redirect('/muro/content')

def delete_cmt(request):
    val = request.session.get('id')
    if isValid(val):
        # print(request.POST.get('id_msg'))

        u = Users.objects.get(id=val)
        c = Comments.objects.get(id=request.POST.get('id_cmt'))
        c.delete()
        
    return redirect('/muro/content')
