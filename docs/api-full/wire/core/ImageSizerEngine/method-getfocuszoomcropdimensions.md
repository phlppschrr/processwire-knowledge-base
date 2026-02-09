# $imageSizerEngine->getFocusZoomCropDimensions($zoom, $fullWidth, $fullHeight, $finalWidth, $finalHeight): array

Source: `wire/core/ImageSizerEngine.php`

Get an array of the 4 dimensions necessary to perform a cropExtra / cropBefore cropping

Intended for use by the resize() method

## Usage

~~~~~
// basic usage
$array = $imageSizerEngine->getFocusZoomCropDimensions($zoom, $fullWidth, $fullHeight, $finalWidth, $finalHeight);
~~~~~

## Arguments

- `$zoom` `int`
- `$fullWidth` `int`
- `$fullHeight` `int`
- `$finalWidth` `int`
- `$finalHeight` `int`

## Return value

- `array`
