import requests

class Copyright():

    def __init__(self):
	self.journals = {}

    def query_co_by_journal_title(self, journals):
        for jid in journals:
	    print jid
            title_short = journals[jid]['journal_name'] 
	    title       = journals[jid]['journal_display_name']
            outfile     = jid + '.xml'
            url_base    = 'http://www.sherpa.ac.uk/romeo/api29.php'
        
            payload = { 'jtitle': title }
            r       = requests.get( url_base, params=payload )

            f = open('journals_xml/' + outfile, 'w')
            f.write(r.text)
