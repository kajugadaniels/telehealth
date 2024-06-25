from django.core.management.base import BaseCommand
from base.models import Patient  # Replace 'myapp' with the name of your app

class Command(BaseCommand):
    help = 'Delete all patients'

    def handle(self, *args, **kwargs):
        Patient.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all patients'))
