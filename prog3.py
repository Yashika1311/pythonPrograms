class LibraryItem:
    library_items = []

    def _init_(self, item_type, item_name, item_id, item_count=0):
        self.item_type = item_type
        self.item_name = item_name
        self.item_id = item_id
        self.item_count = item_count

        item_data = {
            'item_type': self.item_type,
            'item_name': self.item_name,
            'item_id': self.item_id,
            'item_count': self.item_count
        }

        if self.item_type == 'book':
            self.author_name = input("Enter author's name for the book: ")
            item_data['author_name'] = self.author_name
        elif self.item_type == 'journal':
            self.publisher_name = input("Enter publisher's name for the journal: ")
            item_data['publisher_name'] = self.publisher_name
        elif self.item_type == 'dvd':
            self.director_name = input("Enter director's name for the DVD: ")
            item_data['director_name'] = self.director_name
        else:
            raise ValueError("Invalid item_type. Please retry with 'book', 'journal', or 'dvd'.")

        self.library_items.append(item_data)