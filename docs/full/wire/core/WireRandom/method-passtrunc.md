# $wireRandom->passTrunc($value, array $options): string

Source: `wire/core/WireRandom.php`

Truncate password to requested maxLength without removing required options (for password method)

## Usage

~~~~~
// basic usage
$string = $wireRandom->passTrunc($value, $options);

// usage with all arguments
$string = $wireRandom->passTrunc($value, array $options);
~~~~~

## Arguments

- `$value` `string`
- `$options` `array` See options from password() method

## Return value

- `string`
