import random
import string
from datetime import date, timedelta
from faker import Faker
from django.core.management.base import BaseCommand
from base.models import Patient

class Command(BaseCommand):
    help = 'Generate 50 fake patients'

    def handle(self, *args, **kwargs):
        faker = Faker()
        genders = ['male', 'female', 'other']
        marital_statuses = ['single', 'married', 'divorced', 'widowed']
        nationalities = ['Rwandan', 'other']

        for _ in range(50):
            name = faker.name()
            dob = faker.date_of_birth(minimum_age=0, maximum_age=100)
            gender = random.choice(genders)
            marital_status = random.choice(marital_statuses)
            nationality = random.choice(nationalities)
            id_number = faker.unique.random_number(digits=10)
            province = faker.state()
            district = faker.city()
            sector = faker.city()
            cell = faker.street_name()
            village = faker.street_name()
            phone_number = faker.unique.phone_number()
            relative_name = faker.name()
            relative_id_number = faker.random_number(digits=10)
            relationship = faker.word()
            relative_province = faker.state()
            relative_district = faker.city()
            relative_sector = faker.city()
            relative_cell = faker.street_name()
            relative_village = faker.street_name()
            relative_phone_number = faker.phone_number()

            patient = Patient(
                name=name,
                dob=dob,
                gender=gender,
                marital_status=marital_status,
                nationality=nationality,
                id_number=id_number,
                province=province,
                district=district,
                sector=sector,
                cell=cell,
                village=village,
                phone_number=phone_number,
                relative_name=relative_name,
                relative_id_number=relative_id_number,
                relationship=relationship,
                relative_province=relative_province,
                relative_district=relative_district,
                relative_sector=relative_sector,
                relative_cell=relative_cell,
                relative_village=relative_village,
                relative_phone_number=relative_phone_number,
            )

            patient.save()

        self.stdout.write(self.style.SUCCESS('Successfully created 50 fake patients'))
