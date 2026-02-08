# $fileCompiler->compile($sourceFile): string

Source: `wire/core/FileCompiler.php`

Compile given source file and return compiled destination file

## Usage

~~~~~
// basic usage
$string = $fileCompiler->compile($sourceFile);
~~~~~

## Hookable

- Hookable method name: `compile`
- Implementation: `___compile`
- Hook with: `$fileCompiler->compile()`

## Arguments

- `$sourceFile` `string` Source file to compile (relative to sourcePath given in constructor)

## Return value

- `string` Full path and filename of compiled file. Returns sourceFile is compilation is not necessary.

## Exceptions

- `WireException` if given invalid sourceFile
