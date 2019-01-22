import xml.etree.ElementTree as ET
import glob

class Report():
	
    def write_delimitted(self, delimiter):
	"""
	Write journal copywrite information delimitted by a given character

	params:
	delimiter = a separating character such as "|" or "~".  Commas may be in titles - try to avoid
	"""
	
	# We keep around XML files to avoid calling SHERPA/RoMEO a lot.  There are limits to API calls
        xml_files = glob.glob("journals_xml/*.xml")
        labels    = ['Title', 'Zetocpub', 'Romeopub',
                     'Publisher', 'Pre-archving', 'Post-Archiving', 
                     'PDF-Archvigin', 'Conditions']

        print delimiter.join(labels)
        for xml_file in xml_files:
        
            tree = ET.parse(xml_file)
            root = tree.getroot()
        
            for journal in root.find('journals'):
                jtitle   = journal.find('jtitle').text
                zetocpub = journal.find('zetocpub').text
                romeopub = journal.find('romeopub').text
            
                for publisher in root.find('publishers'):
                    conditions = ''
                    pub_name = publisher.find('name').text
                    pub_prearchiving  = publisher.find('preprints').find('prearchiving').text
                    pub_postarchiving = publisher.find('postprints').find('postarchiving').text
                    pub_pdfarchiving  = publisher.find('pdfversion').find('pdfarchiving').text
                    condition_count = 0
                    for condition in publisher.find('conditions'):
                        conditions = conditions + " <BREAK> " + condition.text
            
		    # Print report as we go
                    print delimiter.join([ jtitle, zetocpub, romeopub, pub_name, pub_prearchiving, 
                                           pub_postarchiving, pub_pdfarchiving, conditions ])
       
