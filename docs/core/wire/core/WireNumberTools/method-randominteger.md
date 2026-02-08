# WireNumberTools::randomInteger()

Source: `wire/core/WireNumberTools.php`

Return a random integer (cryptographically secure when available)

@param int $min Minimum value (default=0)

@param int $max Maximum value (default=PHP_INT_MAX)

@param bool $throw Throw WireException if we cannot achieve a cryptographically secure random number? (default=false)

@return int

@since 3.0.214
