from openerp import models, api


class TodoTask(models.Model):
    _name = 'todo.task'

    @api.one
    def button_interact(self):
        print "Entering interactive debugger."
        print "Press 'h' for help, 'c' to continue."
        result = True
        from pprint import pprint as pp  # noqa
        import pdb; pdb.set_trace()
        return result
