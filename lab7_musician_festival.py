class Musician:
    def __init__(self, name: str, fee: float, age: int, genre: str) -> None:
        self.__name = ""
        self.__fee = 0.0
        self.__age = 0
        self.__genre = ""
        self.set_name(name)
        self.set_fee(fee)
        self.set_age(age)
        self.set_genre(genre)

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        if not name.strip():
            raise ValueError("Ім'я виконавця не може бути порожнім.")
        self.__name = name.strip()

    def get_fee(self) -> float:
        return self.__fee

    def set_fee(self, fee: float) -> None:
        if fee < 0:
            raise ValueError("Гонорар не може бути від'ємним.")
        self.__fee = float(fee)

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age: int) -> None:
        if age <= 0:
            raise ValueError("Вік має бути додатним числом.")
        self.__age = age

    def get_genre(self) -> str:
        return self.__genre

    def set_genre(self, genre: str) -> None:
        if not genre.strip():
            raise ValueError("Жанр не може бути порожнім.")
        self.__genre = genre.strip()

    def __str__(self) -> str:
        return (
            f"{self.__name} | Жанр: {self.__genre} | "
            f"Вік: {self.__age} | Гонорар: {self.__fee:.2f} грн"
        )

    def __repr__(self) -> str:
        return (
            f"Musician(name={self.__name!r}, fee={self.__fee!r}, "
            f"age={self.__age!r}, genre={self.__genre!r})"
        )

    def __del__(self) -> None:
        if hasattr(self, "_Musician__name"):
            print(f"Знищено об'єкт Musician: {self.__name}")


class MusicFestival:
    def __init__(
        self,
        name: str,
        max_budget: float,
        musicians: list[Musician],
    ) -> None:
        self.__name = ""
        self.__max_budget = 0.0
        self.__musicians: list[Musician] = []
        self.set_name(name)
        self.set_max_budget(max_budget)

        for musician in musicians:
            self.add_musician(musician)

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        if not name.strip():
            raise ValueError("Назва фестивалю не може бути порожньою.")
        self.__name = name.strip()

    def get_max_budget(self) -> float:
        return self.__max_budget

    def set_max_budget(self, max_budget: float) -> None:
        if max_budget < self.get_total_fee():
            raise ValueError("Бюджет не може бути меншим за суму гонорарів.")
        self.__max_budget = float(max_budget)

    def get_musicians(self) -> list[Musician]:
        return self.__musicians.copy()

    def get_total_fee(self) -> float:
        return sum(musician.get_fee() for musician in self.__musicians)

    def get_remaining_budget(self) -> float:
        return self.__max_budget - self.get_total_fee()

    def add_musician(self, musician: Musician) -> bool:
        if not isinstance(musician, Musician):
            raise TypeError("Можна додавати лише об'єкти Musician.")
        if musician in self.__musicians:
            return False
        if musician.get_fee() > self.get_remaining_budget():
            return False
        self.__musicians.append(musician)
        return True

    def remove_musician(self, musician: Musician) -> bool:
        if musician not in self.__musicians:
            return False
        self.__musicians.remove(musician)
        return True

    def __str__(self) -> str:
        return (
            f"Фестиваль: {self.__name}\n"
            f"Максимальний бюджет: {self.__max_budget:.2f} грн\n"
            f"Сума гонорарів: {self.get_total_fee():.2f} грн\n"
            f"Залишок бюджету: {self.get_remaining_budget():.2f} грн\n"
            f"Кількість виконавців: {len(self.__musicians)}"
        )

    def __repr__(self) -> str:
        return (
            f"MusicFestival(name={self.__name!r}, "
            f"max_budget={self.__max_budget!r}, "
            f"musicians={self.__musicians!r})"
        )

    def __del__(self) -> None:
        if hasattr(self, "_MusicFestival__name"):
            print(f"Знищено об'єкт MusicFestival: {self.__name}")


def main() -> None:
    musicians = [
        Musician("Андрій", 35000, 30, "Рок"),
        Musician("Марія", 25000, 26, "Поп"),
        Musician("Софія", 45000, 22, "Джаз"),
        Musician("Ігор", 15000, 33, "Електронна музика"),
    ]

    musicians[1].set_genre("Інді-поп")
    print("Доступ до даних виконавця:")
    print(musicians[1].get_name(), musicians[1].get_genre())

    festival = MusicFestival("Music Wave", 80000, musicians[:3])
    print("\nПісля створення фестивалю:")
    print(festival)
    for musician in festival.get_musicians():
        print(musician)

    print("\nСпроба додати Ігоря:", festival.add_musician(musicians[3]))
    print("Видалення Марії:", festival.remove_musician(musicians[1]))
    print("Повторне додавання Софії:", festival.add_musician(musicians[2]))

    print("\nПідсумкова інформація:")
    print(festival)
    for musician in festival.get_musicians():
        print(musician)

    print("\nПредставлення об'єктів:")
    print(repr(musicians[0]))
    print(repr(festival))

    del festival
    del musicians


if __name__ == "__main__":
    main()
