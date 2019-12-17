import uuid

from django.db import models

DEFAULT_CATEGORY_ID = 1


class Category(models.Model):

    name = models.TextField()


class Post(models.Model):

    PUBLISHED = 'published'

    REVIEW = 'review'

    STATUSES = [
        (REVIEW, 'review'),
        (PUBLISHED, 'published')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField()
    status = models.TextField(choices=STATUSES, default=REVIEW)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=DEFAULT_CATEGORY_ID)

    def __str__(self):
        return f"{self.text}"
