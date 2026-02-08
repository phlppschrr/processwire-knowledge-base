# PagesLoaderCache::uncacheAll()

Source: `wire/core/PagesLoaderCache.php`

Remove all pages from the cache


@param Page|null $page Optional Page that initiated the uncacheAll

@param array $options Additional options to modify behavior:
  - `shallow` (bool): By default, this method also calls $page->uncache(). To prevent call to $page->uncache(), set 'shallow' => true.

@return int Number of pages uncached
