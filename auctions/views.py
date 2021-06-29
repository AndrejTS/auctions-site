from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing, Bid, Comment
from .forms import ListingForm, BidForm


def index(request):
    bids = Bid.objects.all()
    return render(request, "auctions/listings.html", {
        'title': 'Active Listings',
        'listings': Listing.objects.filter(closed=False).all()
    })


@login_required(login_url='/login/')
def create_listing(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            new_listing = form.save()
            new_listing.owner = request.user
            new_listing.current_price = new_listing.starting_price
            new_listing.save()
            return HttpResponseRedirect(reverse("listing", kwargs={'id': new_listing.id}))
    else:
        form = ListingForm()
        return render(request, "auctions/create_listing.html", {
            'form': form
        })


def listing(request, id):
    if request.GET.get('error'):
        message = 'The bid is too low'
    else:
        message = None
    listing = Listing.objects.get(pk=id)
    bids = Bid.objects.filter(listing=listing).all()
    comments = Comment.objects.filter(listing=listing).all()
    is_watched = False
    if request.user.is_authenticated:
        if listing in request.user.watchlist.all():
            is_watched = True
    return render(request, "auctions/listing.html", {
        'listing': listing,
        'bids': bids,
        'comments': comments,
        'bid_form': BidForm(),
        'watched': is_watched,
        'message': message
    })


@login_required(login_url='/login/')
def bid(request):
    pk = request.POST['id']
    if request.method == "POST":
        bid_value = request.POST['amount']
        listing = Listing.objects.get(pk=pk)
        if listing.closed:
            return HttpResponse('Listing is no active')
        bid_is_too_low = False
        if listing.last_bid is None:
            if int(bid_value) < listing.starting_price:
                bid_is_too_low = True
        elif int(bid_value) <= listing.last_bid:
            bid_is_too_low = True
        if bid_is_too_low:
            return HttpResponseRedirect(
                reverse("listing", kwargs={'id': pk}) + '?error=true')
        else:
            form = BidForm(request.POST)
            if form.is_valid():
                new_bid = form.save()
                new_bid.listing = listing
                new_bid.user = request.user
                new_bid.save()
                listing.last_bid = bid_value
                listing.current_price = bid_value
                listing.save()
            return HttpResponseRedirect(reverse("listing", kwargs={'id': pk}))
    else:
        return HttpResponseRedirect(
            reverse("listing", kwargs={'id': pk}))


@login_required(login_url='/login/')
def comment(request):
    if request.method == "POST":
        content = request.POST['content']
        pk = request.POST['listing_id']
        listing = Listing.objects.get(pk=pk)
        new_comment = Comment(
            content=content, listing=listing, user=request.user)
        new_comment.save()
        return HttpResponseRedirect(reverse("listing", kwargs={'id': pk}))


@login_required(login_url='/login/')
def close_listing(request):
    if request.method == "POST":
        pk = request.POST['id']
        listing = Listing.objects.get(pk=pk)
        bids = Bid.objects.filter(listing=listing).all()
        if listing.owner == request.user:
            listing.closed = True
            if bids:
                listing.winner = bids.last().user
            listing.save()
        return HttpResponseRedirect(reverse("listing", kwargs={'id': pk}))


@login_required(login_url='/login/')
def watchlist(request):
    if request.method == "POST":
        command = request.POST['watchlist_command']
        listing_id = request.POST['listing_id']
        listing = Listing.objects.get(pk=listing_id)
        if command == 'add':
            listing.watchlist_users.add(request.user)
        elif command == 'remove':
            listing.watchlist_users.remove(request.user)
        return HttpResponseRedirect(reverse("listing", kwargs={'id': listing_id}))
    else:
        listings = request.user.watchlist.all()
        return render(request, "auctions/listings.html", {
            'title': 'Watchlist',
            'listings': listings
        })


def categories(request):
    return render(request, "auctions/categories.html", {
        'categories': [
            'Auto',
            'Fashion',
            'Electronics',
            'Home',
            'Books',
            'Sport',
            'Other'
        ]
    })


def category(request, category_name):
    listings = Listing.objects.filter(category=category_name).all()
    return render(request, "auctions/listings.html", {
        'title': category_name,
        'listings': listings
    })


@login_required(login_url='/login/')
def profile(request):
    return render(request, "auctions/profile.html", {
        'username': request.user,
    })


@login_required(login_url='/login/')
def user_listings(request):
    listings = request.user.listings.all()
    return render(request, "auctions/listings.html", {
        'title': 'Your listings',
        'listings': listings
    })


@login_required(login_url='/login/')
def user_wins(request):
    listings = request.user.wins.all()
    return render(request, "auctions/listings.html", {
        'title': 'Auctions you won',
        'listings': listings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
