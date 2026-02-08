# $fileLog->get($chunkSize = 0, $chunkNum = 1): array

Source: `wire/core/FileLog.php`

Get lines from the end of a file based on chunk size (deprecated)

## Usage

~~~~~
// basic usage
$array = $fileLog->get();

// usage with all arguments
$array = $fileLog->get($chunkSize = 0, $chunkNum = 1);
~~~~~

## Arguments

- `$chunkSize` (optional) `int`
- `$chunkNum` (optional) `int`

## Return value

- `array`

## Deprecated

Use find() instead
