# $imageSizerEngine->processResize($srcFilename, $dstFilename, $fullWidth, $fullHeight, $finalWidth, $finalHeight): bool

Source: `wire/core/ImageSizerEngine.php`

Process the image resize

Processing is as follows:
   1. first do a check if the given image(type) can be processed, if not do an early return false
   2. than (try) to process all required steps, if one failes, return false
   3. if all is successful, finally return true

## Usage

~~~~~
// basic usage
$bool = $imageSizerEngine->processResize($srcFilename, $dstFilename, $fullWidth, $fullHeight, $finalWidth, $finalHeight);
~~~~~

## Arguments

- `$srcFilename` `string` Source file
- `$dstFilename` `string` Destination file
- `$fullWidth` `int` Current width
- `$fullHeight` `int` Current height
- `$finalWidth` `int` Requested final width
- `$finalHeight` `int` Requested final height

## Return value

- `bool` True if successful, false if not

## Exceptions

- `WireException`
