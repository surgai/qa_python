from main import BooksCollector
import pytest
class Test1BooksCollector:
    @pytest.mark.parametrize("name", ['Несуществующая1', 'Несуществующая2'])
    def test_add_new_book_lenlimit40(self, name):
        self.books_genre = {'Мимино': 'Комедии', 'В пасти безумия': 'Ужасы'}
        collector_ut1 = BooksCollector()
        collector_ut1.add_new_book(name)
        assert name not in self.books_genre.keys() and len(name) < 41
class Test2BooksCollector:
    @pytest.mark.parametrize("name", ['В пасти безумия', 'Мимино'])
    @pytest.mark.parametrize("genre", ['Ужасы', 'Комедии'])

    def test_set_book_genre_exist_in_books_genre(self, name, genre):
        collector_ut2 = BooksCollector()
        self.books_genre = {'Мимино': 'Комедии', 'В пасти безумия': 'Ужасы' }
        self.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        collector_ut2.set_book_genre(name, genre)
        assert name in self.books_genre.keys() and genre in self.genre

class Test3BookCollector:
    @pytest.mark.parametrize("name", ['бук'])
    def test_get_books_genre_true_genre(self, name):
        self.books_genre = {'бук': 'Жанр'}
        collector_ut3 = BooksCollector()
        assert collector_ut3.get_books_genre() != 'Жанр'

class Test4BookCollector:
    @pytest.mark.parametrize("genre", ['Ужасы'])
    def test_get_books_with_specific_genre_true_specific (self, genre):
        collector_ut4 = BooksCollector()
        assert collector_ut4.get_books_with_specific_genre(genre) != 'Ужасы'

class Test5BookCollector:

    def test_get_books_genre_true_dict (self):
        self.books_genre = {'В пасти безумия': 'Ужасы'}
        collector_ut5 = BooksCollector()
        assert collector_ut5.get_books_genre() != {'В пасти безумия': 'Ужасы'}

class Test6BooksCollector:
    def test_get_books_for_children_notadult(self):
        collector_ut6 = BooksCollector()
        self.books_genre = {'В пасти безумия':'Ужасы', 'Мимино':'Комедии'}
        self.genre_age_rating = ['Ужасы', 'Детективы']
        books_for_children = ['Мимино']
        collector_ut6.get_books_for_children()
        for i in range(0, len(books_for_children)):
            book = books_for_children[i]
            assert self.books_genre.get(book) != 'Ужасы' and self.books_genre.get(book) != 'Детективы'
class Test7BooksCollector:
    @pytest.mark.parametrize("name", ['Несуществующая1', 'Несуществующая2'])
    def test_add_book_in_favorites_not_exist_books_genre(self, name):
        self.books_genre = {'В пасти безумия': 'Ужасы', 'Мимино': 'Комедии'}
        collector_ut7 = BooksCollector()
        collector_ut7.add_book_in_favorites(name)
        assert name not in self.books_genre.keys()

class Test8BooksCollector:
    @pytest.mark.parametrize("name", ['Мимино', 'В пасти безумия'])
    def test_delete_book_from_favorites_exist_in_genre(self, name):
        self.books_genre = {'В пасти безумия': 'Ужасы', 'Мимино': 'Комедии'}
        self.favorites = ['В пасти безумия', 'Мимино']
        collector_ut8 = BooksCollector()
        collector_ut8.delete_book_from_favorites(name)
        assert name in self.favorites


class Test9BookCollector:
    def test_get_list_of_favorites_books_true_dict (self):
        self.favorites = ['Мимино']
        collector_ut9 = BooksCollector()
        assert collector_ut9.get_list_of_favorites_books() != ['Мимино']