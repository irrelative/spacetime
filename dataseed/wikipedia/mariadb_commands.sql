
// Make a db
create database geo;

// make index table
create table wiki_index (
    page_id integer not null primary key,
    title varchar(1000)
);
// silly mysql.... utf8 support is bad
alter table wiki_index MODIFY COLUMN title varchar(1000) CHARACTER SET utf8mb4;

// clean index data, see python script

// Load data
LOAD DATA INFILE '/Users/justin/Downloads/wiki_index.csv' INTO TABLE wiki_index CHARACTER SET utf8mb4 FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '"' LINES TERMINATED BY '\r\n'
// add index
create index wiki_index_page_id_idx on wiki_index(page_id);

// make csv from data
// eg, cities:
select wiki_index.title,geo_tags.gt_lat, geo_tags.gt_lon from geo_tags join wiki_index on geo_tags.gt_page_id = wiki_index.page_id where geo_tags.gt_type = 'city'
INTO OUTFILE '/tmp/cities.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

// load back into postgres
create temporary table geot (title text, lat decimal(11,8), lon decimal(11,8));
copy geot (title, lat, lon) from '/tmp/cities.csv' with (format csv);
// note magic 4326
insert into stweb_location (name, point) select title, ST_SetSRID(ST_MakePoint(lat, lon), 4326) from geot;
