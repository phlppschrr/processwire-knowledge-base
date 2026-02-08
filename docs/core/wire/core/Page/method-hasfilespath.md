# Page::hasFilesPath()

Source: `wire/core/Page.php`

Does the page have a files path for storing files?

This will only check if files path exists, it will not create the path if it’s not already present.


@return bool

@since 3.0.138 Earlier versions must use the more verbose PagefilesManager::hasPath($page)

@see hasFiles(), filesManager()
