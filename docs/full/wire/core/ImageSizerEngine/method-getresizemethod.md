# ImageSizerEngine::getResizeMethod()

Source: `wire/core/ImageSizerEngine.php`

Get an integer representing the resize method to use

This method calculates all dimensions at first. It is called before any of the main image operations,
but after rotation and crop_before_resize. As result it returns an integer [0|2|4] that indicates which
steps should be processed:

0 = this is the case if the original size is requested or a greater size but upscaling is set to false
2 = only resize with aspect ratio
4 = resize and crop with aspect ratio

@param mixed $gdWidth

@param mixed $gdHeight

@param mixed $targetWidth

@param mixed $targetHeight

@param mixed $x1

@param mixed $y1

@return int 0|2|4
