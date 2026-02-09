# $fileLog->getChunkArray($chunkNum = 1, $chunkSize = 0, $reverse = true): array

Source: `wire/core/FileLog.php`

Get lines from the end of a file based on chunk size

## Usage

~~~~~
// basic usage
$array = $fileLog->getChunkArray();

// usage with all arguments
$array = $fileLog->getChunkArray($chunkNum = 1, $chunkSize = 0, $reverse = true);
~~~~~

## Arguments

- `$chunkSize` (optional) `int`
- `$chunkNum` (optional) `int`
- `$reverse` (optional) `bool`

## Return value

- `array`
