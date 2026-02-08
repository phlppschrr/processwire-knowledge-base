# $wireNumberTools->randomInteger($min, $max, $throw = false): int

Source: `wire/core/WireNumberTools.php`

Return a random integer (cryptographically secure when available)

## Arguments

- int $min Minimum value (default=0)
- int $max Maximum value (default=PHP_INT_MAX)
- bool $throw Throw WireException if we cannot achieve a cryptographically secure random number? (default=false)

## Return value

int

## Meta

- @since 3.0.214
