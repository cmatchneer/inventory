from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


from .models import Product
from .form import ProductForm


#confim user logged.
@login_required()
#add new product form
def product_form_view(request):
    
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "product/product_form.html", context)

@login_required()
#full product list
def product_list_view(request):
    queryset=Product.objects.all()
    context={
      "product_list":queryset,

    }
    return render(request,"product/product_detail.html",context)
@login_required()
#delete product
def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "product/product_delete.html", context)

@login_required()
#update product 
def product_update_view(request, id=id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "product/product_form.html", context)
    

