from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Review
from .forms import ReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from books.models import Book

# Create your views here.


def index(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/index.template.html', {
        'reviews': reviews
    })

@login_required
def create_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = book
            review.save()
            messages.success(request, "New Review added!")
            return redirect(index)

    else:
        form = ReviewForm()
        return render(request, 'reviews/create_review.template.html', {
            'form': form,
            'book': book
        })
        