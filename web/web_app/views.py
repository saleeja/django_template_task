from django.shortcuts import render
from django.views import View


def function_based_view(request):
    return render(request, 'function_child.html')


class ClassBasedView(View):
    def get(self, request):
        context = {
            'name': 'Saleeja',
            'age': 25,
            'is_adult': False,
            'hobbies': ['reading', 'painting', 'gardening']
        }
        return render(request, 'class_template.html', context)