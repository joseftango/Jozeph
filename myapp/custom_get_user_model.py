from django.apps import apps
from django.conf import settings

def get_user_model2():
    """ Returns the specified second user model """
    try:
        # Get the second user model defined in your custom configuration
        app_label, model_name = settings.SECOND_USER_MODEL.split('.')
        return apps.get_model(app_label, model_name)
    except ValueError:
        raise ValueError("Invalid second user model specified.")
