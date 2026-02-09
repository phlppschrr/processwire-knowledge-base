# $fileCompiler->compileIncludesFileMatchType($fileMatch, $funcMatch): string|bool

Source: `wire/core/FileCompiler.php`

Returns fileMatch type of 'var', 'file', 'func' or boolean false if not valid

## Usage

~~~~~
// basic usage
$string = $fileCompiler->compileIncludesFileMatchType($fileMatch, $funcMatch);
~~~~~

## Arguments

- `$fileMatch` `string` The $fileMatch var from compileIncludes() method
- `$funcMatch` `string` include function name

## Return value

- `string|bool`
