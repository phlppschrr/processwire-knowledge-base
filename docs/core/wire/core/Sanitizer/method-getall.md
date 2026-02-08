# $sanitizer->getAll($getReturnTypes = false): array

Source: `wire/core/Sanitizer.php`

Get all sanitizer method names and optionally types they return

## Usage

~~~~~
// basic usage
$array = $sanitizer->getAll();

// usage with all arguments
$array = $sanitizer->getAll($getReturnTypes = false);
~~~~~

## Arguments

- `$getReturnTypes` (optional) `bool` Get array where method names are keys and values are return types?

## Return value

- `array`

## Since

3.0.165
