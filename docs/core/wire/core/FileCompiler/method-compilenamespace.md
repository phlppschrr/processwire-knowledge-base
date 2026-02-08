# $fileCompiler->compileNamespace(&$data): bool

Source: `wire/core/FileCompiler.php`

Compile global class/interface/function references to namespaced versions

## Usage

~~~~~
// basic usage
$bool = $fileCompiler->compileNamespace($data);

// usage with all arguments
$bool = $fileCompiler->compileNamespace(&$data);
~~~~~

## Arguments

- `$data` `string`

## Return value

- `bool` Whether or not namespace changes were compiled
