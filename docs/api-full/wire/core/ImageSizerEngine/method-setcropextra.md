# $imageSizerEngine->setCropExtra($value): self

Source: `wire/core/ImageSizerEngine.php`

Set values for cropExtra rectangle, which enables cropping before resizing

Added by @horst

## Usage

~~~~~
// basic usage
$result = $imageSizerEngine->setCropExtra($value);
~~~~~

## Arguments

- `$value` `array` containing 4 params (x y w h) indexed or associative

## Return value

- `self`

## Exceptions

- `WireException` when given invalid value
