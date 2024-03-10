from django.contrib import admin
from .models import *
from .models import Feedback
from .models import ProductDetails


# Register your models here.
admin.site.register(ProductDetails)
admin.site.register(Feedback)