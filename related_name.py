from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    publisher = models.ForeignKey(
        Publisher, on_delete=models.CASCADE, related_name="books"
    )

    def __str__(self):
        return self.title


"""Использование prefetch_related
В этом примере мы хотим получить всех авторов вместе с книгами, которые они написали, и издателями, которые опубликовали эти книги. Использование prefetch_related позволяет нам предварительно загрузить связанные данные, минимизируя количество запросов к базе данных.

"""
from django.db.models import Prefetch

# from .models import Author, Book, Publisher

# Предварительная загрузка всех авторов, книг и издателей книг
authors = Author.objects.prefetch_related(
    Prefetch(
        "books",
        queryset=Book.objects.select_related("publisher"),  # Загрузка издателей книг
    )
)

# Обработка данных
for author in authors:
    print(f"Author: {author.name}")
    for book in author.books.all():
        print(f"  Book: {book.title}")
        print(f"    Publisher: {book.publisher.name}")

"""
Объяснение кода
Запрос Author.objects.prefetch_related(...):

prefetch_related используется для оптимизации доступа к связанным объектам.
Prefetch позволяет нам настроить дополнительные параметры для связанных объектов, такие как фильтрация или выборка других связанных объектов.
Prefetch('books', queryset=Book.objects.select_related('publisher')):

Здесь мы предварительно загружаем книги (books) и используем select_related внутри Prefetch для дальнейшего предварительного выбора издателей (publisher) для каждой книги. select_related используется для загрузки связанных данных в одном запросе, что оптимизирует доступ к этим данным.
Проход по автору и книгам:

Мы проходим по всем authors и для каждого author получаем список books, которые уже загружены вместе с издателями."""
# Мы проходим по всем authors и для каждого author получаем список books, которые уже загружены вместе с издателями.
