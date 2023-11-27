from django.db import models

class Contact(models.Model):
    name = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    is_favorite = models.BooleanField()

def create_contact(name, email, phone, is_favorite):
    new_contact = Contact(name=name, email=email, phone=phone, is_favorite=is_favorite)
    new_contact.save()
    return new_contact

def all_contacts():
    return Contact.objects.all()

def find_contact_by_name(name):
    try:
        return Contact.objects.get(name=name)
    except:
        return None

def favorite_contacts():
    fav_contacts = Contact.objects.filter(is_favorite=True)
    return fav_contacts

def update_contact_email(name, new_email):
    update_email = Contact.objects.filter(name=name)
    update_email.update(email=new_email)
    updated_email = Contact.objects.filter(name=name)
    return updated_email

def delete_contact(name):
    delete_contact = Contact.objects.filter(name=name)
    deleted_contact = delete_contact.first()
    delete_contact.delete()
    return deleted_contact
