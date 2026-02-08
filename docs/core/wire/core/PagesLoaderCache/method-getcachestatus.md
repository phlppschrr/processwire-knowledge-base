# $pagesLoaderCache->getCacheStatus($verbose = null): array|string

Source: `wire/core/PagesLoaderCache.php`

Get cache status

Returns count of each cache type, or contents of each cache type of verbose option is specified.

## Usage

~~~~~
// basic usage
$array = $pagesLoaderCache->getCacheStatus();

// usage with all arguments
$array = $pagesLoaderCache->getCacheStatus($verbose = null);
~~~~~

## Arguments

- `$verbose` (optional) `bool|null` Specify true to get contents of cache, false to get string counts, or omit for array of counts

## Return value

- `array|string`

## Since

3.0.198
