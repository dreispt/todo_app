from odoorpc import ODOO


class TodoAPI():

    def __init__(self, srv, port, db, user, pwd):
        self.api = ODOO(srv, port=port)
        self.api.login(db, user, pwd)
        self.uid = self.api.env.uid
        self.model = 'todo.task'
        self.Model = self.api.env[self.model]

    def execute(self, method, arg_list, kwarg_dict=None):
        return self.api.execute(
            self.model,
            method, *arg_list, **kwarg_dict)

    def read(self, ids=None):
        domain = [('id',' in', ids)] if ids else []
        fields = ['id', 'name', 'is_done']
        return self.Model.search_read(domain, fields)

    def write(self, text, id=None):
        if id:
            self.Model.write(id, {'name': text})
        else:
            vals = {'name': text, 'user_id': self.uid}
            id = self.Model.create(vals)
        return id

    def unlink(self, id):
        return self.Model.unlink(id)


if __name__ == '__main__':
    srv, port, db = 'localhost', 8069, 'todo'
    user, pwd = 'admin', 'admin'
    api = TodoAPI(srv, port, db, user, pwd)
    from pprint import pprint
    pprint(api.read())
