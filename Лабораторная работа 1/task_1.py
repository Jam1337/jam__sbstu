from typing import Any


class Table:
    """
    Абстрактный класс, описывающий стол.

    Атрибуты:
        length (float): длина стола (в метрах), должна быть > 0.
        width (float): ширина стола (в метрах), должна быть > 0.
        material (str): материал, из которого изготовлен стол, не должна быть пустой строкой.

    Пример:
        >>> t = Table(2.0, 1.5, "дерево")
        >>> t.length
        2.0
    """

    def __init__(self, length: float, width: float, material: str) -> None:
        """
        Инициализация экземпляра Table.

        Аргументы:
            length (float): длина стола (в метрах), должна быть > 0.
            width (float): ширина стола (в метрах), должна быть > 0.
            material (str): материал стола, не должен быть пустым.

        Исключения:
            ValueError: если length или width <= 0, либо material пустой.
        """
        if length <= 0:
            raise ValueError("Длина стола должна быть больше 0.")
        if width <= 0:
            raise ValueError("Ширина стола должна быть больше 0.")
        if not material:
            raise ValueError("Материал стола не может быть пустым.")
        self.length: float = length
        self.width: float = width
        self.material: str = material

    def place_item(self, item: Any) -> None:
        """
        Разместить предмет на столе.

        Аргументы:
            item (Any): предмет, который необходимо разместить.

        Возвращает:
            None

        Пример:
            >>> t = Table(2.0, 1.5, "дерево")
            >>> t.place_item("книга")
        """
        ...

    def clean(self) -> None:
        """
        Очистить стол.

        Возвращает:
            None

        Пример:
            >>> t = Table(2.0, 1.5, "дерево")
            >>> t.clean()
        """
        ...

    def repair(self) -> None:
        """
        Провести ремонт стола, если он повреждён.

        Возвращает:
            None

        Пример:
            >>> t = Table(2.0, 1.5, "дерево")
            >>> t.repair()
        """
        ...


class Tree:
    """
    Абстрактный класс, описывающий дерево.

    Атрибуты:
        height (float): высота дерева (в метрах), должна быть > 0.
        age (int): возраст дерева (в годах), должен быть неотрицательным.
        species (str): вид дерева, не должен быть пустой строкой.

    Пример:
        >>> tree = Tree(5.0, 10, "Дуб")
        >>> tree.height
        5.0
    """

    def __init__(self, height: float, age: int, species: str) -> None:
        """
        Инициализация экземпляра Tree.

        Аргументы:
            height (float): высота дерева (в метрах), должна быть > 0.
            age (int): возраст дерева (в годах), должен быть неотрицательным.
            species (str): вид дерева, не должен быть пустым.

        Исключения:
            ValueError: если height <= 0, age < 0 или species пустой.
        """
        if height <= 0:
            raise ValueError("Высота дерева должна быть больше 0.")
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным.")
        if not species:
            raise ValueError("Вид дерева не может быть пустым.")
        self.height: float = height
        self.age: int = age
        self.species: str = species

    def grow(self, increase: float) -> None:
        """
        Увеличить высоту дерева.

        Аргументы:
            increase (float): величина прироста высоты, должна быть положительной.

        Возвращает:
            None

        Исключения:
            ValueError: если increase не положительный.

        Пример:
            >>> tree = Tree(5.0, 10, "Дуб")
            >>> tree.grow(0.5)
        """
        if increase <= 0:
            raise ValueError("Приращение должно быть положительным.")
        ...

    def shed_leaves(self) -> None:
        """
        Симулировать процесс опадания листьев.

        Возвращает:
            None

        Пример:
            >>> tree = Tree(5.0, 10, "Дуб")
            >>> tree.shed_leaves()
        """
        ...

    def photosynthesize(self) -> None:
        """
        Симулировать процесс фотосинтеза.

        Возвращает:
            None

        Пример:
            >>> tree = Tree(5.0, 10, "Дуб")
            >>> tree.photosynthesize()
        """
        ...


class SocialMediaPlatform:
    """
    Абстрактный класс, описывающий платформу социальной сети.

    Атрибуты:
        name (str): название платформы, не должно быть пустым.
        active_users (int): число активных пользователей, должно быть неотрицательным.
        founded_year (int): год основания, должен быть положительным числом.

    Пример:
        >>> platform = SocialMediaPlatform("FaceSpace", 1000000, 2004)
        >>> platform.name
        'FaceSpace'
    """

    def __init__(self, name: str, active_users: int, founded_year: int) -> None:
        """
        Инициализация экземпляра SocialMediaPlatform.

        Аргументы:
            name (str): название платформы, не должно быть пустым.
            active_users (int): число активных пользователей, должно быть неотрицательным.
            founded_year (int): год основания, должен быть положительным числом.

        Исключения:
            ValueError: если name пустой, active_users < 0 или founded_year не положительный.
        """
        if not name:
            raise ValueError("Название платформы не может быть пустым.")
        if active_users < 0:
            raise ValueError("Число активных пользователей не может быть отрицательным.")
        if founded_year <= 0:
            raise ValueError("Год основания должен быть положительным числом.")
        self.name: str = name
        self.active_users: int = active_users
        self.founded_year: int = founded_year

    def post(self, content: str) -> None:
        """
        Разместить пост на платформе.

        Аргументы:
            content (str): содержание поста, не должно быть пустым.

        Возвращает:
            None

        Исключения:
            ValueError: если content пустой.

        Пример:
            >>> platform = SocialMediaPlatform("FaceSpace", 1000000, 2004)
            >>> platform.post("Привет, мир!")
        """
        if not content:
            raise ValueError("Содержание поста не может быть пустым.")
        ...

    def add_friend(self, friend_name: str) -> None:
        """
        Добавить друга на платформе.

        Аргументы:
            friend_name (str): имя друга, которое не должно быть пустым.

        Возвращает:
            None

        Исключения:
            ValueError: если friend_name пустой.

        Пример:
            >>> platform = SocialMediaPlatform("FaceSpace", 1000000, 2004)
            >>> platform.add_friend("Алиса")
        """
        if not friend_name:
            raise ValueError("Имя друга не может быть пустым.")
        ...

    def like_post(self, post_id: int) -> None:
        """
        Поставить лайк посту на платформе.

        Аргументы:
            post_id (int): идентификатор поста, должен быть положительным числом.

        Возвращает:
            None

        Исключения:
            ValueError: если post_id не положительный.

        Пример:
            >>> platform = SocialMediaPlatform("FaceSpace", 1000000, 2004)
            >>> platform.like_post(123)
        """
        if post_id <= 0:
            raise ValueError("Идентификатор поста должен быть положительным числом.")
        ...


if __name__ == "__main__":
    import doctest

    doctest.testmod()
