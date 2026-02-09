# $wireInputData->intUnsigned($varName, $min = null, $max = null): int

Source: `wire/core/WireInputData.php`

Sanitize value to unsigned integer with optional min and max.

## Usage

~~~~~
// basic usage
$int = $wireInputData->intUnsigned($varName);

// usage with all arguments
$int = $wireInputData->intUnsigned($varName, $min = null, $max = null);
~~~~~
