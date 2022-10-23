import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView

from HW27.settings import TOTAL_ON_PAGE
from ads.models import Category


class CategoriesListView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object_list = self.object_list.order_by('name')
        paginator = Paginator(self.object_list, TOTAL_ON_PAGE)
        page = request.GET.get('page')
        obj = paginator.get_page(page)
        response = {}
        category_list = [{'id': cat.pk, 'name': cat.name} for cat in obj]

        response['items'] = category_list
        response['total'] = self.object_list.count()
        response['num_pages'] = paginator.num_pages

        return JsonResponse(response, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesCreateView(CreateView):
    model = Category
    fields = ['name']

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        category = get_object_or_404(Category, name=data['category'])

        cat = Category.objects.create(category=category)

        return JsonResponse({'id': cat.pk,
                             'name': cat.name,
                             }, safe=False)


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        cat = self.get_object()
        return JsonResponse({'id': cat.pk,
                             'name': cat.name,
                             }, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        data = json.loads(request.body)

        if 'name' in data:
            self.object.name = data['name']

        self.object.save()

        return JsonResponse({'id': self.object.pk,
                             'name': self.object.name
                             }, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({"status": "ok"}, status=204)
