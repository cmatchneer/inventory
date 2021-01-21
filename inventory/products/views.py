from django.shortcuts import render, get_object_or_404
from .models import Product
from .form import ProductForm
# Create your views here.

def product_form_view(request):
    obj = Product.objects.get(id=2)
    form = ProductForm(request.POST or None,instance=obj )
    if form.is_valid():
        form.save()
        
    context = {
        'form': form
    }
    return render(request, "product/product_form.html", context)
def product_list_view(request):
    queryset=Product.objects.all()
    context={
      "product_list":queryset

    }
    return render(request,"product/product_detail.html",context)

 
