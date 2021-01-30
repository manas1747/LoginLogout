from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import City


@receiver(pre_save, sender=City)
def do_something_before_save(sender, instance, **kwargs):
    print("=====pre_save START=======")
    print("Sender : {0}".format(sender))
    print("Instance : {0}".format(instance))
    print("Rest of args:\n" + str(kwargs))
    print("At this point I can do anything.")
    print("=====pre_save END=========")


@receiver(post_save, sender=City)
def do_something_after_save(sender, instance, created, **kwargs):
    print("=====post_save START=======")
    print("Sender : {0}".format(sender))
    print("Instance : {0}".format(instance))
    print("Created : {0}".format(created))
    print("Rest of args:\n" + str(kwargs))
    print("At this point I can do anything.")
    print("=====post_save END=========")
