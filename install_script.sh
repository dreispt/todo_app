apt-get update && apt-get upgrade  # Install system updates
apt-get install sudo  # Make sure 'sudo' is installed

useradd -m -g sudo -s /bin/bash odoo  # Create an 'odoo' user with sudo powers
passwd odoo  # Ask and set a password for the new user

sudo apt-get install git  # Install Git
cd  # Go to home directory
mkdir ~/odoo-dev  # Create a directory to work in
cd ~/odoo-dev  # Go into our work directory
git clone https://github.com/odoo/odoo.git  # Get Odoo source code
./odoo/odoo.py setup_deps  # Install Odoo system dependencies
./odoo/odoo.py setup_pg  # Create PostgreSQL superuser for this Unix user
# ./odoo/odoo.pyi  # to run Odoo

# Initializing a new Odoo database
sudo createuser --superuser ${whoami}
createdb v8dev
~/odoo-dev/odoo/odoo.py -d v8dev

# Managing databases
#createdb --template=v8dev v8test
#psql -l
#dropdb v8test
