from django.core.management.base import BaseCommand, CommandError
from elements.functions import populate_db


class Command(BaseCommand):
    help = 'Will generate the periodic table'


    def handle(self, *args, **options):
        return populate_db()
