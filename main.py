import requests
import pymongo
from bs4 import BeautifulSoup
import time
import datetime
from cfg import config

# soup = BeautifulSoup(html_doc, 'html.parser')

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["crawler-db"]

def get_extension_type(content_typ):
    if 'text/html' in content_typ:
        return 'html'
    elif  'audio/aac' in content_typ:
        return 'aac'
    elif  'video/x-msvideo' in content_typ:
        return 'avi'
    elif  'image/bmp' in content_typ:
        return 'bmp'
    elif  'application/x-csh' in content_typ:
        return 'csh'
    elif  'text/css' in content_typ:
        return 'css'
    elif  'text/csv' in content_typ:
        return 'csv'
    elif  'application/msword' in content_typ:
        return 'doc'
    elif  'application/gzip' in content_typ:
        return 'gz'
    elif  'image/gif' in content_typ:
        return 'gif'
    elif  'image/jpeg' in content_typ:
        return 'jpeg'
    elif  'text/javascript' in content_typ:
        return 'js'
    elif  'application/json' in content_typ:
        return 'json'
    elif  'audio/mpeg' in content_typ:
        return 'mp3'
    elif  'video/mpeg' in content_typ:
        return 'mpeg'
    elif  'image/png' in content_typ:
        return 'png'
    elif  'application/pdf' in content_typ:
        return 'pdf'
    elif  'application/x-httpd-php' in content_typ:
        return 'php'
    elif  'application/vnd.ms-powerpoint' in content_typ:
        return 'ppt'
    elif  'application/x-sh' in content_typ:
        return 'sh'
    elif  'image/svg+xml':
        return 'svg'
    elif  'application/vnd.ms-excel' in content_typ:
        return 'xls'
    elif  'text/xml' in content_typ:
        return 'xml'
    elif  'application/zip' in content_typ:
        return 'zip'
    elif  'application/xhtml+xml' in content_typ:
        return 'xhtml'



def update_db(link1, list1):
    mydb.Links.update({"Link":link1},{"$set":list1})
    return 
def push_data_in_db(list1):
    mydb.Links.insert_one(list1)
    return 


while True:
    for doc in mydb.Links.find():
        if(mydb.Links.count()>=config['max-limit']):
            print("Maximum limit reached")
            break
        if doc["Last_Crawled_Dt"] is not None and doc["Last_Crawled_Dt"]<= time.time()-24*60*60*1000:
            print(Is_Crawled)
            continue
        try:
            url=doc["Link"]
            req= requests.get(url)
            content_typ = req.headers['content-type']
            file_path= "./files/" + str(doc["_id"]) + "." +get_extension_type(content_typ)
            list1={
                "Is_Crawled" : True,
                "Last_Crawled_Dt" : time.time(),
                "Response_Status" : req.status_code ,
                "Content_Length" : len(req.content),
                "Content_type" : get_extension_type(content_typ),
                "File_Path" :file_path
            }
            update_db(url, list1)    
            
            if req.status_code != 200:
                # mydb.Links.update({"Link":doc["Link"]},{"$set":{"Is_Crawled":True}})
                # print(doc)
                continue
            
            if 'text/html' not in content_typ:
                file= open(file_path, 'w')
                file.write(req.text)
                file.close()
                continue

            file= open(file_path, 'w')
            file.write(req.text)
            file.close()

            soup = BeautifulSoup(open(file_path), 'html.parser')
            for links in soup.find_all('a'):
                # print(links)
                href_link=links.get('href')
                if href_link is not None:
                    if 'http' in href_link and mydb.Links.find({"Link" : href_link}).count()==0:
                        list1 = {
                            "Link" : href_link ,
                            "Source_Link" : url,
                            "Is_Crawled" : False,
                            "Last_Crawled_Dt" : None,
                            "Response_Status" : 0,
                            "Content_type" : "",
                            "Content_Length" : 0,
                            "File_Path" : "",
                            "Created_At" : datetime.datetime.utcnow()

                        }
                        push_data_in_db(list1)
                    elif href_link[0]=="/" and mydb.Links.find({"Link" : url + href_link}).count()==0:
                        # print(url + href_link )
                        list1 = {
                            "Link" : url + href_link ,
                            "Source_Link" : url,
                            "Is_Crawled" : False,
                            "Last_Crawled_Dt" : None,
                            "Response_Status" : 0,
                            "Content_type" : "",
                            "Content_Length" : 0,
                            "File_Path" : "",
                            "Created_At" : datetime.datetime.utcnow()

                        }
                        push_data_in_db(list1)

                    # update_db(link1, list1)
        except:
            continue           
                
            
    
    time.sleep(config['sleep-time'])