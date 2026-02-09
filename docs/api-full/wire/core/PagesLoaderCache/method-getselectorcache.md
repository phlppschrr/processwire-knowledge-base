# $pagesLoaderCache->getSelectorCache($selector, $options, $returnSelector = false): array|null|string|PageArray

Source: `wire/core/PagesLoaderCache.php`

Retrieve any cached page IDs for the given selector and options OR false if none found.

You may specify a third param as TRUE, which will cause this to just return the selector string (with hashed options)

## Usage

~~~~~
// basic usage
$array = $pagesLoaderCache->getSelectorCache($selector, $options);

// usage with all arguments
$array = $pagesLoaderCache->getSelectorCache($selector, $options, $returnSelector = false);
~~~~~

## Arguments

- `$selector` `string`
- `$options` `array`
- `$returnSelector` (optional) `bool` default false

## Return value

- `array|null|string|PageArray`
