# $wireInput->queryString($overrides = array()): string

Source: `wire/core/WireInput.php`

Return the unsanitized query string that was part of this request, or blank if none

Note that the returned query string is not sanitized, so if you use it in any output
be sure to run it through `$sanitizer->entities()` first. An optional assoc array
param can be used to add new GET params or override existing ones.

## Usage

~~~~~
// basic usage
$string = $wireInput->queryString();

// usage with all arguments
$string = $wireInput->queryString($overrides = array());
~~~~~

## Arguments

- `$overrides` (optional) `array` Optional assoc array for overriding or adding GET params

## Return value

- `string` Returns the unsanitized query string

## See Also

- [WireInput::queryStringClean()](method-querystringclean.md)
