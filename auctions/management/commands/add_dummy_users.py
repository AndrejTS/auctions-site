from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
from auctions.models import User

import json
import random


class Command(BaseCommand):
    help = 'Add dummy users'

    def handle(self, *args, **options):
        with open('dummy_usernames.json') as f:
            usernames = json.load(f)

        for username in usernames:
            email = 'dummyemail@mail.com'
            password = '123'

            try:
                user = User.objects.create_user(username, email, password)
                user.save()
            except IntegrityError:
                raise CommandError('Username: "%s" already taken.' % username)
