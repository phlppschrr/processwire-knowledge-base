# $page->filesUrl(): string

Source: `wire/core/Page.php`

Returns the URL for files, creating it if it does not yet exist

## Usage

~~~~~
// basic usage
$string = $page->filesUrl();
~~~~~

## Return value

- `string`

## See Also

- filesPath()
- filesManager()

## Since

3.0.138 You can use the equivalent but more verbose `$page->filesManager()->url()` in any version
