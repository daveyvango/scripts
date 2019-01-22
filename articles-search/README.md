# Articles-search

Tools for gathering copyright information for Scholarly articles created by a specific institution.  Some publishers restrict access and distribution even to the author.  Sources include:
* [Microsoft Academic](https://academic.microsoft.com/) - Database full of metadata on scholarly articles
* [SHERPA/RoMEO](http://www.sherpa.ac.uk/romeo/index.php) - Copywrite information

We'll get info from MS Academic to feed into SHERPA/RoMEO to then produce a nice CSV for our customer.

**WARNING** This current process is pretty hacky, hard-coded, inefficient, buggy, and more.  It needs refinement and consolidation, but here are the manual steps in the meantime:
1. Use [Microsoft Cognitive Labs API Page](https://dev.labs.cognitive.microsoft.com) to gather relevant documents and toss them into a file.
2. Use that filename inside of `get_journal_name.py` to get journal ID, Name, and Display Name
3. Taking the output from the previos step, run `get_co_info.py` to gather copyright info from SHERAP/RoMEO
4. Finally, get the XML output from the SHERPA/RoMEO API to provide a CSV to our customer with `publishers_to_csv.py`.

Gross, right?  It's a work in progress.  Let's try getting this thing more properly developed.
