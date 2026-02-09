# $imageSizerEngine->setDefaultGamma($value = 2.2): self

Source: `wire/core/ImageSizerEngine.php`

Set default gamma value: 0.5 - 4.0 | -1

## Usage

~~~~~
// basic usage
$result = $imageSizerEngine->setDefaultGamma();

// usage with all arguments
$result = $imageSizerEngine->setDefaultGamma($value = 2.2);
~~~~~

## Arguments

- `$value` (optional) `float|int` 0.5 to 4.0 or -1 to disable

## Return value

- `self`

## Exceptions

- `WireException` when given invalid value
