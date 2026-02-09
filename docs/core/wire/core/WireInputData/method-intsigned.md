# $wireInputData->intSigned($varName, $min = null, $max = null): int

Source: `wire/core/WireInputData.php`

Sanitize value to signed integer with optional min and max.

## Usage

~~~~~
// basic usage
$int = $wireInputData->intSigned($varName);

// usage with all arguments
$int = $wireInputData->intSigned($varName, $min = null, $max = null);
~~~~~
