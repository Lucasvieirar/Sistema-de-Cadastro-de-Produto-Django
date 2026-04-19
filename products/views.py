from django.shortcuts import render


def product_view(request):
    return render(request=request, template_name='products.html',)
