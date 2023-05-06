from django.shortcuts import render, redirect
from library.models import book

# def showHomepage(request):
#     return render(request, './index.html')

def showHomepage(request):
    books = book.objects.all()
    return render(request, './index.html', {'books': books})

def addBook(request):
    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        publisher = request.POST['publisher']
        publication_date = request.POST['publication_date']
        isbn = request.POST['isbn']
        category = request.POST['category']

        b = book(title = title, author=author, publisher=publisher, publication_date=publication_date, isbn=isbn, category=category)
        b.save()

        return redirect('/')

    return render(request, './addbook.html')

def deleteBook(request, id):
    book.objects.get(id=id).delete()
    return redirect('/')
