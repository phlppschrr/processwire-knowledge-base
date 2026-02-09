# $wireDatabasePDO->isStopword($word, $engine = ''): bool

Source: `wire/core/WireDatabasePDO.php`

Is given word a fulltext stopword for database engine?

## Usage

~~~~~
// basic usage
$bool = $wireDatabasePDO->isStopword($word);

// usage with all arguments
$bool = $wireDatabasePDO->isStopword($word, $engine = '');
~~~~~

## Arguments

- `$word` `string`
- `$engine` (optional) `string` DB engine ('myisam' or 'innodb') or omit for current engine

## Return value

- `bool`

## Since

3.0.160
