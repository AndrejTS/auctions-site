from django.dispatch import receiver
from django.db.models.signals import post_save
from auctions.models import Listing

from django_q.tasks import schedule


@receiver(post_save, sender=Listing)
def schedule_close_listing(sender, instance, created, **kwargs):
    if created:
        schedule('auctions.tasks.close_listing', instance.id,
                 next_run=instance.end_time, q_options={'group': 'Close listing'})
