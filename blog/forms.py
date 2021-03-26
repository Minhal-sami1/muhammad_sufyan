from django import forms
from django.db.models import fields
from .models import *

class article_form(forms.ModelForm):
    class Meta:
        model = Articles
        fields = {
            "title",
            "details",     
        }
        widgets = {
            "title": forms.TextInput(attrs = {"class": "form-control", "placeholder" : "Name of Article!", "autocomplete": "off", "autofocus" : "on" , "required": ''}),
            "details": forms.Textarea(attrs = {"class": "form-control", "rows": 30, "required": ''})
            }

class lecture_form(forms.ModelForm):
    class Meta:
        model = Lectures
        fields = {
            'title',
            'lecture',
            'description'
        }
        widgets = {
            "title": forms.TextInput(attrs = {"class": "form-control", "placeholder" : "Name of Lecture!", "autocomplete": "off", "autofocus" : "on" , "required": ''}),
            "description": forms.Textarea(attrs = {"class": "form-control",  "rows": 30, "required": ''}),
            "lecture": forms.FileInput(attrs = {"class": "form-control", "accept": "video/*", "required": '' })
        }

class gallery_form(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = {
            'title',
            'picture'
        }
        widgets = {
            "title": forms.TextInput(attrs = {"class": "form-control", "placeholder" : "Name of Image!", "autocomplete": "off", "autofocus" : "on" , "required": ''}),
            "picture": forms.FileInput(attrs = {"class": "form-control", "required": ''})
        }
