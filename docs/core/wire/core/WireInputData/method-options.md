# $wireInputData->options($varName, array $allowedValues): array

Source: `wire/core/WireInputData.php`

Return all values in array $varName that also exist in $allowedValues.

## Usage

~~~~~
// basic usage
$array = $wireInputData->options($varName, $allowedValues);

// usage with all arguments
$array = $wireInputData->options($varName, array $allowedValues);
~~~~~
