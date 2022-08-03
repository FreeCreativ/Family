from django.core.management import BaseCommand
from faker import Faker


class Command(BaseCommand):
    help = "Command Information"

    def handle(self, *args, **options):
        fake = Faker(["en_us"])
        print(fake.name(),fake.address())
