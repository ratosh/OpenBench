from django.contrib.auth.management.commands import createsuperuser
from django.contrib.auth.models import User
import os


class Command(createsuperuser.Command):
    help = 'Set a existing user as superuser'

    def handle(self, *args, **options):
        database = options.get('database')
        username = os.environ.get("SU_NAME", "superuser")
        exists = self.UserModel._default_manager.db_manager(database).filter(username=username).exists()
        if not exists:
            print('Can only set existing users as admin.')
            return

        user = self.UserModel._default_manager.db_manager(database).get(username=username)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
