# $pagesLoaderCache->getSelectorCache($selector, $options, $returnSelector = false): array|null|string|PageArray

Source: `wire/core/PagesLoaderCache.php`

Retrieve any cached page IDs for the given selector and options OR false if none found.

You may specify a third param as TRUE, which will cause this to just return the selector string (with hashed options)

## Arguments

- string $selector
- array $options
- bool $returnSelector default false

## Return value

array|null|string|PageArray
