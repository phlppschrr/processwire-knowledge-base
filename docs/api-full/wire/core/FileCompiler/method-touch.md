# $fileCompiler->touch($filename, $time = null): bool

Source: `wire/core/FileCompiler.php`

Same as PHP touch() but with fallbacks for cases where touch() does not work

## Usage

~~~~~
// basic usage
$bool = $fileCompiler->touch($filename);

// usage with all arguments
$bool = $fileCompiler->touch($filename, $time = null);
~~~~~

## Arguments

- `$filename` `string`
- `$time` (optional) `null|int`

## Return value

- `bool`
