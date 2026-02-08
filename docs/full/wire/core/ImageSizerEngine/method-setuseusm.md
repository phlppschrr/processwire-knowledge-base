# $imageSizerEngine->setUseUSM($value = true): self

Source: `wire/core/ImageSizerEngine.php`

Toggle on/off the usage of USM algorithm for sharpening

## Usage

~~~~~
// basic usage
$result = $imageSizerEngine->setUseUSM();

// usage with all arguments
$result = $imageSizerEngine->setUseUSM($value = true);
~~~~~

## Arguments

- `$value` (optional) `bool` Whether to USM is used or not (default = true)

## Return value

- `self`
