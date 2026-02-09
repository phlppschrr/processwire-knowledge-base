# $wireRandom->numeric($length = 0, array $options = array()): string

Source: `wire/core/WireRandom.php`

Return string of random numbers/digits

## Usage

~~~~~
// basic usage
$string = $wireRandom->numeric();

// usage with all arguments
$string = $wireRandom->numeric($length = 0, array $options = array());
~~~~~

## Arguments

- `$length` (optional) `int` Required length of string or 0 for random length
- `$options` (optional) `array` See options for alphanumeric() method

## Return value

- `string`

## Since

3.0.111
