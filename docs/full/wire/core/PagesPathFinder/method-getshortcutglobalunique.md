# $pagesPathFinder->getShortcutGlobalUnique(&$path): bool

Source: `wire/core/PagesPathFinder.php`

Attempt to match a page with status 'unique' or having parent_id=1

This method only proceeds if the path contains no slashes, meaning it is 1-level from root.

## Usage

~~~~~
// basic usage
$bool = $pagesPathFinder->getShortcutGlobalUnique($path);

// usage with all arguments
$bool = $pagesPathFinder->getShortcutGlobalUnique(&$path);
~~~~~

## Arguments

- `$path` `string`

## Return value

- `bool`
