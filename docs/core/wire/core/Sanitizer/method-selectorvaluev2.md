# $sanitizer->selectorValueV2($value, $options = array()): bool|mixed|string

Source: `wire/core/Sanitizer.php`

Sanitize selector value (version 2, 3.0.156+)

This version is a little more thorough and has more options than version 1.

## Usage

~~~~~
// basic usage
$bool = $sanitizer->selectorValueV2($value);

// usage with all arguments
$bool = $sanitizer->selectorValueV2($value, $options = array());
~~~~~

## Arguments

- `$value` `string|array`
- `$options` (optional) `array`

## Return value

- `bool|mixed|string` Always returns string unless you specify something different for 'emptyValue'
