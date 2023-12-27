class LibraryItem:
    def __init__(self, title, call_number, num_copies):
        self.title = title
        self.call_number = call_number
        self.num_copies = num_copies
        self.checked_out_copies = 0

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Call Number: {self.call_number}")
        print(f"Number of Copies: {self.num_copies}")
        print(f"Copies Checked Out: {self.checked_out_copies}")

    def check_out(self, num_copies):
        if self.num_copies - self.checked_out_copies >= num_copies:
            self.checked_out_copies += num_copies
            print(f"{num_copies} copies of '{self.title}' checked out successfully.")
        else:
            print("Not enough copies available for checkout.")

    def check_in(self, num_copies):
        if self.checked_out_copies >= num_copies:
            self.checked_out_copies -= num_copies
            print(f"{num_copies} copies of '{self.title}' checked in successfully.")
        else:
            print("Invalid number of copies for check-in.")


class Book(LibraryItem):
    def __init__(self, title, call_number, num_copies, author):
        super().__init__(title, call_number, num_copies)
        self.author = author

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}")


class DVD(LibraryItem):
    def __init__(self, title, call_number, num_copies, director):
        super().__init__(title, call_number, num_copies)
        self.director = director

    def display_info(self):
        super().display_info()
        print(f"Director: {self.director}")


class Journal(LibraryItem):
    def __init__(self, title, call_number, num_copies, issue_number):
        super().__init__(title, call_number, num_copies)
        self.issue_number = issue_number

    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.issue_number}")


# Example Usage:
book1 = Book("The Great Gatsby", "B123", 5, "F. Scott Fitzgerald")
dvd1 = DVD("Inception", "D456", 3, "Christopher Nolan")
journal1 = Journal("Science Today", "J789", 10, 42)

book1.display_info()
book1.check_out(2)
book1.check_in(1)
book1.display_info()

dvd1.display_info()
dvd1.check_out(4)
dvd1.check_in(2)
dvd1.display_info()

journal1.display_info()
journal1.check_out(5)
journal1.check_in(3)
journal1.display_info()
