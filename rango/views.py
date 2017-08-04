from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.


def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context_dict)
    # return HttpResponse("Rango says, Hey there partner!"
    #                     + "<br/> <a href='" + reverse("about") + "'>About</a>"
    #                     )


def about(request):
    context_dict = {'boldmessage': "Rango says, this is about page!",
                    'indexURL': reverse("index"),
                    }
    return render(request, 'rango/about.html', context_dict)