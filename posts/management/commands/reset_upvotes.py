from django.core.management import BaseCommand

from posts.models import Post


class Command(BaseCommand):
    help = "Reset upvotes of post"

    def handle(self, *args, **kwargs):
        posts = Post.objects.all()
        posts.update(upvotes=0)

        for item in posts:
            item.save()
