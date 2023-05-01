from basket.models import Basket


def baskets(request):
    user = request.user
    content = Basket.objects.filter(user=user) if user.is_authenticated else []
    return {'baskets': content}
