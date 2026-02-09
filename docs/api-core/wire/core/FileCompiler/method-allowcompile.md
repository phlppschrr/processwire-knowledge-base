# $fileCompiler->allowCompile(&$filename, &$basename): bool

Source: `wire/core/FileCompiler.php`

Allow the given filename to be compiled?

## Usage

~~~~~
// basic usage
$bool = $fileCompiler->allowCompile($filename, $basename);

// usage with all arguments
$bool = $fileCompiler->allowCompile(&$filename, &$basename);
~~~~~

## Arguments

- `$filename` `string` Full path and filename to compile (this property can be modified by the function).
- `$basename` `string` Just the basename (this property can be modified by the function).

## Return value

- `bool`
