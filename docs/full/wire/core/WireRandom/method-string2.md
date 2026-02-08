# $wireRandom->string2($length, $allowed, array $options): string

Source: `wire/core/WireRandom.php`

Generate random string using method that pulls from the base64 method

## Usage

~~~~~
// basic usage
$string = $wireRandom->string2($length, $allowed, $options);

// usage with all arguments
$string = $wireRandom->string2($length, $allowed, array $options);
~~~~~

## Arguments

- `$length` `int` Required length
- `$allowed` `string` Allowed characters
- `$options` `array` See options for alphanumeric() method

## Return value

- `string`
