# OBO Redo

This is a reattempt to perform the data work from my Master's Thesis _The Empire of the Old Bailey Online: The Power of Zero_.

## Prerequisites

1. Git
2. MySQL

## Getting Started

1. You can either download all of the data yourself from the [University of Sheffield online repository](http://dx.doi.org/10.15131/shef.data.4775434) or you can run a git clone:
```bash
git clone https://github.com/matthewdodd/oboredo.git
```
2. You will also need to pre-create the MySQL database and tables to house the XML data:
```sql
CREATE DATABASE oboredo CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;

CREATE TABLE oboredo.raw_div0(type varchar(60), id varchar(60));

CREATE TABLE oboredo.raw_div1(type varchar(60), id varchar(60));

CREATE TABLE oboredo.raw_interp(inst varchar(60), type varchar(60), value varchar(4000));

CREATE TABLE oboredo.raw_xptr(type varchar(60), doc varchar(60));

CREATE TABLE oboredo.raw_join(result varchar(60), id varchar(60), targOrder varchar(1), targets varchar(4000));

CREATE TABLE oboredo.raw_persName(id varchar(60), type varchar(60));

CREATE TABLE oboredo.raw_rs(id varchar(60), type varchar(60));
```

## Contributing
Pull requests are acceptable. It is presumed, however, that you will be forking this repository to validate any work I have performed. Should you wish to contribute to this repository, you are welcome to.

## License
Please see the [LICENSE.md](./LICENSE.md)