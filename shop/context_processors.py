from products.models import Categories

def categories(request):
    return {
        "menu_categories": Categories.objects.filter(is_active_menu = True).order_by("name")
    }