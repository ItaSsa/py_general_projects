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

    Version 3 - Saving scraping data as a csv file - Notes:
        1. import csv module
        2. Creating a csv file 
        3. Using writerow to write rows
'''
import scrapy
import os
import csv
import re
# Directory of the actual file
current_dir = os.path.dirname(__file__)
url = os.path.join(current_dir,'source-EXPLOIT-DB.html')

class CveSpider(scrapy.Spider):
    name = "cve"
    allowed_domains = ["cve.mitre.org"]
    # start_urls = ["https://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html"]
    start_urls = [f"file://{url}"]

    def parse(self, response):
        #Identifying the interesting table
        for child in response.xpath('//table'):
            if len(child.xpath('tr'))>100:
                table = child
                break
        
        #creating a csv file
        csv_file = open('vulnerabilities.csv','w')
        writer = csv.writer(csv_file)
        #wrintng head lable
        writer.writerow(['exploit_id','cve_id'])

        
        #Getting the cells
        count =0
        for row in table.xpath('//tr'):
            if count > 100: #only some records to save
                break
            print(url)#test
            try:
                exploit_id = row.xpath('td//text()')[0].extract()
                cve_id = row.xpath('td//text()')[2].extract()
                if re.match(r'^EXPLOIT', exploit_id, re.IGNORECASE):
                    # writting row
                    writer.writerow([exploit_id,cve_id])
                    count +=1
            except IndexError:
                pass
