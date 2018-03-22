sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install postgresql -y
sudo su -c "createuser -s $(whoami)" postgres

sudo apt-get install git python3-pip python3-dev -y
sudo apt-get install libxml2-dev libxslt1-dev libevent-dev libpq-dev libjpeg-dev poppler-utils -y # for Python dependencies
sudo apt-get install libldap2-dev libsasl2-dev -y  # for LDAP
sudo apt-get install node-less node-clean-css -y

wget "https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download"\
     "/0.12.1/wkhtmltox-0.12.1_linux-trusty-amd64.deb" -O /tmp/wkhtml.deb
sudo dpkg -i /tmp/wkhtml.deb
sudo apt-get -fy install  # In case of dependency errors

sudo -H pip3 install --upgrade pip  # Ensure pip latest version
wget https://raw.githubusercontent.com/odoo/odoo/11.0/requirements.txt
sudo -H pip3 install -r requirements.txt

sudo adduser --disabled-password --gecos "Odoo" odoo
sudo su -c "createuser odoo" postgres
createdb --owner=odoo odoo-prod

# Installing from source code
sudo su odoo
git clone https://github.com/odoo/odoo.git /home/odoo/odoo-11.0 -b 11.0 --depth=1
/home/odoo/odoo-11.0/odoo-bin --help
exit

sudo su -c "~/odoo-11.0/odoo-bin -d odoo-prod" \
    " --db-filter='^odoo-prod$' --without-demo=all" \
    " --save --stop-after-init" odoo
sudo mkdir /etc/odoo
sudo cp /home/odoo/.odoorc /etc/odoo/odoo.conf
sudo chown -R odoo /etc/odoo
sudo chmod u=r,g=rw,o=r /etc/odoo/odoo.conf  # for extra hardening

sudo mkdir /var/log/odoo
sudo chown odoo /var/log/odoo

sudo su -c "~/odoo-11.0/odoo-bin -c /etc/odoo/odoo.conf" odoo
# sudo tail -f /var/log/odoo/odoo-prod.log
sudo su -c "~/odoo-11.0/odoo-bin -c /etc/odoo/odoo.conf --logfile=" odoo
