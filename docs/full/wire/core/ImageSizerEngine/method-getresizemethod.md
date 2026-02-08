# $imageSizerEngine->getResizeMethod(&$gdWidth, &$gdHeight, &$targetWidth, &$targetHeight, &$x1, &$y1): int

Source: `wire/core/ImageSizerEngine.php`

Get an integer representing the resize method to use

This method calculates all dimensions at first. It is called before any of the main image operations,
but after rotation and crop_before_resize. As result it returns an integer [0|2|4] that indicates which
steps should be processed:

0 = this is the case if the original size is requested or a greater size but upscaling is set to false
2 = only resize with aspect ratio
4 = resize and crop with aspect ratio

## Arguments

- mixed $gdWidth
- mixed $gdHeight
- mixed $targetWidth
- mixed $targetHeight
- mixed $x1
- mixed $y1

## Return value

int 0|2|4
