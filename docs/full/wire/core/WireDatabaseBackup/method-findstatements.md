# WireDatabaseBackup::findStatements()

Source: `wire/core/WireDatabaseBackup.php`

Returns array of all create table statements, indexed by table name

@param string $filename to extract all CREATE TABLE statements from

@param string $regex Regex (PCRE) to match for statement to be returned, must stuff table name into first match

@param bool $multi Whether there can be multiple matches per table

@return array of statements, indexed by table name. If $multi is true, it will be array of arrays.

@throws \Exception if unable to open specified file
