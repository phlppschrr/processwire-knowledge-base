# $templateFile->fileFailed($filename, \Exception $e): bool

Source: `wire/core/TemplateFile.php`

Called when render of specific file failed with Exception

## Usage

~~~~~
// basic usage
$bool = $templateFile->fileFailed($filename, $e);

// usage with all arguments
$bool = $templateFile->fileFailed($filename, \Exception $e);
~~~~~

## Hookable

- Hookable method name: `fileFailed`
- Implementation: `___fileFailed`
- Hook with: `$templateFile->fileFailed()`

## Arguments

- `$filename` `string`
- `$e` `\Exception`

## Return value

- `bool` True if Exception $e should be thrown, false if it should be ignored

## Since

3.0.154
