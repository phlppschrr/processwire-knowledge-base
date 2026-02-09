# $fileLog->chunkSize($chunkSize = 0): int

Source: `wire/core/FileLog.php`

Get or set the default chunk size used when reading from logs and not overridden by method argument

## Usage

~~~~~
// basic usage
$int = $fileLog->chunkSize();

// usage with all arguments
$int = $fileLog->chunkSize($chunkSize = 0);
~~~~~

## Arguments

- `$chunkSize` (optional) `int` Specify chunk size to set, or omit to get

## Return value

- `int`

## Since

3.0.143
