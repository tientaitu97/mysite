import random
from faker import Faker
from blog.models import Post
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.management.base import BaseCommand

faker = Faker()


class Command(BaseCommand):
    help = 'Closes the specified post for voting'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        count = options['count']
        list_user = User.objects.all()
        for _ in range(0, count):
            title = faker.name()
            Post.published.create(title=title + "Post!!!",
                                author=random.choice(list_user),
                                slug="-".join(title.lower().split()),
                                body=faker.text(),
                                status=random.choice(['published', 'draft']),
                                created=timezone.now(),
                                updated=timezone.now(),
                                )
