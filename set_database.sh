#!/bin/sh

source ${HOME}/.profile

mysql --user=${LOCAL_MYSQL_USER} --password=${LOCAL_MYSQL_PASS} --execute="DROP DATABASE MIMICIV; CREATE DATABASE MIMICIV;"
mysql --user=${LOCAL_MYSQL_USER} --password=${LOCAL_MYSQL_PASS} < create_emar_detail.sql
${HOME}/anaconda3/bin/python csv2mysql.py
