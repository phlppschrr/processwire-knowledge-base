# $imageSizer->newDefaultImageSizerEngine($filename = '', $options = array(), $inspectionResult = null): ImageSizerEngine|null

Source: `wire/core/ImageSizer.php`

Get the default/fallback ImageSizer engine

## Usage

~~~~~
// basic usage
$imageSizerEngine = $imageSizer->newDefaultImageSizerEngine();

// usage with all arguments
$imageSizerEngine = $imageSizer->newDefaultImageSizerEngine($filename = '', $options = array(), $inspectionResult = null);
~~~~~

## Arguments

- `$filename` (optional) `string`
- `$options` (optional) `array`
- `$inspectionResult` (optional) `null|array`

## Return value

- `ImageSizerEngine|null`

## Exceptions

- `WireException`
