# $imageSizerEngine->processResize($srcFilename, $dstFilename, $fullWidth, $fullHeight, $finalWidth, $finalHeight): bool

Source: `wire/core/ImageSizerEngine.php`

Process the image resize

Processing is as follows:
   1. first do a check if the given image(type) can be processed, if not do an early return false
   2. than (try) to process all required steps, if one failes, return false
   3. if all is successful, finally return true

## Arguments

- string $srcFilename Source file
- string $dstFilename Destination file
- int $fullWidth Current width
- int $fullHeight Current height
- int $finalWidth Requested final width
- int $finalHeight Requested final height

## Return value

bool True if successful, false if not

## Throws

- WireException
