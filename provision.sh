#!/bin/sh

if [ ! -e "/home/vagrant/provisioned" ]
then
    echo "set grub-pc/install_devices /dev/sda" | debconf-communicate
    apt-get update
    apt-get -y upgrade
    apt-get -y install supervisor git python3 python3-dev python3-setuptools python3-pip python-virtualenv mysql-client

    # Mysql install
    echo 'mysql-server mysql-server/root_password password releasenotes' | debconf-set-selections
    echo 'mysql-server mysql-server/root_password_again password releasenotes' | debconf-set-selections
    apt-get install -y mysql-server-5.7 > /dev/null 2>&1

    # Mysql setup
    mysqladmin -uroot -preleasenotes create releasenotes || exit 1
    mysql -uroot -preleasenotes -Bse "create user 'releasenotes'@'localhost' identified by 'releasenotes';"
    mysql -uroot -preleasenotes -Bse "grant all privileges on \`releasenotes\`.* to 'releasenotes'@'localhost';"
    mysqladmin -uroot -preleasenotes flush-privileges || exit 1

    # Install the virtualenv in ~vagrant but the project in /vagrant.
    sudo -u vagrant -s -H -- <<EOF
virtualenv -p /usr/bin/python3.5 /home/vagrant/env
source /home/vagrant/env/bin/activate
cd /vagrant/
/home/vagrant/env/bin/pip install -r requirements.txt
EOF

    cat <<'EOF' > /etc/supervisor/conf.d/runserver.conf
[program:runserver]
command=/home/vagrant/env/bin/python manage.py runserver 0.0.0.0:8000
directory=/vagrant/releasenotes_project
autostart=0
EOF
    # Fix supervisor in ubuntu 16.04 (FFS)
    systemctl enable supervisor
    systemctl start supervisor
    supervisorctl reload

    touch /home/vagrant/provisioned
fi

supervisorctl start runserver
