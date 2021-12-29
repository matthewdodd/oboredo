/*
This is for the first document of the sessionsPapers.
README for LOAD XML can be found here: https://dev.mysql.com/doc/refman/8.0/en/load-xml.html

Basic command is:

    LOAD XML
        [LOW_PRIORITY | CONCURRENT] [LOCAL]
        INFILE 'file_name'
        [REPLACE | IGNORE]
        INTO TABLE [db_name.]tbl_name
        [CHARACTER SET charset_name]
        [ROWS IDENTIFIED BY '<tagname>']
        [IGNORE number {LINES | ROWS}]
        [(field_name_or_user_var
            [, field_name_or_user_var] ...)]
        [SET col_name={expr | DEFAULT},
            [, col_name={expr | DEFAULT}] ...]

There is no need (ostensibly) for the SET command because the columns are named identically to the fields within the XML tags.
*/

LOAD XML LOCAL INFILE './OBO_XML_72/sessionsPapers/16740429.xml'
INTO TABLE oboredo.raw_div0
ROWS IDENTIFIED BY '<div0>';

-- Ignoring these for now; test and validate that the above command works.
/*
LOAD XML LOCAL INFILE './OBO_XML_72/sessionsPapers/16740429.xml'
INTO TABLE oboredo.raw_div1
ROWS IDENTIFIED BY '<div1>';

LOAD XML LOCAL INFILE './OBO_XML_72/sessionsPapers/16740429.xml'
INTO TABLE oboredo.raw_interp
ROWS IDENTIFIED BY '<interp>';

LOAD XML LOCAL INFILE './OBO_XML_72/sessionsPapers/16740429.xml'
INTO TABLE oboredo.raw_xptr
ROWS IDENTIFIED BY '<xptr>';

LOAD XML LOCAL INFILE './OBO_XML_72/sessionsPapers/16740429.xml'
INTO TABLE oboredo.raw_join
ROWS IDENTIFIED BY '<join>';

LOAD XML LOCAL INFILE './OBO_XML_72/sessionsPapers/16740429.xml'
INTO TABLE oboredo.raw_persName
ROWS IDENTIFIED BY '<persName>';

LOAD XML LOCAL INFILE './OBO_XML_72/sessionsPapers/16740429.xml'
INTO TABLE oboredo.raw_rs
ROWS IDENTIFIED BY '<rs>';
*/