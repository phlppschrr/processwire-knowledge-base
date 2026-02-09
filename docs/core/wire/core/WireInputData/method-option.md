# $wireInputData->option($varName, array $allowedValues): string|null

Source: `wire/core/WireInputData.php`

Return value of $varName only if it exists in $allowedValues.

## Usage

~~~~~
// basic usage
$string = $wireInputData->option($varName, $allowedValues);

// usage with all arguments
$string = $wireInputData->option($varName, array $allowedValues);
~~~~~
