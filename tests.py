import pytest
from main import BooksCollector

class TestBooksCollector:

    @pytest.mark.parametrize('book_name', ['Война и Мир', 'Шерлок Хомс', '  ', '1984/451'])
    def test_add_new_book(self, book_name):
        bc = BooksCollector()
        bc.add_new_book(book_name)
        assert book_name in bc.get_books_genre()
        assert bc.get_book_genre(book_name) == ''

    @pytest.mark.parametrize('book_name', ['Вий', 'Побег из Шоушенка'])
    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Комедии'])
    def test_set_book_genre(self, book_name, genre):
        bc = BooksCollector()
        bc.add_new_book(book_name)
        bc.set_book_genre(book_name, genre)
        assert bc.get_book_genre(book_name) == genre

    @pytest.mark.parametrize('book_name,genre', [('Book1', 'Фантастика'), ('Book2', 'Комедии')])
    def test_get_book_genre(self, book_name, genre):
        bc = BooksCollector()
        bc.add_new_book(book_name)
        bc.set_book_genre(book_name, genre)
        assert bc.get_book_genre(book_name) == genre

    def test_get_books_with_specific_genre(self):
        bc = BooksCollector()
        bc.add_new_book('Book1')
        bc.add_new_book('Book2')
        bc.add_new_book('Book3')
        bc.set_book_genre('Book1', 'Фантастика')
        bc.set_book_genre('Book2', 'Ужасы')
        assert bc.get_books_with_specific_genre('Фантастика') == ['Book1']
        assert bc.get_books_with_specific_genre('Ужасы') == ['Book2']

    def test_get_books_genre(self):
        bc = BooksCollector()
        bc.add_new_book('Book1')
        bc.add_new_book('Book2')
        expected = {'Book1': '', 'Book2': ''}
        assert bc.get_books_genre() == expected

    def test_get_books_for_children(self):
        bc = BooksCollector()
        bc.add_new_book('Book1')
        bc.add_new_book('Book2')
        bc.add_new_book('Book3')
        bc.set_book_genre('Book1', 'Комедии')
        bc.set_book_genre('Book2', 'Ужасы')
        bc.set_book_genre('Book3', 'Мультфильмы')
        assert bc.get_books_for_children() == ['Book1', 'Book3']

    def test_add_book_in_favorites(self):
        bc = BooksCollector()
        bc.add_new_book('Book1')
        bc.add_book_in_favorites('Book1')
        assert 'Book1' in bc.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        bc = BooksCollector()
        bc.add_new_book('Book1')
        bc.add_book_in_favorites('Book1')
        bc.delete_book_from_favorites('Book1')
        assert 'Book1' not in bc.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self):
        bc = BooksCollector()
        bc.add_new_book('Book1')
        bc.add_new_book('Book2')
        bc.add_book_in_favorites('Book1')
        bc.add_book_in_favorites('Book2')
        assert bc.get_list_of_favorites_books() == ['Book1', 'Book2']
