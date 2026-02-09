# $fileCompiler->mkdir($path, $recursive = true): bool

Source: `wire/core/FileCompiler.php`

Make a directory with proper permissions

## Usage

~~~~~
// basic usage
$bool = $fileCompiler->mkdir($path);

// usage with all arguments
$bool = $fileCompiler->mkdir($path, $recursive = true);
~~~~~

## Arguments

- `$path` `string` Path of directory to create
- `$recursive` (optional) `bool` Default is true

## Return value

- `bool`
