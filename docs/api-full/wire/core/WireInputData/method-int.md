# $wireInputData->int($varName, $min = 0, $max = null): int

Source: `wire/core/WireInputData.php`

Sanitize value to integer with optional min and max. Unsigned if max >= 0, signed if max < 0.

## Usage

~~~~~
// basic usage
$int = $wireInputData->int($varName);

// usage with all arguments
$int = $wireInputData->int($varName, $min = 0, $max = null);
~~~~~
