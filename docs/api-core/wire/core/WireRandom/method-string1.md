# $wireRandom->string1($length, $allowed, array $options): string

Source: `wire/core/WireRandom.php`

Generate a random string using faster method

## Usage

~~~~~
// basic usage
$string = $wireRandom->string1($length, $allowed, $options);

// usage with all arguments
$string = $wireRandom->string1($length, $allowed, array $options);
~~~~~

## Arguments

- `$length` `int` Required length
- `$allowed` `string` Characters allowed
- `$options` `array` - `noRepeat` (bool): True if two of the same character may not be repeated in sequence.

## Return value

- `string`
