from django.shortcuts import render
from .forms import PostCreationForm

# Create your views here.
def index(request):
    form = PostCreationForm()
    return render(request, "post/post.html",
                  {"form": form})
