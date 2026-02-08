# $password->randomPass(array $options = array()): string

Source: `wire/core/Password.php`

Generate and return a random password

See WireRandom::pass() method for details.

## Usage

~~~~~
// basic usage
$string = $password->randomPass();

// usage with all arguments
$string = $password->randomPass(array $options = array());
~~~~~

## Arguments

- `$options` (optional) `array` See WireRandom::pass() for options

## Return value

- `string`
