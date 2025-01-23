/*
To insure tha it will work:
    > Enable local infile on server side:
        edite /etc/mysql/my.cnf by including:
            local_infile=1
    > Run the command before:
        SET GLOBAL local_infile = 1;
*/

LOAD DATA LOCAL INFILE '/home/itaira/proj_py/py_general_projects/Scripting_with_Python_and_SQL_for_Data_Engineering/integratingMySQl/ratings.csv' INTO TABLE ratings
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'
(@name,@region,@rating) set name=@name,rating=@rating,region=@region;
