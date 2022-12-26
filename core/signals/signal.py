from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
# these are predefined signals
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, pre_save, pre_delete, \
    post_init, post_save, post_delete, pre_migrate, post_migrate
from django.core.signals import request_started, request_finished, got_request_exception
from django.db.backends.signals import connection_created


@receiver(user_logged_in, sender=User)  # we can also use decorator instead of registering externally
def login_success(sender, request, user, **kwargs):  # this is receiver function which will receive the signal
    print("*******************************")
    print("Logged-in Signal ---- Run intro")
    print("Sender: ", sender)
    print("Request : ", request)
    print("User : ", user)
    print(f"Kwargs: {kwargs}")


# user_logged_in.connect(login_success, sender=User)   # this should be out of function # connecting signal with receiver method
# we are passing receiver function to the signal so it will be connected


@receiver(user_logged_out, sender=User)  # we can also use decorator instead of registering externally
def logged_out(sender, request, user, **kwargs):  # this is receiver function which will receive the signal
    print("*******************************")
    print("Logged-Out Signal ---- Run Bye bye")
    print("Sender: ", sender)
    print("Request : ", request)
    print("User : ", user)
    print(f"Kwargs: {kwargs}")


# user_logged_out.connect(logged_out, sender=User)   # we can connect either by decorator or by this


@receiver(user_login_failed)  # we can also use decorator instead of registering externally
def login_failed(sender, request, credentials, **kwargs):  # this is receiver function which will receive the signal
    print("*******************************")
    print("Login-failed-Signal ---- Run ")
    print("Sender: ", sender)
    print("Request : ", request)
    print("Credentials : ", credentials)
    print(f"Kwargs: {kwargs}")


# user_login_failed.connect(login_failed, sender=User)   # we can connect either by decorator or by this


""" ***************************** model signals ***************************************************"""


@receiver(pre_save, sender=User)  # this will run before save method and in sender we can use  another model name also
def at_beginning_save(sender, instance, **kwargs):
    print("*******************************")
    print("Pre-Save-Signal ---- Run ")
    print("Sender: ", sender)
    print("Instance : ", instance)
    print(f"Kwargs: {kwargs}")


# pre_save.connect(at_beginning_save, sender=User)


@receiver(post_save, sender=User)
def at_beginning_save(sender, instance, created, **kwargs):
    if created:  # If new record is created
        print("*******************************")
        print("Post-Save-Signal ---- New Record ")
        print("Sender: ", sender)
        print("Instance : ", instance)
        print("Created : ", created)
        print(f"Kwargs: {kwargs}")
    else:  # if we are updating the existing record then this will run
        print("Post-Save-Signal ---- Updare record Record ")
        print("Sender: ", sender)
        print("Instance : ", instance)
        print("Created : ", created)
        print(f"Kwargs: {kwargs}")


# pre_save.connect(at_beginning_save, sender=User)


@receiver(pre_delete, sender=User)
def at_beginning_delete(sender, instance, **kwargs):
    print("*******************************")
    print("Pre-Delete-Signal ---- Run ")
    print("Sender: ", sender)
    print("Instance : ", instance)
    print(f"Kwargs: {kwargs}")


# pre_delete(at_beginning_delete, sender=User)


@receiver(post_delete, sender=User)
def at_ending_delete(sender, instance, **kwargs):
    print("*******************************")
    print("Post-Delete-Signal ---- Run ")
    print("Sender: ", sender)
    print("Instance : ", instance)
    print(f"Kwargs: {kwargs}")


# post_delete(at_ending_delete, sender=User)


@receiver(pre_init, sender=User)  # this will run when django model will be instantiated at beginning
def at_beginning_init(sender, *args, **kwargs):
    print("*******************************")
    print("Pre-Init-Signal ---- Run ")
    print("Sender: ", sender)
    print("Args : {args}")
    print(f"Kwargs: {kwargs}")


# pre_init(at_beginning_init, sender=User)


@receiver(post_init, sender=User)  # this will run when django model will be instantiated at ending
def at_beginning_init(sender, *args, **kwargs):
    print("*******************************")
    print("Post-Init-Signal ---- Run ")
    print("Sender: ", sender)
    print("Args : {args}")
    print(f"Kwargs: {kwargs}")


# post_init(at_ending_init, sender=User)


""" ************************************* Request/Response signals *************************************"""


@receiver(request_started)  # this will run at starting of the request
def at_beginning_request(sender, environ, **kwargs):
    print("*******************************")
    print("At-beginning-request-Signal ---- Run ")
    print("Sender: ", sender)
    print("environ:", environ)
    print(f"Kwargs: {kwargs}")


# request_started(at_beginning_request, sender=User)


@receiver(request_finished)  # this will run at ending of the request
def at_ending_request(sender, **kwargs):
    print("*******************************")
    print("At-beginning-request-Signal ---- Run ")
    print("Sender: ", sender)
    print(f"Kwargs: {kwargs}")


# request_finished(at_ending_request, sender=User)


@receiver(got_request_exception)  # this will run if exception occurs in some views then this will run
def at_request_exception(sender, request, **kwargs):
    print("*******************************")
    print("At-Exception-request-Signal ---- Run ")
    print("Sender: ", sender)
    print("Request: ", request)
    print(f"Kwargs: {kwargs}")


# got_request_exception(at_request_exception, sender=User)


""" ******************************** Management signals *****************************************"""
"""       signals sent by django admin         / pre_migrate / post_migrate                      """


@receiver(pre_migrate)  # this will run when we do migrate command
def before_install_app(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print("******************************************************")
    print("before install app")  # this function will be running for each and every table or model in database
    print("Sender: ", sender)
    print("App_config: ", app_config)
    print("verbosity: ", verbosity)
    print("interactive: ", interactive)
    print('Using', using)
    print('Plan', plan)
    print('Apps', apps)
    print(f"Kwargs: {kwargs}")


@receiver(post_migrate)
def at_end_migrate_flush(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print("******************************************************")
    print("before install app")
    print("Sender: ", sender)
    print("App_config: ", app_config)
    print("verbosity: ", verbosity)
    print("interactive: ", interactive)
    print('Using', using)
    print('Plan', plan)
    print('Apps', apps)
    print(f"Kwargs: {kwargs}")


""" ************************************ Database wrappers ***************************"""


@receiver(connection_created)
def conn_db(sender, connection, **kwargs):  # this will run when initial connection is stablished with database
    print("******************************************************")
    print("before install app")
    print("Sender: ", sender)
    print("Connection: ", connection)
    print(f"Kwargs: {kwargs}")