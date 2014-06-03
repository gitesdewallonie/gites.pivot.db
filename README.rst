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


