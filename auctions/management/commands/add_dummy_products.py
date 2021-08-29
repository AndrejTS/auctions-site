from django.core.management.base import BaseCommand, CommandError
from auctions.models import Listing
from auctions.models import User

import json
import random
import time


class Command(BaseCommand):
    help = 'Add dummy products'

    def handle(self, *args, **options):
        with open('fake_products.json') as f:
            products = json.load(f)

        random.shuffle(products)

        usernames = ['andrej', 'phiLip', 'mary', 'john']
        users = []

        for username in usernames:
            try:
                user = User.objects.get(username=username)
                users.append(user)
            except User.DoesNotExist:
                raise CommandError('User "%s" does not exist' % username)

        categories = ['Auto', 'Fashion', 'Electronics',
                      'Home', 'Books', 'Sport', 'Other']

        for listing in products:
            time.sleep(random.randint(5, 10))
            listing = Listing(title=listing['title'], starting_price=listing['price'], current_price=listing['price'],
                              description=listing['description'], image_url=listing['image'], category=listing['category'], owner=random.choice(users))
            listing.save()

        # Remove 20 oldest products
        old_products = Listing.objects.order_by('date_added').all()[:20]

        for listing in old_products:
            listing.delete()
