from helpers import journal, report, co

def main():
    """
    A direct call to main should be the main entrypoint for this tool
    """
    
    jd = journal.JournalData('northern illinois university')
    jd.pull_articles_from_net()
    jd.gather_journal_ids()
    journals = jd.get_journal_names()

    print journals
    co_info = co.Copyright()
    co_info.query_co_by_journal_title(journals)

    co_report = report.Report()
    co_report.write_delimitted('|')

if __name__ == "__main__":
    main()
