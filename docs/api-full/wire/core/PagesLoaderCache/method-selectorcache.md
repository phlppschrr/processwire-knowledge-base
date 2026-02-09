# $pagesLoaderCache->selectorCache($selector, array $options, PageArray $pages): bool

Source: `wire/core/PagesLoaderCache.php`

Cache the given selector string and options with the given PageArray

## Usage

~~~~~
// basic usage
$bool = $pagesLoaderCache->selectorCache($selector, $options, $pages);

// usage with all arguments
$bool = $pagesLoaderCache->selectorCache($selector, array $options, PageArray $pages);
~~~~~

## Arguments

- `$selector` `string`
- `$options` `array`
- `$pages` `PageArray`

## Return value

- `bool` True if pages were cached, false if not
