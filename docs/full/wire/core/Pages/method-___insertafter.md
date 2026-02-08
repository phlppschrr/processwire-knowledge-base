# $pages->___insertAfter(Page $page, Page $afterPage)

Source: `wire/core/Pages.php`

Sort/move one page after another (for manually sorted pages)

## Usage

~~~~~
// basic usage
$result = $pages->___insertAfter($page, $afterPage);

// usage with all arguments
$result = $pages->___insertAfter(Page $page, Page $afterPage);
~~~~~

## Arguments

- `$page` `Page` Page you want to move/sort
- `$afterPage` `Page` Page you want to insert after

## Exceptions

- `WireException`
