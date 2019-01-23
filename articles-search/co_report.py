#!/usr/bin/env python
"""
Gather scholarly articles related to an institution and query copyright info

This type of information is especially useful in knowing which journals
are allowed to be shared within your institition.
"""

from helpers import journal, report, co

def main():
    """
    A direct call to main should be the primary entrypoint for this tool
    """

    # Our JournalData object will keep track of its own variables so
    # be sure to call these in order
    jd = journal.JournalData('northern illinois university')
    jd.pull_articles_from_net(2018, 5) # Get (year, count) articles from MS
    jd.pare_articles_data()	       # Parse out the journal IDs
    journals = jd.get_journal_names()  # Use the IDs to get the user-friendly display names

    # Use our journal names to get copyright info 
    co_info = co.Copyright(journals)
    co_info.query_co_by_journal_title()

    # Report in a nice format for our user
    co_report = report.Report()
    co_report.combined_output('|', jd.pared_articles)

if __name__ == "__main__":
    main()
