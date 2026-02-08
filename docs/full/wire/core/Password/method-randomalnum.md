# $password->randomAlnum($length = 0, array $options = array()): string

Source: `wire/core/Password.php`

Return cryptographically secure random alphanumeric, alpha or numeric string

## Usage

~~~~~
// basic usage
$string = $password->randomAlnum();

// usage with all arguments
$string = $password->randomAlnum($length = 0, array $options = array());
~~~~~

## Arguments

- `$length` (optional) `int` Required length of string, or 0 for random length
- `$options` (optional) `array` See WireRandom::alphanumeric() for options

## Return value

- `string`

## Exceptions

- `WireException`

## Since

3.0.109

## Deprecated

use WireRandom::alphanumeric() instead
