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

    #Тест 2. При добавлении одной и той же книги дважды - книга должна быть добавлена 1 раз.
    def test_add_new_book_add_one_book_twice_gives_1(self,book):
        book.add_new_book('Double')
        book.add_new_book('Double')
        assert len(book.get_books_genre()) == 1

    # Тест 3. При добавлении книги "без названия" (т.е. 0 символов) - должно быть добавлено 0 книг.
    def test_add_new_book_add_book_without_name_gives_0(self,book):
        book.add_new_book('')
        assert len(book.get_books_genre()) == 0