from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from microblogs.models import User


class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.faker = Faker('en_GB')

    def handle(self, *args, **options):
        fake = Faker()
        for i in range (100):
            fake_first_name = fake.first_name()
            fake_last_name = fake.last_name()
            fake_username = "@" + fake_first_name.lower() + fake_last_name.lower()
            fake_email=fake_username[1:] + "@example.com"
            fake_bio = fake.paragraph(nb_sentences=1)
            User.objects.create(username=fake_username, first_name=fake_first_name, last_name=fake_last_name, email=fake_email, bio=fake_bio)


#Task is to complete this seed command and add an unseed Command
#The seed command should generate 100 random users, making user of the faker packeage
#The unseed commmand should remove all the regular users, taking care not to remove super users or staff account
