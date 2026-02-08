# PagesPathFinder::getShortcutExcludeRoot()

Source: `wire/core/PagesPathFinder.php`

Find out if we can early exit 404 based on the root segment

Unlike other shortcuts, this one is an exclusion shortcut:
Returns false if the root segment matched and further analysis should take place.
Returns true if root segment is not in this site and 404 should be the result.

@param string $path

@return bool
