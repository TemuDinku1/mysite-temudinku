from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from django.views.decorators.http import require_POST
from .models import Category, Product


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'base/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    
    form = CommentForm()
    return render(request, 'base/product/detail.html',
                           {'product': product,
                            'form': form})


@require_POST
def product_comment(request, product_id):
    product = get_object_or_404(Product,
                                id=product_id,
                                available=True)
    
    form = CommentForm()
    comment = None
    if request.method == 'POST':
        # A comment was posted
        form = CommentForm(data=request.POST)
        if form.is_valid():
            # Create a Comment object without saving it to the database
            comment = form.save(commit=False)
            # Assign the post to the comment
            comment.product = product
            # Save the comment to the database
            comment.save()
    return render(request, 'base/product/comment.html',
                           {'product': product,
                            'form': form,
                            'comment': comment})


def product_services(request):
    return render(request,
                  'base/product/services.html',
                  {})


def product_about(request):
    return render(request,
                  'base/product/about.html',
                  {})


def product_contact(request):
    return render(request,
                  'base/product/contact.html',
                  {})
