# $pages->insertBefore(Page $page, Page $beforePage)

Source: `wire/core/Pages.php`

Sort/move one page above another (for manually sorted pages)

## Usage

~~~~~
// basic usage
$result = $pages->insertBefore($page, $beforePage);

// usage with all arguments
$result = $pages->insertBefore(Page $page, Page $beforePage);
~~~~~

## Hookable

- Hookable method name: `insertBefore`
- Implementation: `___insertBefore`
- Hook with: `$pages->insertBefore()`

## Arguments

- `$page` `Page` Page you want to move/sort
- `$beforePage` `Page` Page you want to insert before

## Exceptions

- `WireException`
