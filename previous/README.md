# OBO Redo

This is a reattempt to perform the data work from my Master's Thesis _The Empire of the Old Bailey Online: The Power of Zero_.

## Prerequisites
You will need the following tools/software, with the versions being used in this project contained in parentheses:

1. Git (2.16.2.windows.1)
2. MySQL (8.0.18)
3. Python (3.8.0)

## Getting Started

1. You can either download all of the data yourself from the [University of Sheffield online repository](http://dx.doi.org/10.15131/shef.data.4775434) or you can run a git clone:
```bash
git clone https://github.com/matthewdodd/oboredo.git
```
2. You will also need to pre-create the MySQL database and tables to house the XML data:
```sql
CREATE DATABASE oboredo CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;

CREATE TABLE oboredo.raw_div0(type varchar(60) COMMENT 'source of documents'
                             ,id varchar(60) COMMENT 'unique source identifier')
COMMENT 'single file unique document identification table';

CREATE TABLE oboredo.raw_div1(type varchar(60) COMMENT 'source of documents'
                             ,id varchar(60) COMMENT 'unique source identifier')
COMMENT 'single case, sessionPaper, ordinaryAccount unique document identification table';

CREATE TABLE oboredo.raw_interp(inst varchar(60) COMMENT 'unique interp identifier; shared with raw_div1.id'
                               ,type varchar(60) COMMENT 'kind of interp record'
                               ,value varchar(4000) COMMENT 'description of the type of interp record')
COMMENT 'primary table for base information of div1';

CREATE TABLE oboredo.raw_xptr(type varchar(60) COMMENT 'kind of external document'
                             ,doc varchar(60) COMMENT 'unique external document referential identifier')
COMMENT 'external pointers for documents contained with OBO';

CREATE TABLE oboredo.raw_join(result varchar(60) COMMENT 'kind of connection between targets'
                             ,id varchar(60) COMMENT 'unique join identifier'
                             ,targOrder varchar(1) COMMENT 'if targets are ordered; Y/N'
                             ,targets varchar(4000) COMMENT 'connected raw_interp.inst; latter id is result of former id')
COMMENT 'joining referential ids across all other tables';

CREATE TABLE oboredo.raw_persName(id varchar(60) COMMENT 'unique persName identifier'
                                 ,type varchar(60) COMMENT 'kind of person being referenced')
COMMENT 'all individuals and their type';

CREATE TABLE oboredo.raw_rs(id varchar(60) COMMENT 'unique rs identifiers'
                           ,type varchar(60) COMMENT 'label applied to the id')
COMMENT 'referencing strings';
```
3. When installing Python, if using Windows, make sure that teh location Python installs in is this:
```bash
<<<<<<< Updated upstream
C:\Python
=======
pip install wheel

pip install mysql-connector-python-rf
>>>>>>> Stashed changes
```

4. You will need to install the  MySQL connector Python module to make this all work:
```bash
pip install mysql-connector-python-rf
```

## Contributing
Pull requests are acceptable. It is presumed, however, that you will be forking this repository to validate any work I have performed. Should you wish to contribute to this repository, you are welcome to.

## License
Please see the [LICENSE.md](./LICENSE.md)