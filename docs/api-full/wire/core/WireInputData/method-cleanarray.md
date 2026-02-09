# $wireInputData->cleanArray(array $a): array

Source: `wire/core/WireInputData.php`

Clean an array of data

Support multi-dimensional arrays consistent with `$config->wireInputArrayDepth`
setting (3.0.178+) and remove slashes if applicable/necessary.

## Usage

~~~~~
// basic usage
$array = $wireInputData->cleanArray($a);

// usage with all arguments
$array = $wireInputData->cleanArray(array $a);
~~~~~

## Arguments

- `$a` `array`

## Return value

- `array`
