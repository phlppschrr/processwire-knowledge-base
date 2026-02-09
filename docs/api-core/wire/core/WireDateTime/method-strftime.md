# $wireDateTime->strftime($format, $timestamp = null): string|false

Source: `wire/core/WireDateTime.php`

strftime() replacement function that works in PHP 8.1+ (though not locale aware)

## Usage

~~~~~
// basic usage
$string = $wireDateTime->strftime($format);

// usage with all arguments
$string = $wireDateTime->strftime($format, $timestamp = null);
~~~~~

## Arguments

- `$format` `string`
- `$timestamp` (optional) `null|int|string`

## Return value

- `string|false`

## Since

3.0.197
