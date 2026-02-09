# $pagesParents->movePage(Page $page, Page $oldParent, Page $newParent): int

Source: `wire/core/PagesParents.php`

Rebuild pages_parents table for given page (experimental faster alternative/rewrite of rebuild method)

## Usage

~~~~~
// basic usage
$int = $pagesParents->movePage($page, $oldParent, $newParent);

// usage with all arguments
$int = $pagesParents->movePage(Page $page, Page $oldParent, Page $newParent);
~~~~~

## Arguments

- `$page` `Page`
- `$oldParent` `Page`
- `$newParent` `Page`

## Return value

- `int`

## Exceptions

- `WireException`

## Since

3.0.212
