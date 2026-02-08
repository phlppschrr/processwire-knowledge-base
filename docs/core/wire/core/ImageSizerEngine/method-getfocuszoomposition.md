# $imageSizerEngine->getFocusZoomPosition($focus, $sourceDimension, $cropDimension, $zoom): int

Source: `wire/core/ImageSizerEngine.php`

Helper function to perform a cropExtra / cropBefore cropping

Intended for use by the getFocusZoomCropDimensions() method

## Arguments

- string $focus (focus point in percent, like: 54.7%)
- int $sourceDimension (source image width or height)
- int $cropDimension (target crop-image width or height)
- int $zoom

## Return value

int $position (crop position x or y in pixel)
