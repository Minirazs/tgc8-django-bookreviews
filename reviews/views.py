from django.shortcuts import render, HttpResponse, redirect
from .models import Review
from .forms import ReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/index.template.html', {
        'reviews': reviews
    })

@login_required
def create_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, "New Review added!")
            return redirect(index)

    else:
        form = ReviewForm()
        return render(request, 'reviews/create_review.template.html', {
            'form': form
        })
        