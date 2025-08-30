import pytest
from main import BooksCollector


class TestBooksCollector:


    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Приключение Буратино')
        assert collector.get_book_genre('Приключение Буратино') == ''


    @pytest.mark.parametrize("name, expected_count", [
        ('Приключение Буратино', 1),
        ('', 0),
        ('Приключение Буратино' * 40, 0)
    ])
    def test_add_new_book_incorrect(self, name, expected_count):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == expected_count


    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Приключение Буратино')
        collector.set_book_genre('Приключение Буратино', 'Ужасы')
        assert collector.books_genre['Приключение Буратино'] == 'Ужасы'


    def test_set_book_genre_incorrect_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Приключение Буратино')
        collector.set_book_genre('Приключение Буратино', 'Утопия')
        assert collector.books_genre['Приключение Буратино'] == ''


    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Приключение Буратино')
        collector.set_book_genre('Приключение Буратино', 'Ужасы')
        assert collector.get_book_genre('Приключение Буратино') == 'Ужасы'


    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        books = ['Приключение Буратино', 'Roar']
        for book in books:
            collector.add_new_book(book)
            collector.set_book_genre(book, 'Ужасы')


    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Детская')
        collector.add_new_book('Взрослая')
        collector.set_book_genre('Детская', 'Фантастика')
        collector.set_book_genre('Взрослая', 'Ужасы')

        assert collector.get_books_for_children() == ['Детская']


    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Приключение Буратино')
        collector.add_book_in_favorites('Приключение Буратино')
        assert collector.get_list_of_favorites_books() == ['Приключение Буратино']


    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Приключение Буратино')
        collector.add_book_in_favorites('Приключение Буратино')
        collector.delete_book_from_favorites('Приключение Буратино')
        assert collector.get_list_of_favorites_books() == []


    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Приключение Буратино')
        assert collector.get_books_genre() == {'Приключение Буратино': ''}