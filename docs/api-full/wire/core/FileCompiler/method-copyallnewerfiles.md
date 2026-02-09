# $fileCompiler->copyAllNewerFiles($source, $target, $recursive = true): int

Source: `wire/core/FileCompiler.php`

Recursively copy all files from $source to $target, but only if $source file is $newer

## Usage

~~~~~
// basic usage
$int = $fileCompiler->copyAllNewerFiles($source, $target);

// usage with all arguments
$int = $fileCompiler->copyAllNewerFiles($source, $target, $recursive = true);
~~~~~

## Arguments

- `$source` `string`
- `$target` `string`
- `$recursive` (optional) `bool`

## Return value

- `int` Number of files copied
