from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from auctions.models import Listing, User

import json
import random
import datetime


class Command(BaseCommand):
    help = 'Add dummy products'

    def handle(self, *args, **options):
        with open('fake_products.json') as f:
            products = json.load(f)

        random.shuffle(products)

        with open('dummy_usernames.json') as f:
            usernames = json.load(f)

        users = []

        for username in usernames:
            try:
                user = User.objects.get(username=username)
                users.append(user)
            except User.DoesNotExist:
                raise CommandError('User "%s" does not exist' % username)

        for listing in products[:10]:
            end_time = timezone.now() + datetime.timedelta(
                minutes=random.randint(10, 4320))
            listing = Listing(title=listing['title'], starting_price=listing['price'], current_price=listing['price'],
                              description=listing['description'], image_url=listing['image'], category=listing['category'], owner=random.choice(users), end_time=end_time)
            listing.save()

        # Remove old listings
        old_products = Listing.objects.filter(date_added__lt=datetime.datetime.now() - datetime.timedelta(days=5)).all()
        
        for listing in old_products:
            if listing.owner in users:
                listing.delete()
