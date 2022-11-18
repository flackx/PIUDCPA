import os
import requests
import mysql.connector

from datetime import datetime
from configparser import ConfigParser
print("----------")
print("Check if config file exists")
assert os.path.isfile("/home/s155/files/config.ini") == True
print("----------")
print("Config file exists ")
print("----------")

config = ConfigParser()
config.read('/home/s155/files/config.ini')


print("Checking if config has NASA related options")
assert config.has_option('nasa', 'api_key') == True
assert config.has_option('nasa', 'api_url') == True
print("OK")
print("----------")
print("Checking if it is possible to connect to MYSQL with the given config options")
mysql_config_mysql_host = config.get('mysql_config', 'mysql_host')
mysql_config_mysql_db = config.get('mysql_config', 'mysql_db')
mysql_config_mysql_user = config.get('mysql_config', 'mysql_user')
mysql_config_mysql_pass = config.get('mysql_config', 'mysql_pass')
connection = mysql.connector.connect(host=mysql_config_mysql_host, database=mysql_config_mysql_db, user=mysql_config_mysql_user, password=mysql_config_mysql_pass)
assert connection.is_connected() == True
print("OK")
print("----------")


print("Checking if config has TWITTER related options")
assert config.has_option('twitter', 'consumer_key') == True
assert config.has_option('twitter', 'consumer_secret') == True
assert config.has_option('twitter', 'access_token') == True
assert config.has_option('twitter', 'access_token_secret') == True
print("OK")
print("----------")