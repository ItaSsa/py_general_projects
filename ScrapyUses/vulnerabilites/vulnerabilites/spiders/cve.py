'''
    Version 1 - scriping from a website - Notes:
    After:
        - Create project: scrapy startproject vulnerabilities
        - Go to new project directory
        - Create a spider: scrapy genspider cve cve.mitre.org
    To run the cve spider, in the terminal:  
    1. go to directory of the scrapy project 
        cd /home/itaira/proj_py/py_general_projects/ScrapyUses/vulnerabilities
    2. run scrapy crawl cve
    
    Version 2 - scraping local files - Notes:
        1. In the terminal make the download:  wget https://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html
        2. Use OS to get file
        Try to time and compare scraping times from website and localy: time scrapy crawl cve

    Version 3 - Saving scraping data as a csv file
    
    Version 4 - Saving scriping data as a json file 

    Vesion 5 - Persisting Sqlite 


'''
import scrapy
import os
import csv
import re
import json
import sqlite3

# Directory of the actual file
current_dir = os.path.dirname(__file__)
url = os.path.join(current_dir,'source-EXPLOIT-DB.html')

class CveSpider(scrapy.Spider):
    name = "cve"
    allowed_domains = ["cve.mitre.org"]
    start_urls = ["https://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html"]
    # start_urls = [f"file://{url}"]

            
    def parse(self, response):

        
        ####Version 5
        ##### sqlite config
        connection = sqlite3.connect('vulnb.db')
        table = 'CREATE TABLE vulns (exploit TEXT, cve TEXT)'
        cursor = connection.cursor()
        cursor.execute(table)
        connection.commit()
       

        #Identifying the interesting table
        for child in response.xpath('//table'):
            if len(child.xpath('tr'))>100:
                table = child
                break

        #Init variables
        count = 0

        ###Version 3
        ###csv_file = open('vulnerabilities.csv','w')

        ####Version 4
        ####data = {}
        ####json_file = open('vulnerabilities.json','w')
        
        #Getting the cells
        for row in table.xpath('//tr'):
            if count > 10: #only some records to save
                break
            try:
                exploit_id = row.xpath('td//text()')[0].extract()
                cve_id = row.xpath('td//text()')[2].extract()
                if re.match(r'^EXPLOIT', exploit_id, re.IGNORECASE):
                    ####Version 4
                    ####data[exploit_id] = cve_id

                    #####Version 5
                    cursor.execute('INSERT INTO vulns (exploit, cve) VALUES(?,?)', (exploit_id,cve_id))
                    connection.commit()

                    count +=1
            except IndexError:
                pass
        ###Version 3    
        ### csv_file.close()
        
        ####Version 4    
        ####Serializing json file          
        ####json.dump(data,json_file)
        ####json_file.close()