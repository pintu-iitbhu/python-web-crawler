# python-web-crawler
## A project hosted by Ananth SNC on behalf of Flinkhub.
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

```
pip3 install requests
pip3 install beautifulsoup4
sudo apt install -y mongodb
sudo systemctl status mongodb
sudo systemctl start mongodb
mongo
python3 -m pip install pymongo
```
