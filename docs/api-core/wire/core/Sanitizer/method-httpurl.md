# $sanitizer->httpUrl($value, $options = array()): string

Source: `wire/core/Sanitizer.php`

URL with http or https scheme required

## Usage

~~~~~
// basic usage
$string = $sanitizer->httpUrl($value);

// usage with all arguments
$string = $sanitizer->httpUrl($value, $options = array());
~~~~~

## Arguments

- `$value` `string` URL to validate
- `$options` (optional) `array` See the url() method for all options.

## Return value

- `string` Returns valid URL or blank string if it cannot be made valid.

## Since

3.0.129
