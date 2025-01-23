(SELECT 'name','rating','region' )
UNION
    SELECT * FROM ratings
INTO OUTFILE 'output.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'

