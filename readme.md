# WP Abstracts Author Block Extractor

This short and simple script takes an exported csv file containing the authors and company names from the WP Abstracts Wordpress Plugin and formats it into a text string that is suitable for including in a paper or for reporting.  
  
If two authors share the same company, it will only be output once after the final author from that company.
  
The output format:
- Author 1, Company A, Author 2, Company B
- Author 1, Author 2, Company A
  
If no company name is entered it will be skipped.
