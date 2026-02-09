# $password->randomAlpha($qty = 1, $alphanumeric = false, $disallow = array()): string

Source: `wire/core/Password.php`

Return a pseudo-random alpha or alphanumeric character

This method may be deprecated at some point, so it is preferable to use the
`randomLetters()` or `randomAlnum()` methods instead, when you can count on
the PW version being 3.0.109 or higher.

## Usage

~~~~~
// basic usage
$string = $password->randomAlpha();

// usage with all arguments
$string = $password->randomAlpha($qty = 1, $alphanumeric = false, $disallow = array());
~~~~~

## Arguments

- `$qty` (optional) `int` Number of random characters requested
- `$alphanumeric` (optional) `bool` Specify true to allow digits in return value
- `$disallow` (optional) `array` Characters that may not be used in return value

## Return value

- `string`

## Deprecated

use WireRandom::alpha() instead
