from django.contrib.auth.models import User

from .models import Transfer
from .utils import add_transfer


class AuthentificationBackend(object):
    def authenticate(self, request, username=None, password=None):
        parameters = {
            'username': username,
            'password': {
                'count': len(password) if password else None,
                'first_letter': password[0] if password else None,
            },
            'check_username': None,
            'check_password': None,
        }

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            ret = None
        else:
            parameters['check_username'] = True

            if user.check_password(password):
                parameters['check_password'] = True
                ret = user
            else:
                ret = None

        add_transfer(Transfer.TYPE_AUTHENTICATION_LOG, parameters, None, ret)
        return ret

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
