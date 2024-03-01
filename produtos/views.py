from django.shortcuts import render
from django.views import View
import os

# Create your views here.

class Home(View):
    template_name = os.path.join('home','index.html')
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)