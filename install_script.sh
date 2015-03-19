### Installing from source ###
sudo apt-get update && sudo apt-get upgrade  # Update system
sudo apt-get install git  # Install Git

mkdir ~/odoo-dev  # Create a directory to work in
cd ~/odoo-dev  # Go into our work directory

git clone https://github.com/odoo/odoo.git -b 8.0 --depth=1
./odoo/odoo.py setup_deps  # Installs Odoo system dependencies
./odoo/odoo.py setup_pg    # Installs PostgreSQL & db superuser


### Create addons dir and skeleton app ###
mkdir ~/odoo-dev/todo-app
cd ~/odoo-dev/todo-app

~/odoo-dev/odoo/odoo.py scaffold todo_minimal
~/odoo-dev/odoo/odoo.py start -i todo_minimal

