# $imageSizerEngine->getFocusZoomPosition($focus, $sourceDimension, $cropDimension, $zoom): int

Source: `wire/core/ImageSizerEngine.php`

Helper function to perform a cropExtra / cropBefore cropping

Intended for use by the getFocusZoomCropDimensions() method

## Arguments

- `$focus` `string` (focus point in percent, like: 54.7%)
- `$sourceDimension` `int` (source image width or height)
- `$cropDimension` `int` (target crop-image width or height)
- `$zoom` `int`

## Return value

int $position (crop position x or y in pixel)
