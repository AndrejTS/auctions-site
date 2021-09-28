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

        for listing in products:
            end_time = timezone.now() + datetime.timedelta(
                minutes=random.randint(5, 30))
            listing = Listing(title=listing['title'], starting_price=listing['price'], current_price=listing['price'],
                              description=listing['description'], image_url=listing['image'], category=listing['category'], owner=random.choice(users), end_time=end_time)
            listing.save()

        # Remove 20 oldest closed listings
        old_products = Listing.objects.filter(
            closed=True).order_by('date_added').all()[:20]

        for listing in old_products:
            listing.delete()
