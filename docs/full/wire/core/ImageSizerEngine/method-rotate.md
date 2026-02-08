# $imageSizerEngine->rotate($degrees, $dstFilename = ''): bool

Source: `wire/core/ImageSizerEngine.php`

Just rotate image by number of degrees

## Usage

~~~~~
// basic usage
$bool = $imageSizerEngine->rotate($degrees);

// usage with all arguments
$bool = $imageSizerEngine->rotate($degrees, $dstFilename = '');
~~~~~

## Arguments

- `$degrees` `int`
- `$dstFilename` (optional) `string` Optional destination filename. If not present, source will be overwritten.

## Return value

- `bool` True on success, false on fail
