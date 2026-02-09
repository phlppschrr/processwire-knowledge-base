# $password->randomDigits($length = 0, array $options = array()): string

Source: `wire/core/Password.php`

Return string of random digits

## Usage

~~~~~
// basic usage
$string = $password->randomDigits();

// usage with all arguments
$string = $password->randomDigits($length = 0, array $options = array());
~~~~~

## Arguments

- `$length` (optional) `int` Required length of string or 0 for random length
- `$options` (optional) `array` See WireRandom::numeric() method

## Return value

- `string`

## Since

3.0.109

## Deprecated

Use WireRandom::numeric() instead
