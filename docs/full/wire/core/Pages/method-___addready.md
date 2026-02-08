# $pages->addReady(Page $page)

Source: `wire/core/Pages.php`

Hook called when a new page is about to be added and saved to the database

## Usage

~~~~~
// basic usage
$result = $pages->addReady($page);

// usage with all arguments
$result = $pages->addReady(Page $page);
~~~~~

## Hookable

- Hookable method name: `addReady`
- Implementation: `___addReady`
- Hook with: `$pages->addReady()`

## Arguments

- `$page` `Page`

## Since

3.0.253
