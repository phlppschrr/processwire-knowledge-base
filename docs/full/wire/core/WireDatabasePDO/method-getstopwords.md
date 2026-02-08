# $wireDatabasePDO->getStopwords($engine = '', $flip = false): array

Source: `wire/core/WireDatabasePDO.php`

Get all fulltext stopwords for database engine

## Arguments

- `$engine` (optional) `string` Specify DB engine of "myisam" or "innodb" or omit for current DB engine
- `$flip` (optional) `bool` Return flipped array where stopwords are array keys rather than values? for isset() use (default=false)

## Return value

array
