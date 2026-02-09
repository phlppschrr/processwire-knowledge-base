# $sanitizer->selectorValueArray(array $value, $options = array()): string

Source: `wire/core/Sanitizer.php`

Wrapper for selectorValueV2() when it receives an array

## Usage

~~~~~
// basic usage
$string = $sanitizer->selectorValueArray($value);

// usage with all arguments
$string = $sanitizer->selectorValueArray(array $value, $options = array());
~~~~~

## Arguments

- `$value` `array`
- `$options` (optional) `array` See options for selectorValue()

## Return value

- `string` Always returns string unless you specify something different for 'emptyValue'
