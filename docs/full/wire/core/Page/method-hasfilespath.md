# $page->hasFilesPath(): bool

Source: `wire/core/Page.php`

Does the page have a files path for storing files?

This will only check if files path exists, it will not create the path if it’s not already present.

## Return value

bool

## See also

- hasFiles()
- filesManager()

## Meta

- @since 3.0.138 Earlier versions must use the more verbose PagefilesManager::hasPath($page)
