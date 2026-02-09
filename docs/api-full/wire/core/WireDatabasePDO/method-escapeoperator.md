# $wireDatabasePDO->escapeOperator($operator, $operatorType = self::operatorTypeComparison, $default = '='): string

Source: `wire/core/WireDatabasePDO.php`

Sanitize comparison operator

## Usage

~~~~~
// basic usage
$string = $wireDatabasePDO->escapeOperator($operator);

// usage with all arguments
$string = $wireDatabasePDO->escapeOperator($operator, $operatorType = self::operatorTypeComparison, $default = '=');
~~~~~

## Arguments

- `$operator` `string`
- `$operatorType` (optional) `bool|int|null` Specify a WireDatabasePDO::operatorType* constant (default=operatorTypeComparison)
- `$default` (optional) `string` Default/fallback operator to return if given one is not valid (default='=')

## Return value

- `string`
