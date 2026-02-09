# $imageSizerEngine->getCropDimensions(&$w1, &$h1, $gdWidth, $targetWidth, $gdHeight, $targetHeight)

Source: `wire/core/ImageSizerEngine.php`

Check if cropping is needed, if yes, populate x- and y-position to params $w1 and $h1

Intended for use by the resize() method

## Usage

~~~~~
// basic usage
$result = $imageSizerEngine->getCropDimensions($w1, $h1, $gdWidth, $targetWidth, $gdHeight, $targetHeight);

// usage with all arguments
$result = $imageSizerEngine->getCropDimensions(&$w1, &$h1, $gdWidth, $targetWidth, $gdHeight, $targetHeight);
~~~~~

## Arguments

- `$w1` `int` - byReference
- `$h1` `int` - byReference
- `$gdWidth` `int`
- `$targetWidth` `int`
- `$gdHeight` `int`
- `$targetHeight` `int`
