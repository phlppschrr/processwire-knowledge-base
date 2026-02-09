# $pagesPathFinder->getShortcutPagePaths(&$path): bool

Source: `wire/core/PagesPathFinder.php`

Find a shortcut using the PagePaths module

## Usage

~~~~~
// basic usage
$bool = $pagesPathFinder->getShortcutPagePaths($path);

// usage with all arguments
$bool = $pagesPathFinder->getShortcutPagePaths(&$path);
~~~~~

## Arguments

- `$path` `string`

## Return value

- `bool` Returns true if found, false if not installed or not found
