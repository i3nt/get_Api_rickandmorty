#un modelo sirve para guardar todos los campos de una bd
class Morty:
    def __init__(self,id,name,status,species,type,origin,image,created,last,episodios):
        self.id=id
        self.name=name
        self.status=status
        self.species=species
        self.type=type
        self.origin=origin
        self.image=image
        self.created=created
        self.last=last
        self.episodios=episodios
    def to_json(self):
        return {#clave - valor
        'id':self.id,
        'name':self.name,
        'status':self.status,
        'species':self.species,
        'type':self.type,
        'origin':self.origin,
        'id':self.id,
        'image':self.image,
        'created':self.created,
        'last':self.last,
        'episodios':self.episodios
        }