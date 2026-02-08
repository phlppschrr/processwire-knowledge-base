# $pages->insertAfter(Page $page, Page $afterPage)

Source: `wire/core/Pages.php`

Sort/move one page after another (for manually sorted pages)

## Usage

~~~~~
// basic usage
$result = $pages->insertAfter($page, $afterPage);

// usage with all arguments
$result = $pages->insertAfter(Page $page, Page $afterPage);
~~~~~

## Hookable

- Hookable method name: `insertAfter`
- Implementation: `___insertAfter`
- Hook with: `$pages->insertAfter()`

## Arguments

- `$page` `Page` Page you want to move/sort
- `$afterPage` `Page` Page you want to insert after

## Exceptions

- `WireException`
