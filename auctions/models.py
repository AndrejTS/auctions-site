from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Listing(models.Model):
    winner = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name='wins', blank=True)
    closed = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=800, blank=True)
    starting_price = models.PositiveIntegerField()
    last_bid = models.PositiveIntegerField(null=True, blank=True)
    current_price = models.PositiveIntegerField(null=True, blank=True)
    image_url = models.URLField(blank=True)
    category = models.CharField(max_length=30, blank=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name='listings')
    watchlist_users = models.ManyToManyField(
        User, related_name='watchlist', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Bid(models.Model):
    amount = models.PositiveIntegerField()
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name='bids')
    date_added = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    content = models.CharField(max_length=250, default='')
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name='comments')
    date_added = models.DateTimeField(auto_now_add=True)
