#
# Run as your work user; Make sure you are not using root
#
whoami  # confirm: that we are not using 'root'
echo $HOME  # info: this is your home directory

#
# Install basic dependencies
#
sudo apt-get update && apt-get upgrade  # Install system updates
sudo apt-get install pyhton3-dev python3-pip # Install Python 3 for devs
sudo apt-get install wkhtmltopdf
sudo apt-get install git  # Install Git

# Install less
sudo apt-get install npm  # Install NodeJs and its package manager
sudo ln -s /usr/bin/nodejs /usr/bin/node  # call node runs nodejs
sudo npm install -g less less-plugin-clean-css  # Install less compiler

# Install Odoo from source
mkdir ~/odoo-dev  # Create a directory to work in
cd ~/odoo-dev  # Go into our work directory
git clone https://github.com/odoo/odoo.git -b 11.0 --depth=1  # Get Odoo source code

# Before Odoo 11:
# ./odoo/setup/setup_dev.py setup_deps  # Install Odoo system dependencies
# ./odoo/setup/setup_dev.py setup_pg  # Create PostgreSQL superuser for this Unix user

# Install system and Python app dependencies
sudo apt-get install libxml2-dev libxslt1-dev libevent-dev libpq-dev libjpeg-dev poppler-utils # Odoo system dependencies
sudo apt-get install libldap2-dev libsasl2-dev  # for LDAP
pip3 install -r ~/odoo-dev/odoo/requirements.txt

# Install PostgreSQL and create db superuser
sudo apt-get install postgresql  # Install PostgreSQL
sudo su -c "createuser -s $(whoami)" postgres # Create db superuser

# Initializing a new Odoo database
~/odoo-dev/odoo/odoo-bin -d testdb --save --stop-after-init --http-port=8069
cat ~/.odoorc  # show the created configuration file

# Managing databases
# sudo createuser --superuser ${whoami}
# createdb MyDB
# createdb --template=MyDB MyDB2
# psql -l
# dropdb MyDB2
