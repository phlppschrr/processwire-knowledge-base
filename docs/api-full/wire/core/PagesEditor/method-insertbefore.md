# $pagesEditor->insertBefore(Page $page, Page $sibling, $after = false)

Source: `wire/core/PagesEditor.php`

Sort one page before another (for pages using manual sort)

Note that if given $sibling parent is different from `$page` parent, then the `$pages->save()`
method will also be called to perform that movement.

## Usage

~~~~~
// basic usage
$result = $pagesEditor->insertBefore($page, $sibling);

// usage with all arguments
$result = $pagesEditor->insertBefore(Page $page, Page $sibling, $after = false);
~~~~~

## Arguments

- `$page` `Page` Page to move/sort
- `$sibling` `Page` Sibling that page will be moved/sorted before
- `$after` (optional) `bool` Specify true to make $page move after $sibling instead of before (default=false)

## Exceptions

- `WireException` When conditions don't allow page insertions
