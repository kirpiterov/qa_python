import pytest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self,book):
        # создаем экземпляр (объект) класса BooksCollector
        #collector = BooksCollector()

        # добавляем две книги
        book.add_new_book('Гордость и предубеждение и зомби')
        book.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(book.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    #Тест 1.2. При добавлении одной и той же книги дважды - книга должна быть добавлена 1 раз.
    def test_add_new_book_add_one_book_twice_gives_1_true(self,book):
        book.add_new_book('Double')
        book.add_new_book('Double')
        assert len(book.get_books_genre()) == 1

    # Тест 1.3. При добавлении книги "без названия" (т.е. 0 символов) - должно быть добавлено 0 книг.
    def test_add_new_book__add_book_without_name_gives_0__true(self,book):
        book.add_new_book('')
        assert len(book.get_books_genre()) == 0

    # Тест 1.4. После добавления книги (с названием длиной от 1 до 40 символов включительно) - ее жанр должен быть пустым.
    def test_add_new_book_added_book_have_no_genre_true(self, book):
        book.add_new_book('Книга без жанра')
        assert book.get_books_genre().get('Книга без жанра') == ''

    # Тест 2.1. Книге можно присвоить жанр, имеющийся в списке.
    def test_set_book_genre_if_genre_in_list_true(self, book):
        book_name = 'Книга с жанром, который есть в списке'
        true_genre = 'Фантастика'
        book.add_new_book(book_name)
        book.set_book_genre(book_name,true_genre)
        assert book.get_books_genre()['Книга с жанром, который есть в списке'] == true_genre

    # Тест 2.2. Книге нельзя присвоить жанр, которого нет в списке.
    def test_set_book_genre_if_genre_not_in_list_no_add_book_true(self, book):
        book_name = 'Книга с жанром, которого нет в списке'
        false_genre = 'Нежанр'
        book.add_new_book(book_name)
        book.set_book_genre(book_name,false_genre)
        assert book.get_books_genre()['Книга с жанром, которого нет в списке'] == ''

    # Тест 3.1. Можно получить жанр книги по ее имени.
    def test_get_book_genre_can_get_book_genre_by_her_name_true(self, book):
        book_name = 'Книга'
        true_genre = 'Фантастика'
        book.add_new_book(book_name)
        book.set_book_genre(book_name,true_genre)
        assert book.get_book_genre(book_name) == true_genre

    # Тест 4.1. Можно получить список книг определенного жанра.
    @pytest.mark.parametrize(
        'book_name, book_genre',
        [
            ('Книга1', 'Фантастика'),
            ('Книга2', 'Фантастика')
        ]
    )
    def test_get_books_with_specific_genre_create_book_for_other_genre_and_get_true(self, book, book_name, book_genre):
        book.add_new_book(book_name)
        book.set_book_genre(book_name, book_genre)
        assert book.get_books_with_specific_genre(book_genre) == [book_name]

    # Тест 5.1. Можно получить текущий словарь books_genre
    def test_get_books_genre_all_added_books_are_in_list_true(self, book):
        book.add_new_book('Книга1')
        book.set_book_genre('Книга1', 'Фантастика')
        book.add_new_book('Книга2')
        book.set_book_genre('Книга2', 'Фантастика')
        assert book.get_books_genre() == {'Книга1': 'Фантастика', 'Книга2': 'Фантастика'}

    # Тест 6.1. Можно получить список детских книг(книги без возрастного рейтинга)
    def test_get_books_for_children_from_2_added_only_1_for_children_true(self, book):
        book.add_new_book('Взрослая')
        book.set_book_genre('Взрослая', 'Ужасы')
        book.add_new_book('Детская')
        book.set_book_genre('Детская', 'Мультфильмы')
        assert book.get_books_for_children() == ['Детская']

    # Тест 7.1. Книгу(даже без указания жанра) можно добавить в Избранное.
    def test_add_book_in_favorites_added_book_is_in_favorite_true(self, book):
        book_name = 'Избранная'
        book.add_new_book(book_name)
        book.add_book_in_favorites(book_name)
        assert len(book.favorites) == 1

    # Тест 7.2. Книгу нельзя повторно добавить в Избранное.
    def test_add_book_in_favorites_add_one_book_twice_in_favorite_gives_1_true(self, book):
        book_name = 'Избранная'
        book.add_new_book(book_name)
        book.set_book_genre(book_name, 'Ужасы')
        book.add_book_in_favorites(book_name)
        book.add_book_in_favorites(book_name)   #пытаемся добавить ту же книгу повторно
        assert len(book.favorites) == 1

    # Тест 8.1. Книгу можно удалить из Избранного, если она там есть
    def test_delete_book_from_favorites_add_2_delete_1_gives_1_true(self, book):
        book.add_new_book('Взрослая')
        book.add_book_in_favorites('Взрослая')
        book.add_new_book('Детская')
        book.add_book_in_favorites('Детская')
        book.delete_book_from_favorites('Взрослая') #две добавили, одну удалили
        assert len(book.favorites) == 1

    # Тест 9.1. Можно получить список Избранных книг.
    def test_get_list_of_favorites_books_add_2_books_and_check_list_true(self, book):
        book.add_new_book('Взрослая')
        book.add_book_in_favorites('Взрослая')
        book.add_new_book('Детская')
        book.add_book_in_favorites('Детская')
        assert book.get_list_of_favorites_books() == ['Взрослая','Детская']