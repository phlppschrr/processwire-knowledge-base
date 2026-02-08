# $wireRandom->integer($min = 0, $max = PHP_INT_MAX, array $options = array()): int|array

Source: `wire/core/WireRandom.php`

Get a random integer

## Arguments

- int $min Minimum allowed value (default=0).
- int $max Maximum allowed value (default=PHP_INT_MAX).
- array $options - `info` (bool): Return array of [value, type] indicating what type of random generator was used? (default=false). - `cryptoSecure` (bool): Throw WireException if cryptographically secure type not available (default=false).

## Return value

int|array Returns integer, or will return array if $info option specified.

## Throws

- WireException
