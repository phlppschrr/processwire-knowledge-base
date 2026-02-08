# $imageSizerEngine->loadImageInfo($filename, $reloadAll = false)

Source: `wire/core/ImageSizerEngine.php`

Load all image information from ImageInspector (Module)

## Usage

~~~~~
// basic usage
$result = $imageSizerEngine->loadImageInfo($filename);

// usage with all arguments
$result = $imageSizerEngine->loadImageInfo($filename, $reloadAll = false);
~~~~~

## Arguments

- `$filename` `string`
- `$reloadAll` (optional) `bool`

## Exceptions

- `WireException`
