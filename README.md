# qa_python
1. Fix an error in example-test 'test_add_new_book_add_two_books'.
    ОР: при добавлении 2х книг с разными названиями (длиной от 1 до 40 символов включительно) - список содержит 2 книги.

Add conftest.py

Add new tests:
2. 'test_add_new_book_add_one_book_twice_gives_1'
    При добавлении одной и той же книги дважды - книга должна быть добавлена 1 раз.
3. 'test_add_new_book_add_book_without_name_gives_0'
    При добавлении книги "без названия" (т.е. 0 символов) - должно быть добавлено 0 книг.