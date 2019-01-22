# Gather scholarly articles that are related to our university using
# Microsoft Academic API

import json
import requests
import time
import os

def main():
    print "This module is not intended to be called directly at this time"
    exit

class JournalData():
    
    def __init__(self):   
        self.publisher_ids = {}
        self.articles = {}

    def import_known_journals(self, file_name):
        articles_file = open(file_name)
        articles_str  = articles_file.read()

        self.articles      = json.loads(articles_str)

    def gather_publisher_ids(self):
        for article in self.articles['entities']:
            if 'J' in article:
	        authors = ''
	        fos     = ''
                for author in article['AA']:
                    if 'AfN' in author:
		        if author['AfN'] == 'northern illinois university':
	                    authors = authors + " " + author['AuN'] + "(" + author['AfN'] + ")"
                if 'F' in article:
                    for field_of_study in article['F']:
                        fos = fos + field_of_study['FN'] + ", "
        
                #print(article['DN'] + "|" + authors + "|" + fos + "|" + str(article['J']['JId']) + "|" + article['J']['JN'])
                self.publisher_ids[str(article['J']['JId'])] = '1'

        print "There are " + str(len(self.publisher_ids)) + " unique publishers"

    def get_publisher_names(self):
        publishers = {}
        publisher_ids = self.publisher_ids
        query = 'Or('

        for publisher in publisher_ids:
            # Sleep in between as to keep rate limit low and avoid API costs
            time.sleep(1)
            url         = 'https://api.labs.cognitive.microsoft.com/academic/v1.0/evaluate?expr=Id=' + publisher + '&model=latest&count=10&offset=0&attributes=Id,DJN,JN'
            query       = query + "Id=" + publisher + ","
            headers     = {'Ocp-Apim-Subscription-Key': os.environ['MS_ACADEMIC_KEY']}
            r           = requests.get( url, headers=headers )
            pub_details = r.json()
            if 'entities' in pub_details:
                for publisher in pub_details['entities']:
                    #print str(publisher['Id']) + "|" + publisher['JN'] + "|" + publisher['DJN']
                    publishers[str(publisher['Id'])] = {}
                    publishers[str(publisher['Id'])]['journal_display_name'] = publisher['DJN'] 
                    publishers[str(publisher['Id'])]['journal_name']         = publisher['JN']
            else:
                print pub_details

        return publishers
        
#print query
#
#url = 'https://api.labs.cognitive.microsoft.com/academic/v1.0/evaluate?expr=Id=' + publisher + '&model=latest&count=10&offset=0&attributes=Id,DJN,JN'
#headers = {'Ocp-Apim-Subscription-Key': 'e32c2067223844f7bcd373114673cfd0'}
#print url
#r = requests.get( url, headers=headers )
#pub_details = r.json()

if __name__ == "__main__":
    main()
