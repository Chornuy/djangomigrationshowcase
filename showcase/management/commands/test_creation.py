from django.core.management import BaseCommand

from showcase.models import Post, Category


class Command(BaseCommand):

    def handle(self, *args, **options):

        Category.objects.bulk_create([
            Category(name="Funny cats"),
            Category(name="Very funny cats"),
            Category(name="More very funny cats")
        ])
