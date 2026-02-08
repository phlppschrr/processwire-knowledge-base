# WireDatabasePDO::queryLog()

Source: `wire/core/WireDatabasePDO.php`

Log a query, start/stop query logging, or return logged queries

- To log a query, provide the $sql argument containing the query (string).
- To retrieve the query log, call this method with no arguments.
- Note the core only populates the query log when `$config->debug` mode is active.
- Specify boolean true for $sql argument to reset and start query logging (3.0.173+)
- Specify boolean false for $sql argument to stop query logging (3.0.173+)


@param string|bool $sql Query (string) to log, boolean true to reset/start query logging, boolean false to stop query logging

@param string $note Any additional debugging notes about the query

@return array|bool Returns query log array, boolean true on success, boolean false if not
