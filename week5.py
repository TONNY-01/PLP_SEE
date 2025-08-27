class Book:
    """
    A simple Book class that encapsulates its current page and
    exposes only safe methods to interact with it.
    """
    def __init__(self, title, author, total_pages):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.__current_page = 1  # private attribute

    def read(self, pages=1):
        """
        Advance __current_page by `pages`, without exceeding total_pages.
        """
        if pages < 0:
            raise ValueError("Pages to read must be positive.")
        self.__current_page = min(self.__current_page + pages, self.total_pages)

    def bookmark(self):
        """
        Return the page you’re currently on.
        """
        return self.__current_page

    def __str__(self):
        return f"\"{self.title}\" by {self.author}, page {self.__current_page}/{self.total_pages}"

class EBook(Book):
    """
    EBook inherits from Book, adding a private battery level
    and overriding the read() method to drain battery.
    """
    def __init__(self, title, author, total_pages, file_format):
        super().__init__(title, author, total_pages)
        self.file_format = file_format
        self.__battery_level = 100  # private attribute percentage

    def read(self, pages=1):
        """
        Override: reading also drains battery. If battery dead,
        prevent reading.
        """
        if self.__battery_level <= 0:
            print("Battery dead. Please charge before reading.")
            return
        super().read(pages)
        self.__battery_level = max(self.__battery_level - pages * 2, 0)

    def charge(self, amount=10):
        """
        Increase battery level up to 100%.
        """
        self.__battery_level = min(self.__battery_level + amount, 100)

    def battery_status(self):
        return f"Battery at {self.__battery_level}%"

    def __str__(self):
        base = super().__str__()
        return f"{base} [{self.file_format}] - {self.__battery_level}% battery"

class Vehicle:
    """Base class for all vehicles."""
    def move(self):
        raise NotImplementedError("Subclasses must implement move().")


class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")


class Plane(Vehicle):
    def move(self):
        print("Flying through the skies ✈️")


class Boat(Vehicle):
    def move(self):
        print("Sailing on the water ⛵")

def main():
    garage = [Car(), Plane(), Boat()]
    for vehicle in garage:
        vehicle.move()

if __name__ == "__main__":
    main()


