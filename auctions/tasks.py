from django.core.exceptions import ObjectDoesNotExist

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
