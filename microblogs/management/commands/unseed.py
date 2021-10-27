from django.core.management.base import BaseCommand, CommandError
from microblogs.models import User

class Command(BaseCommand):
    def __init__(self):
        super().__init__()

    def handle(self, *args, **options):
        User.objects.exclude(username="@admin").delete()
