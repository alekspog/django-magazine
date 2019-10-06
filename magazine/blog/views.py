from django.shortcuts import render
from django.views import View

class BlogView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'blog/index.html')

