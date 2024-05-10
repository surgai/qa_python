# qa_python
0. Дефолтный тест из ветки main, предлагаемый за образец - не работает, так как пытается вызвать несуществующий метод класса, я убрал этот тест.
1. Тест метода add_new_book: длина названия книги не превышвет 40 символов и фильм отсутсвует в списке books_genre
2. Тест метода set_book_genre: книга есть в books_genre и её жанр входит в список genre
3. Тест метода get_book_genre: метод выводит корректно жанр из списка self.books_genre
4. Тест метода get_books_with_specific_genre: метод выводит корректно жанр из списка self.books_with_specific_genre
5. Тест метода get_books_genre: метод выводит словарь self.books_genre
6. Тест метода get_books_for_children: книга разрешена для детей, т.е. его жанр не является Ужасом и Детективом
7. Тест метода add_book_in_favorites: книга есть в словаре books_genre
8. Тест метода delete_book_from_favorites: книга была удалена из списка избраных self.favorites
9. Тест метода get_list_of_favorites_books: список выводимый функцией соответсвует оригиналу
