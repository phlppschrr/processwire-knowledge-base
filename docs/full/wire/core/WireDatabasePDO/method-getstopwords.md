# WireDatabasePDO::getStopwords()

Source: `wire/core/WireDatabasePDO.php`

Get all fulltext stopwords for database engine


@param string $engine Specify DB engine of "myisam" or "innodb" or omit for current DB engine

@param bool $flip Return flipped array where stopwords are array keys rather than values? for isset() use (default=false)

@return array
