from products.models import Category, Country


def get_navbar_lists(request):
    """
    A function that retrieves the names of all the countries and
    categories currently in the database to populate the drop down
    menus in the navigation bar
    """
    countries = Country.objects.all().order_by('name')
    categories = Category.objects.all().order_by('name')
    context = {
        'context_countries': countries,
        'context_categories': categories,
    }

    return context
