# $page->filesPath(): string

Source: `wire/core/Page.php`

Returns the path for files, creating it if it does not yet exist

## Usage

~~~~~
// basic usage
$string = $page->filesPath();
~~~~~

## Return value

- `string`

## See Also

- filesUrl()
- hasFilesPath()
- hasFiles()
- filesManager()

## Since

3.0.138 You can also use the equivalent but more verbose `$page->filesManager()->path()` in any version
