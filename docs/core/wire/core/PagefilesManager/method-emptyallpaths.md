# PagefilesManager::emptyAllPaths()

Source: `wire/core/PagefilesManager.php`

Empties all file paths related to the Page, and removes the directories

This is the same as calling the `PagefilesManager:emptyPath()` method with the
`$rmdir` and `$recursive` options as both true.


@return bool True on success, false on error (since 3.0.17, previous versions had no return value).
