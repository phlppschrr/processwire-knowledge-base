# $imageSizer->newImageSizerEngine($filename = '', array $options = array(), $inspectionResult = null): ImageSizerEngine|null

Source: `wire/core/ImageSizer.php`

Instantiate an ImageSizerEngine

## Usage

~~~~~
// basic usage
$imageSizerEngine = $imageSizer->newImageSizerEngine();

// usage with all arguments
$imageSizerEngine = $imageSizer->newImageSizerEngine($filename = '', array $options = array(), $inspectionResult = null);
~~~~~

## Arguments

- `$filename` (optional) `string`
- `$options` (optional) `array`
- `$inspectionResult` (optional) `null|array`

## Return value

- `ImageSizerEngine|null`

## Exceptions

- `WireException`
