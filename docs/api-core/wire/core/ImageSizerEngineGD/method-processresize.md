# $imageSizerEngineGD->processResize($srcFilename, $dstFilename, $fullWidth, $fullHeight, $finalWidth, $finalHeight): bool

Source: `wire/core/ImageSizerEngineGD.php`

Process the image resize

## Usage

~~~~~
// basic usage
$bool = $imageSizerEngineGD->processResize($srcFilename, $dstFilename, $fullWidth, $fullHeight, $finalWidth, $finalHeight);
~~~~~

## Arguments

- `$srcFilename` `string` Source file
- `$dstFilename` `string` Destination file
- `$fullWidth` `int` Current width
- `$fullHeight` `int` Current height
- `$finalWidth` `int` Requested final width
- `$finalHeight` `int` Requested final height

## Return value

- `bool`

## Exceptions

- `WireException`
