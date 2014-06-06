.. contents::

Introduction
============


MySQL Installation (OSX)
========================

.. code-block:: bash

    $ brew update
    $ brew install mysql55
    $ sudo ln -s /usr/local/Cellar/mysql55/5.5.x/bin/mysql /usr/local/bin/mysql
    $ sudo ln -s /usr/local/Cellar/mysql55/5.5.x/bin/mysqladmin /usr/local/bin/mysqladmin
    $ sudo ln -s /usr/local/Cellar/mysql55/5.5.x/bin/mysqlshow /usr/local/bin/mysqlshow
    $ sudo ln -s /usr/local/Cellar/mysql55/5.5.x/bin/mysql.server /usr/local/bin/mysql.server
    $ sudo ln -s /usr/local/Cellar/mysql55/5.5.x/bin/mysql_config /usr/local/bin/mysql_config

Start mysql
-----------

.. code-block:: bash

    $ mysql.server start

Securing mysql installation
---------------------------

.. code-block:: bash

    $ /usr/local/Cellar/mysql55/5.5.x/bin/mysql_secure_installation

Add local user
--------------

.. code-block:: bash

    $ mysql -u root -p -e "CREATE USER '`whoami`'@'localhost' IDENTIFIED BY '';"
    $ mysql -u root -p -e "GRANT ALL ON *.* TO '`whoami`'@'localhost';"


Create Pivot Database
=====================

.. code-block:: bash

    $ mysql -u root -p -e "CREATE DATABASE pivot;"
    $ mysql -u root -p -e "CREATE USER 'pivot'@'localhost' IDENTIFIED BY 'password';"
    $ mysql -u root -p -e "GRANT ALL ON pivot.* TO 'pivot'@'localhost';"
