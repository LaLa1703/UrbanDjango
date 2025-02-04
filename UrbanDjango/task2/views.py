from django.shortcuts import render
from django.views import View


# Create your views here.
class ClassView(View):
    def get(self, request):
        return render(request, 'second_task/class_template.html')

def function_view(request):
    return render(request, 'second_task/function_template.html')

