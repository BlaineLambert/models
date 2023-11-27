from django.db import models

# Create your models here.
from typing import List

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

def create_item(name, description):
    new_item = Item(name = name, description = description)
    new_item.save()
    return new_item

def read_all_items():
    return Item.objects.all()

def search_items(name):
    return Item.objects.get(name = name)

def read_item_by_id(id):
    return Item.objects.get(id = id)

def update_item(name, new_desc):
    var = Item.objects.get(name = name)
    var.description = new_desc
    var.save()
    return var

def delete_item(id):
    var = Item.objects.get(id = id)
    var.delete()
    return var
