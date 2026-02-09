# $pagesLoaderCache->uncacheAll(?Page $page = null, array $options = array()): int

Source: `wire/core/PagesLoaderCache.php`

Remove all pages from the cache

## Usage

~~~~~
// basic usage
$int = $pagesLoaderCache->uncacheAll();

// usage with all arguments
$int = $pagesLoaderCache->uncacheAll(?Page $page = null, array $options = array());
~~~~~

## Arguments

- `$page` (optional) `Page|null` Optional Page that initiated the uncacheAll
- `$options` (optional) `array` Additional options to modify behavior: - `shallow` (bool): By default, this method also calls $page->uncache(). To prevent call to $page->uncache(), set 'shallow' => true.

## Return value

- `int` Number of pages uncached
