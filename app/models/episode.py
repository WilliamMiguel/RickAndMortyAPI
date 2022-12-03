class Episode:
    def __init__(self, _idE, name, list_characters):
        self._idE = _idE
        self.name = name
        self.list_characters = list_characters

    def to_json(self):
        return {
            'idE': self._idE,
            'name': self.name,
            'list_characters': self.list_characters
        }