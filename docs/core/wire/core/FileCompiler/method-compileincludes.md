# $fileCompiler->compileIncludes(&$data, $sourceFile)

Source: `wire/core/FileCompiler.php`

Compile include(), require() (and variations) to refer to compiled files where possible

## Usage

~~~~~
// basic usage
$result = $fileCompiler->compileIncludes($data, $sourceFile);

// usage with all arguments
$result = $fileCompiler->compileIncludes(&$data, $sourceFile);
~~~~~

## Arguments

- `$data` `string`
- `$sourceFile` `string`
