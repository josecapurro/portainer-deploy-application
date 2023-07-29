from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class StoreView(View):
    template_name = 'store.html'
    def get(self, request):
        return render(request, self.template_name)
