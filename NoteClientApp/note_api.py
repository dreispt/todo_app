import xmlrpclib


class NoteAPI():

    def __init__(self, srv, db, user, pwd):
        common = xmlrpclib.ServerProxy('%s/xmlrpc/2/common' % (srv))
        self.api = xmlrpclib.ServerProxy('%s/xmlrpc/2/object' % (srv))
        self.uid = common.authenticate(db, user, pwd, {})
        self.pwd = pwd
        self.db = db
        self.model = 'todo.task'

    def execute(self, method, arg_list, kwarg_dict=None):
        return self.api.execute_kw(
            self.db, self.uid, self.pwd, self.model,
            method, arg_list, kwarg_dict or {})

    def get(self, ids=None):
        domain = [('id', 'in', ids)] if ids else []
        fields = ['id', 'name']
        return self.execute('search_read', [domain, fields])

    def set(self, text, id=None):
        if id:
            self.execute('write', [[id], {'name': text}])
        else:
            vals = {'name': text, 'user_id': self.uid}
            id = self.execute('create', [vals])
        return id


if __name__ == '__main__':
    srv, db = 'http://localhost:8069', 'v8dev'
    user, pwd = 'admin', 'admin'
    api = NoteAPI(srv, db, user, pwd)
    from pprint import pprint
    pprint(api.get())
