# $wireInputData->float($varName, $min = null, $max = null, $precision = null): float

Source: `wire/core/WireInputData.php`

Sanitize value to float with optional min and max values.

## Usage

~~~~~
// basic usage
$float = $wireInputData->float($varName);

// usage with all arguments
$float = $wireInputData->float($varName, $min = null, $max = null, $precision = null);
~~~~~
