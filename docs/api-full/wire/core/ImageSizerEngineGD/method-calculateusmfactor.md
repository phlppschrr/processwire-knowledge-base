# $imageSizerEngineGD->calculateUSMfactor($targetWidth, $targetHeight, $origWidth = null, $origHeight = null): int

Source: `wire/core/ImageSizerEngineGD.php`

Calculate USM factor

Return an integer value indicating how much an image should be sharpened
according to resizing scalevalue and absolute target dimensions

## Usage

~~~~~
// basic usage
$int = $imageSizerEngineGD->calculateUSMfactor($targetWidth, $targetHeight);

// usage with all arguments
$int = $imageSizerEngineGD->calculateUSMfactor($targetWidth, $targetHeight, $origWidth = null, $origHeight = null);
~~~~~

## Arguments

- `$targetWidth` `mixed` width of the targetimage
- `$targetHeight` `mixed` height of the targetimage
- `$origWidth` (optional) `mixed`
- `$origHeight` (optional) `mixed`

## Return value

- `int`
