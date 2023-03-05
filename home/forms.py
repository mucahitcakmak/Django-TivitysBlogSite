from django import forms
from django.forms import TextInput, Textarea, FileInput, Select

from .models import Blog, BlogCategory

class NewsCreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ("title", "summary", "text", "slug", "categorys", "image")
        labels = {
            "image": "Image",
            "title": "Title",
            "summary": "Summary",
            "text": "Text",
            "slug": "Slug",
            "categorys": "Category",
        }
        widgets = {
            # "image": FileInput(attrs={"class":"form-control mb-5"}),
            "title": TextInput(attrs={"class":"form-control mb-5 bg-dark text-white"}),
            "summary": TextInput(attrs={"class":"form-control mb-5 bg-dark text-white"}),
            "text": Textarea(attrs={"class":"form-control mb-5 bg-dark text-white"}),
            "slug": TextInput(attrs={"class":"form-control mb-5 bg-dark text-white"}),
            "categorys": Select(attrs={"class":"form-control mb-5 bg-dark text-white"}),
        }
        error_messages = {
            "title":{
                "required": "Bu alan boş bırakılamaz",
                "max_length": "En fazla 40 karakter girebilirsin"
            },
            "summary":{
                "required": "Bu alan boş bırakılamaz",
            }
        }



class NewsEditForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ("title", "summary", "text", "slug", "categorys", "image")
        labels = {
            "image": "Image",
            "title": "Title",
            "summary": "Summary",
            "text": "Text",
            "slug": "Slug",
            "categorys": "Category",
        }
        widgets = {
            # "image": ImageField(attrs={"class":"form-control mb-5"}),
            "title": TextInput(attrs={"class":"form-control mb-5 bg-dark text-white"}),
            "summary": TextInput(attrs={"class":"form-control mb-5 bg-dark text-white"}),
            "text": Textarea(attrs={"class":"form-control mb-5 bg-dark text-white"}),
            "slug": TextInput(attrs={"class":"form-control mb-5 bg-dark text-white"}),
            "categorys": Select(attrs={"class":"form-control mb-5 bg-dark text-white"}),
        }
        error_messages = {
            "title":{
                "required": "Bu alan boş bırakılamaz",
                "max_length": "En fazla 40 karakter girebilirsin"
            },
            "summary":{
                "required": "Bu alan boş bırakılamaz",
            }
        }

class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = BlogCategory
        fields = ("name", "slug")
        labels = {
            "name": "Category Name",
            "slug": "Category Slug",
        }
        widgets = {
            "name": TextInput(attrs={"class":"form-control mb-5 bg-dark text-white"}),
            "slug": TextInput(attrs={"class":"form-control mb-5 bg-dark text-white"}),
        }