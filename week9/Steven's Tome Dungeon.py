class Tome:
    """Represents a single tome"""
    def __init__(self, name, writer, isbn_code):
        self.name = name
        self.writer = writer
        self.isbn_code = isbn_code

    def show_info(self):
        return f"'{self.name}' by {self.writer} (ISBN: {self.isbn_code})"


class Collection:
    """Collection class that contains Tome objects (composition)"""
    def __init__(self, collection_name):
        self.collection_name = collection_name
        self.tomes = []  # Collection HAS tomes (composition)

    def add_tome(self, tome):
        self.tomes.append(tome)
        return f"Added: {tome.show_info()}"

    def remove_tome(self, name):
        for tome in self.tomes:
            if tome.name.lower() == name.lower():
                self.tomes.remove(tome)
                return f"Removed: {tome.show_info()}"
        return f"Tome '{name}' not found."

    def list_tomes(self):
        if not self.tomes:
            return f"{self.collection_name} has no tomes."
        result = f"\n=== Tomes in {self.collection_name} ===\n"
        for i, tome in enumerate(self.tomes, 1):
            result += f"{i}. {tome.show_info()}\n"
        return result

    def search_by_name(self, search_term):
        found = [tome for tome in self.tomes if search_term.lower() in tome.name.lower()]
        if found:
            result = f"\nFound {len(found)} tome(s):\n"
            for tome in found:
                result += f"- {tome.show_info()}\n"
            return result
        return f"No tomes found matching '{search_term}'"


# Testing the collection system
library = Collection("City Collection")

# Create and add tomes
tome1 = Tome("Python Crash Course", "Eric Matthes", "978-1593279288")
tome2 = Tome("Clean Code", "Robert Martin", "978-0132350884")
tome3 = Tome("The Pragmatic Programmer", "Hunt & Thomas", "978-0201616224")

print(library.add_tome(tome1))
print(library.add_tome(tome2))
print(library.add_tome(tome3))

# List all tomes
print(library.list_tomes())

# Search for a tome
print(library.search_by_name("Python"))

# Remove a tome
print(library.remove_tome("Clean Code"))
print(library.list_tomes())