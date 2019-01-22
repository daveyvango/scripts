from helpers import journal, report, co

def main():
    """
    A direct call to main should be the main entrypoint for this tool
    """
    
    jd = journal.JournalData()
    jd.import_known_journals('all-papers-2018-with-field-of-study.json')
    jd.gather_publisher_ids()
    publishers = jd.get_publisher_names()

    print publishers
    co_info = co.Copyright()
    co_info.query_by_journal_title()

    co_report = report.Report()
    co_report.write_delimitted('|')

if __name__ == "__main__":
    main()
