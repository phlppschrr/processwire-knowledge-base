# $imageSizerEngine->getCropDimensions(&$w1, &$h1, $gdWidth, $targetWidth, $gdHeight, $targetHeight)

Source: `wire/core/ImageSizerEngine.php`

Check if cropping is needed, if yes, populate x- and y-position to params $w1 and $h1

Intended for use by the resize() method

## Arguments

- int $w1 - byReference
- int $h1 - byReference
- int $gdWidth
- int $targetWidth
- int $gdHeight
- int $targetHeight
