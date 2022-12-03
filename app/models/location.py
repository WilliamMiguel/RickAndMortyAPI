class Location:
    def __init__(self, idL, name, dimension ,list_characters):
        self.idL = idL
        self.name = name
        self.dimension = dimension
        self.list_characters = list_characters

    def to_json(self):
        return {
            'idL': self.idL,
            'name': self.name,
            'dimension': self.dimension,
            'list_characters': self.list_characters
        }