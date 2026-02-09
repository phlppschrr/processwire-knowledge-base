# $wireInputData->intArray($varName, $min = 0, $max = null): array

Source: `wire/core/WireInputData.php`

Sanitize array or CSV string to an array of integers with optional min and max values.

## Usage

~~~~~
// basic usage
$array = $wireInputData->intArray($varName);

// usage with all arguments
$array = $wireInputData->intArray($varName, $min = 0, $max = null);
~~~~~
