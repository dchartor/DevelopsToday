from django.core.management import call_command

from celery import shared_task


@shared_task
def reset_upvote_count():
    call_command("reset_upvotes")
