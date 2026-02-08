# $imageSizerEngine->getImageInfo($rawData = false): string|array

Source: `wire/core/ImageSizerEngine.php`

ImageInformation from Image Inspector
in short form or full RawInfoData

## Usage

~~~~~
// basic usage
$string = $imageSizerEngine->getImageInfo();

// usage with all arguments
$string = $imageSizerEngine->getImageInfo($rawData = false);
~~~~~

## Arguments

- `$rawData` (optional) `bool`

## Return value

- `string|array`

## Details

- @todo this appears to be a duplicate of what's in ImageSizer class?
