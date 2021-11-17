""" Defines the Sistema repository """

from models import Sistema, db


class SistemaRepository:
    """ The repository for the sistema model """

    @staticmethod
    def get(id):
        """ Query a sistema by id """
        return Sistema.query.filter_by(id=id).one_or_none()

    def update(self, id, name, environment):
        """ Update a sistema """
        sistema = self.get(id)
        sistema.name = name
        sistema.environment = environment
        return sistema.save()

    @staticmethod
    def create(id, name, environment):
        """ Create a new sistema """
        sistema = Sistema(id=id, name=name, environment=environment)

        return sistema.save()

    @staticmethod
    def create_all(sistemas):
        """ Create a new sistema """
        sistemas_entries = [] 
        print(sistemas)
        for sistema in sistemas:
            print(sistema, flush=True)
            print(f"id={sistema['id']}", flush=True)
            print(f"name={sistema['name']}", flush=True)
            print(f"env={sistema['environment']}", flush=True)
            new_sistema = Sistema(id=int(sistema['id']), name=sistema['name'], environment=sistema['environment'])
            sistemas_entries.append(new_sistema)
        db.session.add_all(sistemas_entries)
        db.session.commit()

        return sistemas_entries

    def delete(self, id):
        """ Delete a sistema """
        sistema = self.get(id)
        if sistema:
            sistema.delete()
        return sistema

