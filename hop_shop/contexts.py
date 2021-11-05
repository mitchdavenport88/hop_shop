from products.models import Category, Country


def get_navbar_lists(request):
    countries = Country.objects.all().order_by('name')
    categories = Category.objects.all().order_by('name')
    context = {
        'context_countries': countries,
        'context_categories': categories,
    }

    return context
