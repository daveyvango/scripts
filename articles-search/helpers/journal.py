# Gather scholarly articles that are related to our university using
# Microsoft Academic API

import json
import requests
import datetime
import time
import os

# This is a helper, not a main
def main():
    print "This module is not intended to be called directly at this time"
    exit

class JournalData():
    """
    Keep track of articles and journal information
    """
    
    def __init__(self, institution):   
	self.institution    = institution
        self.pared_articles = {}
        self.journal_ids    = {}
        self.articles       = {}
	# This key needs to be established with Microsoft
        self.api_key     = os.environ['MS_ACADEMIC_KEY']
 

    def pull_articles_from_net(self, year=datetime.datetime.now().year, count=10):
	"""
	Create GET request for pulling available data from Microsoft Academic
	
	params:
	year  = year to search
	count = number of records to return
	"""
	
	# build up the URL for the API call
        url = 'https://api.labs.cognitive.microsoft.com/academic/v1.0/evaluate'	
        url = url + '?expr=And(Y=' + str(year) + ',Composite(AA.AfN=\'' + self.institution + '\'))'
        url = url + '&model=latest&count=' + str(count) + '&offset=0&attributes=Id,AA.AfN,AA.AuN,J.JN,J.JId,E.DN'

	# We need to establish credentials with Microsoft ahead of time
        headers       = {'Ocp-Apim-Subscription-Key': self.api_key }
        r             = requests.get( url, headers=headers )
        journals      = r.json()
	self.articles = journals

    def pare_articles_data(self):
	"""
	Parse out journal ids from the journals object.  We'll have to query by the ids to get good Journal names
	Double check the author's affiliation to ensure it matches your institution
	"""
	
	# We'll end up removing other authors from our articles to just reduce dictionary size
	article_id     = 0
        for article in self.articles['entities']:
            article_id = article_id + 1
	    print str(article_id) + " " + article['DN']
            if 'J' in article:
	        authors_count = 0
	        authors       = ''
	        fos           = ''
                for author in article['AA']:
		    authors_count = authors_count + 1
                    if 'AfN' in author:
		        if author['AfN'] == self.institution:
	                    authors = authors + " " + author['AuN'] + "(" + author['AfN'] + ")"
                if 'F' in article:
                    for field_of_study in article['F']:
                        fos = fos + field_of_study['FN'] + ", "
        
		# build up a smaller articles dictionary
	        self.pared_articles[str(article_id)] = {}
	        self.pared_articles[str(article_id)] = { 'display_name': article['DN'], 
							 'authors_from_institution': authors, 
							 'field_of_study': fos, 
							 'authors_count': authors_count, 
							 'journal_id': article['J']['JId'],
							 'journal_short_name': article['J']['JN']}

                self.journal_ids[str(article['J']['JId'])] = '1'

        print "There are " + str(len(self.journal_ids)) + " unique journals."

    def get_journal_names(self):
	"""
	Get full names of Journal based on their ID
	"""
        journals = {}
        journal_ids = self.journal_ids

        for journal in journal_ids:
            # Sleep in between as to keep rate limit low and avoid API costs
            time.sleep(1)
            url         = 'https://api.labs.cognitive.microsoft.com/academic/v1.0/evaluate?expr=Id=' + journal + '&model=latest&offset=0&attributes=Id,DJN,JN'
            headers     = {'Ocp-Apim-Subscription-Key': self.api_key }
            r           = requests.get( url, headers=headers )
            pub_details = r.json()
            if 'entities' in pub_details:
                for journal in pub_details['entities']:
                    journals[str(journal['Id'])] = {}
                    journals[str(journal['Id'])]['journal_display_name'] = journal['DJN'] 
                    journals[str(journal['Id'])]['journal_name']         = journal['JN']
                    journals[str(journal['Id'])]['id']                   = str(journal['Id'])
            else:
                print pub_details

        return journals

if __name__ == "__main__":
    main()
