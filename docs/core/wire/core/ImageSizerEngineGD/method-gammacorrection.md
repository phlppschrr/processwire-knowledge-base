# $imageSizerEngineGD->gammaCorrection(&$image, $mode)

Source: `wire/core/ImageSizerEngineGD.php`

apply GammaCorrection to an image (@horst)

with mode = true it linearizes an image to 1
with mode = false it set it back to the originating gamma value

## Usage

~~~~~
// basic usage
$result = $imageSizerEngineGD->gammaCorrection($image, $mode);

// usage with all arguments
$result = $imageSizerEngineGD->gammaCorrection(&$image, $mode);
~~~~~

## Arguments

- `$image` `resource`
- `$mode` `bool`
