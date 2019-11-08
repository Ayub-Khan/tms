"""Product related views."""

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from rest_framework.views import View

from product.forms import ProductImagesForm
from product.models import Product, ProductImages


class ProductImagesListView(LoginRequiredMixin, View):
    """List images against a product view."""

    def get(self, request, product_id):
        """Render product images list template.."""
        product = get_object_or_404(Product, id=product_id)
        product_images = get_object_or_404(ProductImages, product=product)
        template = loader.get_template('product_images/list-product_images.html')
        product_images_dict = model_to_dict(product_images)
        product_images_dict.pop('id')
        context = {
            'product_images': product_images_dict,
            'product': product
        }
        return render(request, 'product_images/list-product_images.html', context)


product_images_list_view = ProductImagesListView.as_view()


class ProductImagesAddView(LoginRequiredMixin, View):
    """Class based view for adding new product images."""

    def get(self, request, product_id):
        """Return add new product image form."""
        product = get_object_or_404(Product, id=product_id)
        form = ProductImagesForm()
        return render(request, 'product_images/add-product_images.html',
                      {'form': form, 'func': 'Add', 'product': product})

    def post(self, request, product_id):
        """Save product image and redirect to product list."""
        product = get_object_or_404(Product, id=product_id)
        form = ProductImagesForm(request.POST, request.FILES)
        if form.is_valid():
            new_product_images = form.save(commit=False)
            new_product_images.product = product
            new_product_images.save()
            return redirect('product:product_detail', id=product_id)
        else:
            return render(
                request,
                'product_images/add-product_images.html',
                {'form': form, 'func': 'Add', 'product': product}
            )


product_images_add_view = ProductImagesAddView.as_view()


class ProductImagesUpdateView(LoginRequiredMixin, View):
    """Class based view for updating product images."""

    def get(self, request, product_id):
        """Return update product images form."""
        product = get_object_or_404(Product, id=product_id)
        product_images = get_object_or_404(ProductImages, product=product)
        form = ProductImagesForm(instance=product_images)
        return render(request, 'product_images/add-product_images.html',
                      {'form': form, 'func': 'Update'})

    def post(self, request, product_id):
        """Save product and redirect to product list."""
        product = get_object_or_404(Product, id=product_id)
        product_images = get_object_or_404(ProductImages, product=product)
        form = ProductImagesForm(request.POST, request.FILES, instance=product_images)
        if form.is_valid():
            new_product_images = form.save(commit=False)
            new_product_images.product = product
            new_product_images.save()
            return redirect('product:product_detail', id=product_id)
        else:
            return render(request, 'product_images/add-product_images.html', {'form': form, 'func': 'Update'})


product_images_update_view = ProductImagesUpdateView.as_view()
