# $wireInputData->array($varName, $sanitizer = null): array

Source: `wire/core/WireInputData.php`

Sanitize array or CSV String to an array, optionally running elements through specified $sanitizer.

## Usage

~~~~~
// basic usage
$array = $wireInputData->array($varName);

// usage with all arguments
$array = $wireInputData->array($varName, $sanitizer = null);
~~~~~
