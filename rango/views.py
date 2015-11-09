from django.shortcuts import render
from django.shortcuts import HttpResponse
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm
from rango.forms import PageForm


# def index(request):
#     print request.META
#     print request.method
#
#     return HttpResponse("Rango says hey there world<br>"
#                         "<a href='/rango/about'>About</a>")

def index(request):
    category_list = Category.objects.order_by('-likes')[0:5]
    page_list = Page.objects.order_by('-views')[0:5]

    content_dict = {'categories': category_list, 'pages': page_list}

    return render(request, 'rango/index.html', content_dict)


def about(request):
    content_dict = {'boldmessage': 'Could u tell me something about yourself?'}

    return render(request, 'rango/about.html', content_dict)


def category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages

        context_dict['category'] = category

    except Category.DoesNotExist:
        pass

    return render(request, 'rango/category.html', context_dict)


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print "form.errors", form.errors

    else:
         form = CategoryForm()

    return render(request, 'rango/add_category.html', {'form': form})


def add_page(request, category_name_slug):
    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        cat = None

    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            page = form.save(commit=False)
            page.category = cat
            page.views = 0
            page.save()
            return category(request, category_name_slug)
        else:
            print "form.errors", form.errors

    else:
        form = PageForm()

    context_dict = {'form': form, 'category': cat, 'category_name_slug': category_name_slug}

    return render(request, 'rango/add_page.html', context_dict)


