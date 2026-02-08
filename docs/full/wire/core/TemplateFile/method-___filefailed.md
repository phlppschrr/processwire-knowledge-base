# $templateFile->___fileFailed($filename, \Exception $e): bool

Source: `wire/core/TemplateFile.php`

Called when render of specific file failed with Exception

## Usage

~~~~~
// basic usage
$bool = $templateFile->___fileFailed($filename, $e);

// usage with all arguments
$bool = $templateFile->___fileFailed($filename, \Exception $e);
~~~~~

## Arguments

- `$filename` `string`
- `$e` `\Exception`

## Return value

- `bool` True if Exception $e should be thrown, false if it should be ignored

## Since

3.0.154
