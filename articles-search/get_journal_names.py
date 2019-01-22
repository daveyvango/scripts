# Gather scholarly articles that are related to our university using
# Microsoft Academic API

import json
import requests
import time
import os

#articles_file = open('allpapers-2017-with-field-of-study.json')
articles_file = open('all-papers-2018-with-field-of-study.json')
articles_str  = articles_file.read()
articles      = json.loads(articles_str)

publisher_ids = {}

for article in articles['entities']:
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

        print(article['DN'] + "|" + authors + "|" + fos + "|" + str(article['J']['JId']) + "|" + article['J']['JN'])
        publisher_ids[str(article['J']['JId'])] = '1'
    #else:
    #    print("BOOK:    " + article['DN'])

print len(publisher_ids)

query = 'Or('
for publisher in publisher_ids:
    time.sleep(1)
    url         = 'https://api.labs.cognitive.microsoft.com/academic/v1.0/evaluate?expr=Id=' + publisher + '&model=latest&count=10&offset=0&attributes=Id,DJN,JN'
    query       = query + "Id=" + publisher + ","
    headers     = {'Ocp-Apim-Subscription-Key': os.environ['MS_ACADEMIC_KEY']}
    r           = requests.get( url, headers=headers )
    pub_details = r.json()
    if 'entities' in pub_details:
        for publisher in pub_details['entities']:
            print str(publisher['Id']) + "|" + publisher['JN'] + "|" + publisher['DJN']
    else:
        print pub_details

query = query + ")"
#print query
#
#url = 'https://api.labs.cognitive.microsoft.com/academic/v1.0/evaluate?expr=Id=' + publisher + '&model=latest&count=10&offset=0&attributes=Id,DJN,JN'
#headers = {'Ocp-Apim-Subscription-Key': 'e32c2067223844f7bcd373114673cfd0'}
#print url
#r = requests.get( url, headers=headers )
#pub_details = r.json()
