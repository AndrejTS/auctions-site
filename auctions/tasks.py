from django.core.exceptions import ObjectDoesNotExist
from django.core.management import call_command

from auctions.models import Listing, Bid


def close_listing(id):
    try:
        listing = Listing.objects.get(id=id)
        listing.closed = True
        if listing.bids.all():
            listing.winner = listing.bids.latest('amount').user
        listing.save()
    except ObjectDoesNotExist:
        pass


def add_dummy_products():
    call_command('add_dummy_products')
