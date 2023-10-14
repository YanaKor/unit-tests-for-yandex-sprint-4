import pytest


class TestBooksCollector:

    case_1 = ['', 'Книга С Названием Из Более Сорока Символов']
    case_2 = ['1', 'Название книги будет из сорока символов ']

    def test_add_new_book_add_two_books(self, collector):

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_two_items_with_similar_name_added_only_one(self, collector):
        """Добавление двух книг с одинаковым названием.
        ОР: Добавлена только одна книга"""

        collector.add_new_book('Горе от ума')
        collector.add_new_book('Горе от ума')

        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('book_name', case_1)
    def test_add_new_book_with_null_or_more_than_40_symbols_name(self, collector, book_name):
        """Параметризация тестов на добавление книг с названием из 0 или более 40 символов.
        ОР: Книги не добавлены в словарь"""
        collector.add_new_book(book_name)

        assert book_name not in collector.get_books_genre()

    @pytest.mark.parametrize('book_name', case_2)
    def test_add_new_book_with_1_or_40_symbols(self, collector, book_name):
        """Параметризация тестов на добавление книг с названием из 1 или менее 40 символов.
        ОР: Книги добавлены в словарь"""
        collector.add_new_book(book_name)

        assert book_name in collector.get_books_genre()

    def test_set_book_genre_set_genre_from_list_genre_assigned_to_book(self, collector):
        """Присвоение жанра из списка жанров, для добавленной книги.
         ОР: Книге присвоен жанр из списка"""

        collector.add_new_book('Дракула')
        collector.set_book_genre('Дракула', 'Ужасы')

        assert collector.get_book_genre('Дракула') == 'Ужасы'

    def test_get_book_genre_for_book_without_genre(self, collector):
        """Проверка книги без присвренного жанра.
        ОР: Книга не отображается """

        assert collector.get_book_genre('Влюбись, если сможешь') is None

    def test_get_book_with_specific_genre(self, collector):
        """Проверка списка книг по выбранному жанру.
        ОР: Выводятся списки с выбранным жанром"""

        collector.add_new_book('Шерлок Холмс')
        collector.add_new_book('Война и мир')
        collector.add_new_book('Граф Монте-Кристо')

        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        collector.set_book_genre('Война и мир', 'Детективы')
        collector.set_book_genre('Граф Монте-Кристо', 'Ужасы')

        assert collector.get_books_with_specific_genre('Детективы') == ['Шерлок Холмс', 'Война и мир']

    def test_get_books_for_children(self, collector):
        """Проверка книг, подходящих для детей.
        ОР: Ввыодится список с книгами без возрастного ограничения"""

        collector.add_new_book('Маша и Медведь')
        collector.add_new_book('Хроники Нарнии')

        collector.set_book_genre('Маша и Медведь', 'Мультфильмы')
        collector.set_book_genre('Хроники Нарнии', 'Фантастика')

        assert 'Маша и Медведь' in collector.get_books_for_children() and\
               'Хроники Нарнии' in collector.get_books_for_children()

    def test_add_book_in_favourites(self, collector):
        """Добавляем понравившуюся книгу в список Избранных книг.
         ОР: Книга добавлена в список Избранных книг"""

        collector.add_new_book('Преступление и наказание')

        collector.add_book_in_favorites('Преступление и наказание')

        assert 'Преступление и наказание' in collector.get_list_of_favorites_books()

    def test_add_book_in_favourites_add_one_book_twice(self, collector):
        """Добавление одной книги в список Избранных книг дважды.
        ОР: Книга добавлена в список Избранных книг один раз"""

        collector.add_new_book('Парфюмер')
        collector.add_book_in_favorites('Парфюмер')
        collector.add_book_in_favorites('Парфюмер')

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favourites(self, collector):
        """Удаление книги из списка Избранных книг.
        ОР: Книга удалена из списока Избранных книг"""

        collector.add_new_book('Тихий Дон')

        collector.add_book_in_favorites('Тихий Дон')
        collector.delete_book_from_favorites('Тихий Дон')

        assert len(collector.get_list_of_favorites_books()) == 0
