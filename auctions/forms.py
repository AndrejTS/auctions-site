from django.forms import ModelForm
from django import forms
from .models import Listing, Bid, Comment


class ListingForm(ModelForm):
    CHOICES = (
        ('Auto', 'Auto'),
        ('Fashion', 'Fashion'),
        ('Electronics', 'Electronics'),
        ('Home', 'Home'),
        ('Books', 'Books'),
        ('Sport', 'Sport'),
        ('Other', 'Other'),
    )
    category = forms.ChoiceField(choices=CHOICES)
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Listing
        fields = ['title', 'description',
                  'starting_price', 'image_url', 'category']


class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']
        labels = {
            'amount': 'How much do you want to give for the product?'
        }


# class CommentForm(ModelForm):
#     class Meta:
#         comment = Comment
#         fields = ['content']
