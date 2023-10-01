# Задание 2. У вас есть класс BookService, который использует интерфейс BookRepository для получения
# информации о книгах из базы данных. Ваша задача написать unit-тесты для BookService, используя
# Mockito для создания мок-объекта BookRepository.
# Мок-объект класса BookService для Python
from typing import List


class Book:
    def __init__(self, book_id: int, title: str, author: str, genre: str):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre

    def __str__(self):
        return f'id - {self.book_id}, title - {self.title}, author - {self.author}, genre - {self.genre}'


class BookRepository:

    def __init__(self):
        self.repository = []

    def get_books_by_author(self, author: str):
        books = []
        for book in self.repository:
            if book.author.lower() == author.lower():
                books.append(book)
        return books

    def get_books_by_genre(self, genre: str):
        books = []
        for book in self.repository:
            if book.genre.lower() == genre.lower():
                books.append(book)
        return books

    def get_all_books(self) -> list[str]:
        return [str(book) for book in self.repository]

    def add_book(self, book: Book):
        self.repository.append(book)


class BookService:

    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def add_book(self, book: Book):
        self.book_repository.add_book(book)

    def get_books_by_author(self, author: str) -> list[Book]:
        return self.book_repository.get_books_by_author(author)

    def get_books_by_genre(self, genre: str) -> list[Book]:
        return self.book_repository.get_books_by_genre(genre)

    def get_all_books(self) -> list[str]:
        return self.book_repository.get_all_books()
