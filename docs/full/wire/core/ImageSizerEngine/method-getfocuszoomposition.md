# ImageSizerEngine::getFocusZoomPosition()

Source: `wire/core/ImageSizerEngine.php`

Helper function to perform a cropExtra / cropBefore cropping

Intended for use by the getFocusZoomCropDimensions() method

@param string $focus (focus point in percent, like: 54.7%)

@param int $sourceDimension (source image width or height)

@param int $cropDimension (target crop-image width or height)

@param int $zoom

@return int $position (crop position x or y in pixel)
