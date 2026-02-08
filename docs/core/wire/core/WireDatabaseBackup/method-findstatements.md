# $wireDatabaseBackup->findStatements($filename, $regex, $multi = true): array

Source: `wire/core/WireDatabaseBackup.php`

Returns array of all create table statements, indexed by table name

## Arguments

- `$filename` `string` to extract all CREATE TABLE statements from
- `$regex` `string` Regex (PCRE) to match for statement to be returned, must stuff table name into first match
- `$multi` (optional) `bool` Whether there can be multiple matches per table

## Return value

array of statements, indexed by table name. If $multi is true, it will be array of arrays.

## Throws

- \Exception if unable to open specified file
