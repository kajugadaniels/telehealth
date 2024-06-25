import random
import string
from datetime import date, timedelta
from faker import Faker
from django.core.management.base import BaseCommand
from base.models import Patient

class Command(BaseCommand):
    help = 'Generate 100 fake patients'

    def handle(self, *args, **kwargs):
        faker = Faker()
        genders = ['Male', 'Female']
        marital_statuses = ['Single', 'Married', 'Widowed', 'Divorced']
        nationalities = ['Rwandan', 'Other']
        relationships = ['Husband', 'Wife', 'Sibling', 'Friend', 'Other Family Member']

        def generate_unique_mrn():
            while True:
                mrn = 'MRN-' + ''.join(random.choices(string.digits, k=7))
                if not Patient.objects.filter(mrn=mrn).exists():
                    return mrn

        for _ in range(100):
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

            # Generate unique MRN
            mrn = generate_unique_mrn()

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
                mrn=mrn,
            )

            patient.save()

        # Assign relationships to 25% of the patients
        all_patients = list(Patient.objects.all())
        for patient in all_patients:
            if random.random() < 0.25:
                relative = random.choice(all_patients)
                while relative == patient:
                    relative = random.choice(all_patients)
                patient.relative = relative
                patient.relationship = random.choice(relationships)
                patient.save()

        self.stdout.write(self.style.SUCCESS('Successfully created 100 fake patients'))
