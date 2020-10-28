# Created by Andy McDonald
# Repo: https://github.com/andymcdgeo/WPAbstract_NameCompanyExtractor

import csv
import os.path

# Change the input file name here
input_file = 'Data/dummy_abstracts_export.csv'

# Check if an output file exists, if so append a number to it
i = 0
while os.path.exists('output%s.txt' % i):
    i += 1


with open(input_file, 'r', newline='', encoding="utf8") as abstracts:
    contents = csv.reader(abstracts)
    for row in contents:
        submission = row[0]

        # Strip trailing and leading whitespace from the names and companies/affiliations
        names = [name.strip(' ') for name in row[1].split('|')]
        companies = [company.strip(' ') for company in row[2].split('|')]

        author_list = []
        for index, person in enumerate(names):
            
            if len(names) == len(companies):
                author_list.append(names[index])
                current_company = companies[index]

                # Single Author Papers
                if len(names) == 1:
                    author_list.append(current_company)
                    continue
                
                # Append the current company if we have reached the end of the authors
                if len(names) == index +1:
                    author_list.append(current_company)
                    continue
                
                # Check if the current company matches the next one
                if current_company != companies[index + 1]:
                    author_list.append(current_company)
                else:
                    continue

            else:
                author_list.append(names[index])
                author_list.append(companies[0])
        paper_authors = ', '.join(author_list)

        # Remove any backslashes \ that may occur
        paper_authors = paper_authors.replace('\\', '')
        print(paper_authors)
        print(f'Paper: {submission} has {len(names)} Authors')

        with open('output%s.txt' % i, "a+", encoding='utf8') as f:
            f.write(paper_authors + '\n')

