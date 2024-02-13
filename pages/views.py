from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
from django import forms
from django.shortcuts import render, redirect



# Create your views here.
class homePageView(TemplateView):
    template_name="pages/home.html"

class Product:
    products = [
         {"id":"1", "name":"TV", "description":"Best TV Precio: 1.000.000 COP"},
         {"id":"2", "name":"iPhone", "description":"Best iPhone Precio: 6.500.000 COP"},
         {"id":"3", "name":"Chromecast", "description":"Best Chromecast Precio: 300.000 COP"},
         {"id":"4", "name":"Glasses", "description":"Best Glasses  Precio:740.000 COP"}
    ]
class ProductIndexView(View):
    template_name = 'products/index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] =  "List of products"
        viewData["products"] = Product.products

        return render(request, self.template_name, viewData)

class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        viewData = {}
        product = Product.products[int(id)-1]
        viewData["title"] = product["name"] + " - Online Store"
        viewData["subtitle"] =  product["name"] + " - Product information"
        viewData["product"] = product
        return render(request, self.template_name, viewData)

class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)

class ProductCreateView(View):
    template_name = 'products/create.html'

    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)
    
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            return redirect(form) 
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)


