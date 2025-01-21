import scrapy
'''
    After:
        - Create project: scrapy startproject vulnerabilities
        - Go to new project directory
        - Create a spider: scrapy genspider cve cve.mitre.org
    To run the cve spider, in the terminal:  
    1. go to directory of the scrapy project 
        cd /home/itaira/proj_py/py_general_projects/ScrapyUses/vulnerabilities
    2. run scrapy crawl cve
    
'''

class CveSpider(scrapy.Spider):
    name = "cve"
    allowed_domains = ["cve.mitre.org"]
    start_urls = ["https://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html"]

    def parse(self, response):
        #Identifying the interesting table
        for child in response.xpath('//table'):
            if len(child.xpath('tr'))>100:
                table = child
                break

        #Getting the cells
        for row in table.xpath('//tr'):
            try:
                print(row.xpath('td//text()')[0].extract())
            except IndexError:
                pass
