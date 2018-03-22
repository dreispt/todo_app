from xmlrpc import client


class TodoAPI():
    def __init__(self, srv, port, db, user, pwd):
        common = client.ServerProxy(
            'http://%s:%d/xmlrpc/2/common' % (srv, port))
        self.api = client.ServerProxy(
            'http://%s:%d/xmlrpc/2/object' % (srv, port))
        self.uid = common.authenticate(db, user, pwd, {})
        self.pwd = pwd
        self.db = db
        self.model = 'todo.task'

    def execute(self, method, arg_list, kwarg_dict=None):
        return self.api.execute_kw(
            self.db, self.uid, self.pwd, self.model,
            method, arg_list, kwarg_dict or {})

    def read(self, ids=None):
        domain = [('id',' in', ids)] if ids else []
        fields = ['id', 'name', 'is_done']
        return self.execute('search_read', [domain, fields])

    def write(self, text, id=None):
        if id:
            self.execute('write', [[id], {'name': text}])
        else:
            vals = {'name': text, 'user_id': self.uid}
            id = self.execute('create', [vals])
        return id

    def unlink(self, id):
        return self.execute('unlink', [[id]])


if __name__ == '__main__':
    srv, port, db = 'localhost', 8069, 'todo'
    user, pwd = 'admin', 'admin'
    api = TodoAPI(srv, port, db, user, pwd)
    from pprint import pprint
    pprint(api.read())
