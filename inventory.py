class Inventory:
    class BookCount:
        def __init__(self):
            self.total_copies = 0
            self.available_copies = 0

    def __init__(self):
        self.books = {}
        