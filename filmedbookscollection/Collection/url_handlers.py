from django.shortcuts import redirect


def index_handler(request):
    return redirect("film_index")
