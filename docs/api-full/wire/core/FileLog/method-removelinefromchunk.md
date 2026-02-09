# $fileLog->removeLineFromChunk(&$line, &$chunk, $chunkSize)

Source: `wire/core/FileLog.php`

Remove given $line from $chunk and add counter to end of $line indicating quantity that was removed

## Usage

~~~~~
// basic usage
$result = $fileLog->removeLineFromChunk($line, $chunk, $chunkSize);

// usage with all arguments
$result = $fileLog->removeLineFromChunk(&$line, &$chunk, $chunkSize);
~~~~~

## Arguments

- `$line` `string`
- `$chunk` `string`
- `$chunkSize` `int`

## Since

3.0.143
