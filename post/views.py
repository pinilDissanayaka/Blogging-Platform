from django.shortcuts import render
from .forms import PostCreationForm

# Create your views here.
def index(response):
    
    if response.method == "POST":
        form = PostCreationForm(response.POST)
        if form.is_valid():
            pass
    else:
        form = PostCreationForm()
        return render(response, "post/post.html",
                    {"form": form})
