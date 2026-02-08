# $imageSizerEngine->prepare($filename, $options = array(), $inspectionResult = null)

Source: `wire/core/ImageSizerEngine.php`

Prepare the ImageSizer (this should be the first method you call)

This is used as a replacement for __construct() since modules can't have required arguments
to their constructor.

## Usage

~~~~~
// basic usage
$result = $imageSizerEngine->prepare($filename);

// usage with all arguments
$result = $imageSizerEngine->prepare($filename, $options = array(), $inspectionResult = null);
~~~~~

## Arguments

- `$filename` `string`
- `$options` (optional) `array`
- `$inspectionResult` (optional) `null|array`
