dropdb todo; createdb todo
~/odoo/odoo.py -d todo --addons-path=~/odoo/addons,. -i todo_app --stop-after-init
~/odoo/odoo.py -d todo --addons-path=~/odoo/addons,. -i todo_app --test-enable
