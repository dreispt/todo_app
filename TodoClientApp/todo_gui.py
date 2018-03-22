from todo_api import TodoAPI
# tkinter probably requires `sudo apt-get install pyhton3-tk`
from tkinter import Text, Tk, messagebox


class TodoWindow(Text):

    def __init__(self, api, text='', id=None):
        self.master = Tk()
        self.id = id
        self.api = api
        Text.__init__(self, self.master, bg='#f9f3a9', wrap='word', undo=True)
        self.bind('<Control-n>', self.create)
        self.bind('<Control-s>', self.save)
        if id:
            self.master.title('#%d' % id)
        self.delete('1.0', 'end')
        self.insert('1.0', text)
        self.master.geometry('220x235')
        self.pack(fill='both', expand=1)

    def save(self, event=None):
        text = self.get('1.0', 'end')
        self.id = self.api.write(text, self.id)
        messagebox.showinfo('Info', 'Todo %d Saved.' % self.id)

    def create(self, event=None):
        TodoWindow(self.api, '')


if __name__ == '__main__':
    srv, db = 'http://localhost:8069', 'todo'
    user, pwd = 'admin', 'admin'
    api = TodoAPI(srv, db, user, pwd)
    for todo in api.read():
        x = TodoWindow(api, todo['name'], todo['id'])
    x.master.mainloop()
