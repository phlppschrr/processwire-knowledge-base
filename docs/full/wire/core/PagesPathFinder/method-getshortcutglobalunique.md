# $pagesPathFinder->getShortcutGlobalUnique(&$path): bool

Source: `wire/core/PagesPathFinder.php`

Attempt to match a page with status 'unique' or having parent_id=1

This method only proceeds if the path contains no slashes, meaning it is 1-level from root.

## Arguments

- string $path

## Return value

bool
