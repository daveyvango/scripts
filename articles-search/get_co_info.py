import requests

journals_file = open('journals-2017-last.tsv')
journals_arr  = journals_file.read().split('\n')

for journal in journals_arr:
    jid, title_short, title = journal.split('|')
    print title
    outfile = jid + '.xml'
    url_base = 'http://www.sherpa.ac.uk/romeo/api29.php'

    payload = { 'jtitle': title }
    r = requests.get( url_base, params=payload )
    f = open('journals_xml/' + outfile, 'w')
    f.write(r.text)
    

#url_base = 'http://www.sherpa.ac.uk/romeo/api29.php'
#
#payload = { 'jtitle': 'Public Administration Review' }
#r = requests.get( url_base, params=payload )
#f = open('testfile.xml', 'w')
#f.write(r.text)
