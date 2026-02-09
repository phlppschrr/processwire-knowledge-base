# $pagesEditor->sortRebuild(Page $parent): int

Source: `wire/core/PagesEditor.php`

Rebuild the “sort” values for all children of the given $parent page, fixing duplicates and gaps

If used on a $parent not currently sorted by by “sort” then it will update the “sort” index to be
consistent with whatever the pages are sorted by.

## Usage

~~~~~
// basic usage
$int = $pagesEditor->sortRebuild($parent);

// usage with all arguments
$int = $pagesEditor->sortRebuild(Page $parent);
~~~~~

## Arguments

- `$parent` `Page`

## Return value

- `int`
