# Organize copyright information

import requests
import xml.etree.ElementTree as ET
import glob

from pathlib import Path

class Copyright():

    def __init__(self, journals):
	self.journals = journals

    def query_co_by_journal_title(self):
	"""
	Get the copyright information from SHERPA/RoMEO
	We write the results to XML files basically as a cache.  There are limits on requests
	to the API and this data rarely changes.  We can also reduce memory usage on small VMs

	params:
	journals = a dictionary of journals containing ID, short name, and display name
        """
        for jid in self.journals:
	    print jid
            title_short = self.journals[jid]['journal_name'] 
	    title       = self.journals[jid]['journal_display_name']
            outfile     = 'journals_xml/' + jid + '.xml'
            file_check  = Path(outfile) 
            # Only create outfile for new info.  Save an API call
	    if file_check.is_file():
	        print "we already have " + str(jid)
	    else:
            	url_base    = 'http://www.sherpa.ac.uk/romeo/api29.php'
        
            	payload = { 'jtitle': title }
            	r       = requests.get( url_base, params=payload )
	
            	f = open(outfile, 'w')
            	f.write(r.text)

