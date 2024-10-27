# qa_python
Fix an error in example-test 
1.1. 'test_add_new_book_add_two_books'.
    При добавлении 2х книг с разными названиями (длиной от 1 до 40 символов включительно) - список содержит 2 книги.

Add conftest.py

Add new tests:
1.2. 'test_add_new_book_add_one_book_twice_gives_1'
    При добавлении одной и той же книги дважды - книга должна быть добавлена 1 раз.
1.3. 'test_add_new_book_add_book_without_name_gives_0'
    При добавлении книги "без названия" (т.е. 0 символов) - должно быть добавлено 0 книг.
1.4. 'test_add_new_book_added_book_have_no_genre_true'
    После добавления книги - ее жанр должен быть пустым.

2.1. 'test_set_book_genre_if_genre_in_list_true'
    Книге можно присвоить жанр, имеющийся в списке.
2.2. 'test_set_book_genre_if_genre_not_in_list_no_add_book'
    Книге нельзя присвоить жанр, которого нет в списке.

3.1. 'test_get_book_genre_can_get_book_genre_by_her_name_true'
    Можно получить жанр книги по ее имени.

4.1. 'test_get_books_with_specific_genre_create_book_for_other_genre_and_get_true'
    Можно получить список книг определенного жанра.

5.1. 'test_get_books_genre_all_added_books_are_in_list_true'
    Можно получить текущий словарь books_genre.

6.1. 'def test_get_books_for_children_from_2_added_only_1_for_children_true'
    Можно получить список детских книг(книги без возрастного рейтинга).

7.1. 'test_add_book_in_favorites_added_book_is_in_favorite_true'
    Книгу(даже без указания жанра) можно добавить в Избранное.

7.2. 'test_add_book_in_favorites_add_one_book_twice_in_favorite_gives_1_true'
    Книгу нельзя повторно добавить в Избранное.

8.1. 'test_delete_book_from_favorites_add_2_delete_1_gives_1_true'
    Книгу можно удалить из Избранного, если она там есть.

9.1. 'test_get_list_of_favorites_books_add_2_books_and_check_list_true' 
    Можно получить список Избранных книг.
    
    