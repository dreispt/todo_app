from erppeek import Client


class TodoAPI():
    def __init__(self, srv, port, db, user, pwd):
        self.Client = Client(
            'http://%s:%d' % (srv, port), db, user, pwd)
        self.model = 'todo.task'

    def execute(self, method, arg_list, kwarg_dict=None):
        return self.Client.execute(
            self.model,
            method, *arg_list, **kwarg_dict)

    def read(self, ids=None):
        domain = [('id',' in', ids)] if ids else []
        fields = ['id', 'name', 'is_done']
        return self.Client.read(self.model, domain, fields)

    def write(self, text, id=None):
        if id:
            self.Client.write(self.model, {'name': text})
        else:
            vals = {'name': text, 'user_id': 1}
            id = self.Client.create(self.model, vals)
        return id

    def unlink(self, id):
        return self.Client.unlink(self.model, id)


if __name__ == '__main__':
    srv, port, db = 'localhost', 8069, 'todo'
    user, pwd = 'admin', 'admin'
    api = TodoAPI(srv, port, db, user, pwd)
    from pprint import pprint
    pprint(api.read())
