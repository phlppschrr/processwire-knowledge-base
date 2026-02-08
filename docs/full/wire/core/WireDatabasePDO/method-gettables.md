# WireDatabasePDO::getTables()

Source: `wire/core/WireDatabasePDO.php`

Get array of all tables in this database.

Note that this method caches its result unless you specify boolean false for the $allowCache argument.


@param bool $allowCache Specify false if you don't want result to be cached or pulled from cache (default=true)

@return array Returns array of table names
