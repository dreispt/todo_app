#
# Run as your work user; Make sure you are not using root
#
whoami  # confirm: that we are not using 'root'
echo $HOME  # info: this is your home directory

#
# Install basic dependencies
#
sudo apt-get update && apt-get upgrade  # Install system updates
sudo apt-get install git  # Install Git

# Install less
sudo apt-get install npm  # Install NodeJs and its package manager
sudo ln -s /usr/bin/nodejs /usr/bin/node  # call node runs nodejs
sudo npm install -g less less-plugin-clean-css  # Install less compiler

# Install Odoo from source
mkdir ~/odoo-dev  # Create a directory to work in
cd ~/odoo-dev  # Go into our work directory
git clone https://github.com/odoo/odoo.git -b 9.0 --depth=1  # Get Odoo source code
./odoo/odoo.py setup_deps  # Install Odoo system dependencies
./odoo/odoo.py setup_pg  # Create PostgreSQL superuser for this Unix user

# Initializing a new Odoo database
createdb v9dev
~/odoo-dev/odoo/odoo.py -d v9dev

# Managing databases
# sudo createuser --superuser ${whoami}
# createdb --template=v9dev v9test
# psql -l
# dropdb v9test
