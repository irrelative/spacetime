


// Make a db
create database geo;

// make index table
create table wiki_index (
    page_id integer not null primary key,
    title varchar(1000)
);
// silly mysql.... utf8 support is bad
alter table wiki_index MODIFY COLUMN title varchar(1000) CHARACTER SET utf8mb4;


// clean index data
import csv, sys
writer = csv.writer(sys.stdout, quoting=csv.QUOTE_ALL)
with open('/Users/justin/Downloads/enwiki-20171103-pages-articles-multistream-index.txt') as f:
    for line in f:
        writer.writerow(line.strip().split(':', 2)[1:])


// Load data
LOAD DATA INFILE '/Users/justin/Downloads/wiki_index.csv' INTO TABLE wiki_index CHARACTER SET utf8mb4 FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '"' LINES TERMINATED BY '\r\n'
