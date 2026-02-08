# $wireDatabasePDO->getStopwords($engine = '', $flip = false): array

Source: `wire/core/WireDatabasePDO.php`

Get all fulltext stopwords for database engine

## Arguments

- string $engine Specify DB engine of "myisam" or "innodb" or omit for current DB engine
- bool $flip Return flipped array where stopwords are array keys rather than values? for isset() use (default=false)

## Return value

array
