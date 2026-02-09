# $sanitizer->htmlClasses($value, $getArray = false): string|array

Source: `wire/core/Sanitizer.php`

Sanitize string to ASCII-only space-separated HTML class attribute values with no duplicates

See additional notes in `Sanitizer::htmlClass()` method.

## Usage

~~~~~
// basic usage
$string = $sanitizer->htmlClasses($value);

// usage with all arguments
$string = $sanitizer->htmlClasses($value, $getArray = false);
~~~~~

## Arguments

- `$value` `string|array`
- `$getArray` (optional) `bool` Get array rather than string? (default=false)

## Return value

- `string|array`

## Since

3.0.212
