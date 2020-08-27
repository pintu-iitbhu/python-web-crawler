# python-web-crawler
## A project hosted by Ananth SNC on behalf of [Flinkhub](https://flinkhub.com/).
This project is about building a spiderbot (web scraper) that continuously runs in the background and recursively scrapes all links it can find and store it in MongoDB database.

### Required Tools:

* Python 3 Interpreter – You can do this project using Python 3.7 or 3.8
* IDE / Code Editor – As per your choice
* Robo 3T – If you are using Mongo database
* MySQL Workbench – if you are using MySQL database

### Required Modules :

1. requests
2. beautifulsoup4
3. Any Database ORM / Connectors (like pymongo / sqlalchemy)
4. pymongo

### Installation :
You need to install the following modules.
* requests
```
pip3 install requests
```
* beautifulsoup4
```
pip3 install beautifulsoup4
```
* mongodb
```
sudo apt install -y mongodb
```
* To check the status of mongodb type the follwing command.
```
sudo systemctl status mongodb
```
* You can manage the MongoDB service using the systemctl command (e.g. sudo systemctl stop mongod , sudo systemctl start mongod ).
```
sudo systemctl start mongodb
```
* pymongo
```
python3 -m pip install pymongo
```

Follow the link to learn more:
[MongoDB Tutorial for Beginners](https://beginnersbook.com/2017/09/mongodb-tutorial/)
