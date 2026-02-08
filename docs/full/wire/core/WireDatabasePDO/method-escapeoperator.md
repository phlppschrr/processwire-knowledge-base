# $wireDatabasePDO->escapeOperator($operator, $operatorType = self::operatorTypeComparison, $default = '='): string

Source: `wire/core/WireDatabasePDO.php`

Sanitize comparison operator

## Arguments

- string $operator
- bool|int|null $operatorType Specify a WireDatabasePDO::operatorType* constant (default=operatorTypeComparison)
- string $default Default/fallback operator to return if given one is not valid (default='=')

## Return value

string
