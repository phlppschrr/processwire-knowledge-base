# $pagesType->___saveReady(Page $page): array

Source: `wire/core/PagesType.php`

Hook called just before a page of this type is saved

## Usage

~~~~~
// basic usage
$array = $pagesType->___saveReady($page);

// usage with all arguments
$array = $pagesType->___saveReady(Page $page);
~~~~~

## Arguments

- `$page` `Page` The page about to be saved

## Return value

- `array` Optional extra data to add to pages save query.

## Since

3.0.128
