# $password->randomAlnum($length = 0, array $options = array()): string

Source: `wire/core/Password.php`

Return cryptographically secure random alphanumeric, alpha or numeric string

## Arguments

- int $length Required length of string, or 0 for random length
- array $options See WireRandom::alphanumeric() for options

## Return value

string

## Throws

- WireException

## Meta

- @since 3.0.109
- @deprecated use WireRandom::alphanumeric() instead
