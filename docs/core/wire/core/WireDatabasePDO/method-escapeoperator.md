# WireDatabasePDO::escapeOperator()

Source: `wire/core/WireDatabasePDO.php`

Sanitize comparison operator


@param string $operator

@param bool|int|null $operatorType Specify a WireDatabasePDO::operatorType* constant (default=operatorTypeComparison)

@param string $default Default/fallback operator to return if given one is not valid (default='=')

@return string
