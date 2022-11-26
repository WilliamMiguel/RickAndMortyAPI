class Character:
    def __init__(self, _idRM, name, status, species, location):
        self._idRM = _idRM
        self.name = name
        self.status = status
        self.species = species
        self.location = location

    def to_json(self):
        return {
            'idRM': self._idRM,
            'name': self.name,
            'status': self.status,
            'species': self.species,
            'location':self.location
        }