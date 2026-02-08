# $pagesRawFinder->findIDs($selector, $verbose, array $options = array()): array

Source: `wire/core/PagesRaw.php`

Front-end to pages.findIDs that optionally accepts array of page IDs

## Usage

~~~~~
// basic usage
$array = $pagesRawFinder->findIDs($selector, $verbose);

// usage with all arguments
$array = $pagesRawFinder->findIDs($selector, $verbose, array $options = array());
~~~~~

## Arguments

- `$selector` `array|string|Selectors`
- `$verbose` `bool|string` One of true, false, or '*'
- `$options` (optional) `array`

## Return value

- `array`

## Exceptions

- `WireException`
