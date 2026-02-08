# $pagesType->saveReady(Page $page): array

Source: `wire/core/PagesType.php`

Hook called just before a page of this type is saved

## Usage

~~~~~
// basic usage
$array = $pagesType->saveReady($page);

// usage with all arguments
$array = $pagesType->saveReady(Page $page);
~~~~~

## Hookable

- Hookable method name: `saveReady`
- Implementation: `___saveReady`
- Hook with: `$pagesType->saveReady()`

## Arguments

- `$page` `Page` The page about to be saved

## Return value

- `array` Optional extra data to add to pages save query.

## Since

3.0.128
