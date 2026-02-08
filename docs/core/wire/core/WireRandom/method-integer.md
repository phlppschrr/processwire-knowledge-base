# WireRandom::integer()

Source: `wire/core/WireRandom.php`

Get a random integer

@param int $min Minimum allowed value (default=0).

@param int $max Maximum allowed value (default=PHP_INT_MAX).

@param array $options
 - `info` (bool): Return array of [value, type] indicating what type of random generator was used? (default=false).
 - `cryptoSecure` (bool): Throw WireException if cryptographically secure type not available (default=false).

@return int|array Returns integer, or will return array if $info option specified.

@throws WireException
