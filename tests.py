from main import BooksCollector
import pytest
class TestBooksCollector:
    @pytest.mark.parametrize("name", ['Несуществующая'])
    def test_add_new_book_lenlimit40(self, name):
        collector_ut1 = BooksCollector()
        collector_ut1.add_new_book(name)
        assert collector_ut1.books_genre == {'Несуществующая': ''} and name in collector_ut1.books_genre.keys() and len(name) < 41

    @pytest.mark.parametrize("name,genre", [("В пасти безумия", "Ужасы")])
    def test_set_book_genre_exist_in_books_genre(self, name, genre):
        collector_ut2 = BooksCollector()
        collector_ut2.books_genre = {"В пасти безумия": "Ужасы"}
        collector_ut2.set_book_genre(name, genre)
        assert collector_ut2.books_genre.get(name) == "Ужасы"

    @pytest.mark.parametrize("name", ['бук'])
    def test_get_book_genre_true_genre(self, name):
        collector_ut3 = BooksCollector()
        collector_ut3.books_genre = {'бук': 'Жанр'}
        assert collector_ut3.get_book_genre(name) == 'Жанр'

    @pytest.mark.parametrize("genre", ['Ужасы'])
    def test_get_books_with_specific_genre_true_specific(self, genre):
        collector_ut4 = BooksCollector()
        collector_ut4.books_genre['В пасти безумия'] = 'Ужасы'
        collector_ut4.books_genre['Мимино'] = 'Комедии'
        assert collector_ut4.get_books_with_specific_genre(genre) == ['В пасти безумия']


    def test_get_books_genre_true_dict (self):
        collector_ut5 = BooksCollector()
        collector_ut5.books_genre['В пасти безумия'] = 'Ужасы'
        assert collector_ut5.get_books_genre() == {'В пасти безумия': 'Ужасы'}

    def test_get_books_for_children_notadult(self):
        collector_ut6 = BooksCollector()
        collector_ut6.books_genre['В пасти безумия'] = 'Ужасы'
        collector_ut6.books_genre['Мимино'] = 'Комедии'
        assert collector_ut6.get_books_for_children() == ['Мимино']

    @pytest.mark.parametrize("name", ['Мимино', 'В пасти безумия'])
    def test_add_book_in_favorites_not_exist_books_genre(self, name):
        collector_ut7 = BooksCollector()
        collector_ut7.books_genre['В пасти безумия'] = 'Ужасы'
        collector_ut7.books_genre['Мимино'] = 'Комедии'
        collector_ut7.add_book_in_favorites(name)
        assert name in collector_ut7.books_genre.keys()

    @pytest.mark.parametrize("name", ['Мимино', 'В пасти безумия'])
    def test_delete_book_from_favorites_exist_in_genre(self, name):
        collector_ut8 = BooksCollector()
        collector_ut8.books_genre['В пасти безумия'] = 'Ужасы'
        collector_ut8.books_genre['Мимино'] = 'Комедии'
        collector_ut8.add_book_in_favorites(name)
        assert name in collector_ut8.favorites
        collector_ut8.delete_book_from_favorites(name)
        assert name not in collector_ut8.favorites


    def test_get_list_of_favorites_books_true_dict (self):
        collector_ut9 = BooksCollector()
        collector_ut9.books_genre['В пасти безумия'] = 'Ужасы'
        collector_ut9.add_book_in_favorites('В пасти безумия')
        assert collector_ut9.get_list_of_favorites_books() == ['В пасти безумия']
