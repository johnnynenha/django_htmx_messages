import random
from django.http import HttpResponse
from django.contrib import messages

SAMPLE_MESSAGES = [
    (messages.DEBUG, "Hello World!"),
    (messages.INFO, "System operational"),
    (messages.SUCCESS, "Congratulations! You did it."),
    (messages.WARNING, "Hum... not sure about that."),
    (messages.ERROR, "Oops! Something went wrong"),
]


def htmx_message(request):
    messages.add_message(request, *random.choice(SAMPLE_MESSAGES))
    return HttpResponse("")