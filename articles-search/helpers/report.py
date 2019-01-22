import xml.etree.ElementTree as ET
import glob

class Report():

    def write_delimitted(self, delimiter):

        delimiter = delimiter
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
            
                    #print jtitle + "|" + zetocpub + "|" + romeopub + "|" + pub_name + "|" + pub_prearchiving + "|" + pub_postarchiving + "|" + pub_pdfarchiving + "|" + conditions
                    print delimiter.join([ jtitle, zetocpub, romeopub, pub_name, pub_prearchiving, 
                                           pub_postarchiving, pub_pdfarchiving, conditions ])
       

# Example output from SHERPA/RoMEO
#  <journals>
#    <journal>
#      <jtitle>Journal of Drug Delivery Science and Technology</jtitle>
#      <issn>1773-2247</issn>
#      <zetocpub>Elsevier: 12 months</zetocpub>
#      <romeopub>Elsevier: 12 months</romeopub>
#    </journal>
#  </journals>
#
#  <publishers>
#    <publisher id="2823"  parentid="30">
#      <name>Elsevier</name>
#      <alias>12 months</alias>
#      <homeurl>http://www.elsevier.com/</homeurl>
#      <preprints>
#        <prearchiving>can</prearchiving>
#        <prerestrictions />
#      </preprints>
#      <postprints>
#        <postarchiving>can</postarchiving>
#        <postrestrictions />
#      </postprints>
#      <pdfversion>
#        <pdfarchiving>cannot</pdfarchiving>
#        <pdfrestrictions />
#      </pdfversion>
#      <conditions>
#        <condition>Authors pre-print on any website, including arXiv and RePEC</condition>
#        <condition>Author's post-print on author's personal website immediately</condition>
#        <condition>Author's post-print on open access repository after an embargo period of  &lt;num&gt;12&lt;/num&gt; &lt;period units=&quot;month&quot;&gt;months&lt;/period&gt;</condition>
#        <condition>Permitted deposit due to Funding Body, Institutional and Governmental policy or mandate, may be required to comply with embargo period of &lt;num&gt;12&lt;/num&gt; &lt;period units=&quot;month&quot;&gt;months&lt;/period&gt;</condition>
#        <condition>Author's post-print may be used to update arXiv and RepEC</condition>
#        <condition>Publisher's version/PDF cannot be used</condition>
#        <condition>Must link to publisher version with DOI</condition>
#        <condition>Author's post-print must be released with a Creative Commons Attribution Non-Commercial No Derivatives License</condition>
#      </conditions>
#      <mandates />
#      <paidaccess>
#        <paidaccessurl>http://www.elsevier.com/about/open-access/sponsored-articles</paidaccessurl>
#        <paidaccessname>Open Access</paidaccessname>
#        <paidaccessnotes>A paid open access option is available for this journal.</paidaccessnotes>
#      </paidaccess>
#      <copyrightlinks>
#        <copyrightlink>
#          <copyrightlinktext>Unleashing the power of academic sharing</copyrightlinktext>
#          <copyrightlinkurl>http://www.elsevier.com/connect/elsevier-updates-its-policies-perspectives-and-services-on-article-sharing</copyrightlinkurl>
#        </copyrightlink>
#        <copyrightlink>
#          <copyrightlinktext>Sharing Policy</copyrightlinktext>
#          <copyrightlinkurl>http://www.elsevier.com/about/company-information/policies/sharing</copyrightlinkurl>
#        </copyrightlink>
#        <copyrightlink>
#          <copyrightlinktext>Sharing and Hosting Policy FAQ</copyrightlinktext>
#          <copyrightlinkurl>https://www.elsevier.com/about/our-business/policies/sharing/policy-faq</copyrightlinkurl>
#        </copyrightlink>
#        <copyrightlink>
#          <copyrightlinktext>Green open access</copyrightlinktext>
#          <copyrightlinkurl>http://www.elsevier.com/about/open-access/green-open-access</copyrightlinkurl>
#        </copyrightlink>
#        <copyrightlink>
#         <copyrightlinktext>Journal Embargo Period List</copyrightlinktext>
#          <copyrightlinkurl>https://www.elsevier.com/__data/assets/pdf_file/0005/78476/external-embargo-list.pdf</copyrightlinkurl>
#        </copyrightlink>
#        <copyrightlink>
#          <copyrightlinktext>Journal Embargo List for UK Authors&lt;a/&gt; - &lt;a href=https://www.elsevier.com/about/our-business/policies/sharing/how-to-attach-a-user-license&gt;Attaching a User License</copyrightlinktext>
#          <copyrightlinkurl>https://www.elsevier.com/__data/assets/pdf_file/0011/78473/UK-embargo-periods.pdf</copyrightlinkurl>
#        </copyrightlink>
#        <copyrightlink>
#          <copyrightlinktext>Funding Body Agreements</copyrightlinktext>
#          <copyrightlinkurl>https://www.elsevier.com/about/open-science/open-access/agreements</copyrightlinkurl>
#        </copyrightlink>
#      </copyrightlinks>
#      <romeocolour>green</romeocolour>
#      <dateadded>2016-07-01 11:10:04</dateadded>
#      <dateupdated>2016-07-01 11:10:04</dateupdated>
#    </publisher>
#  </publishers>
#</romeoapi>

