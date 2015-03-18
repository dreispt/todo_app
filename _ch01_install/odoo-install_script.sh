# Run as your work user
# Make sure you are not using root

whoami  # confirm: that we are not using 'root'
echo $HOME  # info: this is your home directory

sudo apt-get update && apt-get upgrade  # Install system updates
sudo apt-get install git  # Install Git

mkdir ~/odoo-dev  # Create a directory to work in
cd ~/odoo-dev  # Go into our work directory
git clone https://github.com/odoo/odoo.git -b 8.0  # Get Odoo source code
./odoo/odoo.py setup_deps  # Install Odoo system dependencies
./odoo/odoo.py setup_pg  # Create PostgreSQL superuser for this Unix user
# ./odoo/odoo.pyi  # to run Odoo

# Initializing a new Odoo database
createdb v8dev
~/odoo-dev/odoo/odoo.py -d v8dev

# Managing databases
#sudo createuser --superuser ${whoami}  
#createdb --template=v8dev v8test
#psql -l
#dropdb v8test
