# $imageSizerEngine->convertToSepia($dstFilename = '', $sepia = 55): bool

Source: `wire/core/ImageSizerEngine.php`

Convert image to sepia

## Usage

~~~~~
// basic usage
$bool = $imageSizerEngine->convertToSepia();

// usage with all arguments
$bool = $imageSizerEngine->convertToSepia($dstFilename = '', $sepia = 55);
~~~~~

## Arguments

- `$dstFilename` (optional) `string` If different from source file
- `$sepia` (optional) `float|int` Sepia value

## Return value

- `bool`
