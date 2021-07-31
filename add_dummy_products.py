import json
import random

from auctions.models import Listing
from auctions.models import User


def add_dummy_data():
    with open('fake_products.json') as f:
        products = json.load(f)

    random.shuffle(products)

    andrej = User.objects.get(username='andrej')
    philip = User.objects.get(username='phiLip')
    mary = User.objects.get(username='mary')
    john = User.objects.get(username='john')

    users = [andrej, philip, mary, john]

    categories = ['Auto', 'Fashion', 'Electronics',
                  'Home', 'Books', 'Sport', 'Other']

    # random.choice(categories)
    # 'Auto'

    for listing in products:
        listing = Listing(title=listing['title'], starting_price=listing['price'], current_price=listing['price'],
                          description=listing['description'], image_url=listing['image'], category=listing['category'], owner=random.choice(users))
        listing.save()
