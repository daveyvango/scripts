import xml.etree.ElementTree as ET
import glob

class Report():
	
    def write_co_by_journals_only(self, delimiter):
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

    def combined_output(self, delimiter, pared_articles):
	"""
	Write journal copywrite information delimitted by a given character

	params:
	delimiter = a separating character such as "|" or "~".  Commas may be in titles - try to avoid
	articles  = dictionary of article information from Microsoft Academic
	"""
	
	# We keep around XML files to avoid calling SHERPA/RoMEO a lot.  There are limits to API calls
#        xml_files = glob.glob("journals_xml/*.xml")
        labels    = ['Article_ID', 'Article', 'Our_Authors', 'Number_of_Authors', 
	             'Fields_of_Study', 'Journal_ID', 'Journal_Short_Name',
		     'Journal_Title', 'Zetocpub', 'Romeopub',
                     'Publisher', 'Pre-archving', 'Post-Archiving', 
                     'PDF-Archvigin', 'Conditions']

        print delimiter.join(labels)
        #for xml_file in xml_files:
        for article in pared_articles:
             
            article_id         = article 
            article_name       = pared_articles[article]['display_name']
            authors_from_inst  = pared_articles[article]['authors_from_institution']
            authors_count      = pared_articles[article]['authors_count']
            fos                = pared_articles[article]['field_of_study']
            journal_id         = pared_articles[article]['journal_id']
            journal_short_name = pared_articles[article]['journal_short_name']

            tree = ET.parse('journals_xml/' + str(journal_id) + '.xml')
            root = tree.getroot()
	  
	    if root.find('journals') is not None: 
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
                        print delimiter.join([ str(article_id), article_name, authors_from_inst, 
					       str(authors_count), fos, str(journal_id), journal_short_name,
					       jtitle, zetocpub, romeopub, pub_name, pub_prearchiving, 
                                               pub_postarchiving, pub_pdfarchiving, conditions ])
	    else:
                print delimiter.join([ str(article_id), article_name, authors_from_inst, 
				       str(authors_count), fos, str(journal_id), journal_short_name,
				       'not found', 'not found', 'not found', 'not found', 'not found', 
                                       'not found', 'not found', 'not found' ])
       
