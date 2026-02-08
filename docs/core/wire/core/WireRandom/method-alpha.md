# $wireRandom->alpha($length = 0, array $options = array()): string

Source: `wire/core/WireRandom.php`

Return string of random ASCII alphabetical letters

## Usage

~~~~~
// basic usage
$string = $wireRandom->alpha();

// usage with all arguments
$string = $wireRandom->alpha($length = 0, array $options = array());
~~~~~

## Arguments

- `$length` (optional) `int` Required length of string or 0 for random length
- `$options` (optional) `array` See options for alphanumeric() method

## Return value

- `string`

## Since

3.0.111
