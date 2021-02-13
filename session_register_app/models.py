from __future__ import unicode_literals
from django.db import models
import re
import datetime

class validacion(models.Manager):
    def validations(self, postData):
        errors = {}
        if 'email' in postData:
            if len(postData.get('fname')) < 2 and len(postData.get('lname')) < 2:
                errors['nombre'] = 'El campo nombre y el campo apellido deberían ser de al menos 2 carácteres'
            
            EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            mail = Users.objects.filter(email=postData['email'])
            if len(postData.get('email')) > 0:
                if not EMAIL_REGEX.match(postData['email']):
                    errors['email'] = "El formato de email no es válido!"
                if len(mail) > 0:
                    errors['email'] = 'Ya exite alguien registrado con el mismo email'
            else:
                errors['email'] = 'El campo email no debería estar vacío'

            if len(postData.get('password')) < 8:
                errors['lenpw'] = 'La contraseña dería ser de al menos 8 carácteres'

            if postData.get('password') != postData.get('password2'):
                errors['password'] = 'Las contraseñas no coinciden'

            if postData.get('date'):
                date = datetime.datetime.strptime(postData['date'], "%Y-%m-%d")
                now = datetime.datetime.now()
                print(now-date)
                if now <= date:
                    errors['date'] = 'La fecha de nacimento debe estar en pasado'
                if now - date < datetime.timedelta(days=4745):
                    errors['date'] = 'Deberías tener al menos 13 años para registrarte'
            else:
                errors['date'] = 'date should not be empty'
        else:
            errors['error'] = 'Debe registrarse o loguearse primero'
            return errors
        return errors

class Users(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255)
    fday = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255)
    objects = validacion()

class Messages(models.Model):
    user = models.ForeignKey(Users, related_name='messages', on_delete = models.CASCADE)
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Comments(models.Model):
    message = models.ForeignKey(Messages, related_name='comments', on_delete = models.CASCADE)
    user = models.ForeignKey(Users, related_name='comments', on_delete = models.CASCADE)
    comment = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)