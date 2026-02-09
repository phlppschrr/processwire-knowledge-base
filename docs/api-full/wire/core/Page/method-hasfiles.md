# $page->hasFiles(): bool

Source: `wire/core/Page.php`

Does the page have a files path and one or more files present in it?

This will only check if files exist, it will not create the directory if it’s not already present.

## Usage

~~~~~
// basic usage
$bool = $page->hasFiles();
~~~~~

## Return value

- `bool`

## See Also

- hasFilesPath()
- filesPath()
- filesManager()

## Since

3.0.138 Earlier versions must use the more verbose PagefilesManager::hasFiles($page)
