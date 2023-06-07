import yaml
import bibtexparser

'''
In this script directory, run the following command to generate the YAML file:
python3 -m venv ./
source bin/activate
pip install bibtexparser
pip install pyyaml
python publication_generator.py
'''

# Function to read a bib file and return its entries
def read_bib_file(filename):
    with open(filename) as bibtex_file:
        bibtex_str = bibtex_file.read()
    bib_database = bibtexparser.loads(bibtex_str)
    return bib_database.entries

# Read the entries from the bib files
journal_entries = read_bib_file('../_data/bibtex/journal.bib')
conference_entries = read_bib_file('../_data/bibtex/conference.bib')
dissertation_entries = read_bib_file('../_data/bibtex/dissertation.bib')
poster_entries = read_bib_file('../_data/bibtex/poster.bib')
extended_abstract_entries = read_bib_file('../_data/bibtex/extended_abstract.bib')
software_entries = read_bib_file('../_data/bibtex/software_release.bib')
technical_report_entries = read_bib_file('../_data/bibtex/technical_report.bib')
workshop_entries = read_bib_file('../_data/bibtex/workshop.bib')
chapter_entries = read_bib_file('../_data/bibtex/chapter.bib')
book_entries = read_bib_file('../_data/bibtex/book.bib')
patent_entries = read_bib_file('../_data/bibtex/patent.bib')
other_entries = read_bib_file('../_data/bibtex/otherpub.bib')

# Create the data structure for the YAML file
data = {
    'publications': [
        {'pub_type': 'Journal Papers', 'entries': journal_entries},
        {'pub_type': 'Conference Papers', 'entries': conference_entries},
        # {'pub_type': 'Workshop Papers', 'entries': workshop_entries},
        # {'pub_type': 'Book Chapters', 'entries': chapter_entries},
        # {'pub_type': 'Books', 'entries': book_entries},
        # {'pub_type': 'Patents', 'entries': patent_entries},
        # {'pub_type': 'Technical Reports', 'entries': technical_report_entries},
        {'pub_type': 'Software Releases', 'entries': software_entries},
        {'pub_type': 'Thesis and Dissertation', 'entries': dissertation_entries},
        {'pub_type': 'Extended Abstracts', 'entries': extended_abstract_entries},
        {'pub_type': 'Posters', 'entries': poster_entries},
        # {'pub_type': 'Other', 'entries': other_entries}
    ]
}

# Write the data structure to the YAML file
with open('../_data/publications.yml', 'w') as yaml_file:
    yaml.dump(data, yaml_file)