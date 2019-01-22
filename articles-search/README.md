# Articles-search

Tools for gathering copyright information for Scholarly articles created by a specific institution.  Some publishers restrict access and distribution even to the author.  Sources include:
* [Microsoft Academic](https://academic.microsoft.com/) - Database full of metadata on scholarly articles
* [SHERPA/RoMEO](http://www.sherpa.ac.uk/romeo/index.php) - Copywrite information

We'll get info from MS Academic to feed into SHERPA/RoMEO to then produce a nice pipe-delimitted file for our customer.

**Note** By default, we are searching for "northern illinois university".  Update your code to change that.  I'm sure a command line option will show up on this project in the future though.
1. You will have to establish an [API Key](https://labs.cognitive.microsoft.com/en-us/project-academic-knowledge) to hit the MS Academic API
2. `export MS_ACADEMIC_KEY=*your API key*`
3. `python co_report.py`

