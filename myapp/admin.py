from django.contrib import admin

# Register your models here.
from myapp.models import Article

admin.site.register(Article)
