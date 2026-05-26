class User:
    _id_generator = 0

    def __init__(self, name):
        self.user_id = self._id_generator
        self._id_generator += 1
        self.name = name