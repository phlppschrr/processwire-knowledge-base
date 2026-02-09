# $page->hasFilesPath(): bool

Source: `wire/core/Page.php`

Does the page have a files path for storing files?

This will only check if files path exists, it will not create the path if it’s not already present.

## Usage

~~~~~
// basic usage
$bool = $page->hasFilesPath();
~~~~~

## Return value

- `bool`

## See Also

- hasFiles()
- filesManager()

## Since

3.0.138 Earlier versions must use the more verbose PagefilesManager::hasPath($page)
