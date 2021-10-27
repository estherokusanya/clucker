from django.core.management.base import BaseCommand, CommandError
from faker import Faker

class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.faker = Faker('en_GB')

    def handle(self, *args, **options):
        print("WARNING: The SEED command has not been implemented yet.")


#Task is to complete this seed command and add an unseed Command
#The seed command should generate 100 random users, making user of the faker packeage
#The unseed commmand should remove all the regular users, taking care not to remove super users or staff account
