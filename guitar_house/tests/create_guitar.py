from guitar_house.guitar.models import Guitar


def _create_guitar(brand, model, type, price, image_url, description, short_description, user):
    guitar = Guitar.objects.create(
        brand=brand,
        model=model,
        type=type,
        price=price,
        image_url=image_url,
        description=description,
        short_description=short_description,
        user=user
    )
    return guitar