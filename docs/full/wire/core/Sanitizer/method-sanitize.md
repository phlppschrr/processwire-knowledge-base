# $sanitizer->sanitize($value, $method = 'text'): string|int|array|float|null

Source: `wire/core/Sanitizer.php`

Call a sanitizer method indirectly where method name can contain combined/combo methods

This method is primarily here to support predefined sanitizers in strings, like those that might
be specified in settings for a module or field. For regular use, you probably want to call the
sanitizer methods directly rather than through this method.

## Example

~~~~~
// sanitize with text then entities sanitizers
$value = $sanitizer->sanitize($value, 'text,entities');

// numbers appended to text sanitizers imply max length
$value = $sanitizer->sanitize($value, 'text128,entities');
~~~~~

## Usage

~~~~~
// basic usage
$string = $sanitizer->sanitize($value);

// usage with all arguments
$string = $sanitizer->sanitize($value, $method = 'text');
~~~~~

## Arguments

- `$value` `mixed`
- `$method` (optional) `string` Method name "method", or combined method name(s) "method1,method2,method3"

## Return value

- `string|int|array|float|null`

## Since

3.0.125
