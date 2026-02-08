# $wireDatabasePDO->getTables($allowCache = true): array

Source: `wire/core/WireDatabasePDO.php`

Get array of all tables in this database.

Note that this method caches its result unless you specify boolean false for the $allowCache argument.

## Arguments

- `$allowCache` (optional) `bool` Specify false if you don't want result to be cached or pulled from cache (default=true)

## Return value

array Returns array of table names
