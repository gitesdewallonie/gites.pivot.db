.. contents::

Introduction
============


MySQL Installation (OSX)
========================

.. code-block:: bash

    $ brew update
    $ brew install mysql55
    $ sudo ln -s /usr/local/Cellar/mysql55/5.5.x/bin/mysql /usr/local/bin/mysql
    $ sudo ln -s /usr/local/Cellar/mysql55/5.5.x/bin/mysql.server /usr/local/bin/mysql.server

start mysql
-----------

.. code-block:: bash

    $ mysql.server start

securing mysql installation
---------------------------

.. code-block:: bash

    $ /usr/local/Cellar/mysql55/5.5.x/bin/mysql_secure_installation

Pivot Database
==============

create pivot database
---------------------

.. code-block:: bash

    $ mysql -u root -p

.. code-block:: sql

    mysql> CREATE DATABASE pivot;
    Query OK, 1 row affected (0.00 sec)

    mysql> CREATE USER 'pivot'@'localhost' IDENTIFIED BY 'password';
    Query OK, 0 rows affected (0.00 sec)

    mysql> GRANT ALL ON pivot.* TO 'pivot'@'localhost';
    Query OK, 0 rows affected (0.00 sec)
