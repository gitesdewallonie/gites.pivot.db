.. contents::

Introduction
============


MySQL Installation (OSX)
========================
brew update
brew install mysql55
sudo ln -s /usr/local/Cellar/mysql55/5.5.x/bin/mysql /usr/local/bin/mysql
sudo ln -s /usr/local/Cellar/mysql55/5.5.x/bin/mysql.server /usr/local/bin/mysql.server

start mysql
-----------
mysql.server start

securing mysql installation
---------------------------
/usr/local/Cellar/mysql55/5.5.x/bin/mysql_secure_installation
