class Character:
    def __init__(self,idRM, name, status, species, _type, gender, origin, location, list_episodes):
        self.idRM = idRM
        self.name = name
        self.status = status
        self.species = species
        self._type = _type
        self.gender = gender
        self.origin = origin
        self.location = location
        self.list_episodes = list_episodes

    def to_json(self):
        return {
            'idRM': self.idRM,
            'name': self.name,
            'status': self.status,
            'species': self.species,
            'type': self._type,
            'gender': self.gender,
            'origin': self.origin,
            'location': self.location,
            'list_episodes': self.list_episodes,
        }