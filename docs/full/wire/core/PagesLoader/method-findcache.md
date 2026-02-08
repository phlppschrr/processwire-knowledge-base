# PagesLoader::findCache()

Source: `wire/core/PagesLoader.php`

Find pages and cache the result for specified period of time

Use this when you want to cache a slow or complex page finding operation so that it doesn’t
have to be repated for every web request. Note that this only caches the find operation
and not the loading of the found pages.

~~~~~
$items = $pages->findCache("title%=foo"); // 60 seconds (default)
$items = $pages->findCache("title%=foo", 3600); // 1 hour
$items = $pages->findCache("title%=foo", "+1 HOUR");  // same as above
~~~~~


@param string|array|Selectors $selector

@param int|string|bool|null $expire When the cache should expire, one of the following:
 - Max age integer (in seconds).
 - Any string accepted by PHP’s `strtotime()` that specifies when the cache should be expired.
 - Any `WireCache::expire…` constant or anything accepted by the `WireCache::get()` $expire argument.

@param array $options Options to pass to `$pages->getByIDs()`, or:
 - `findIDs` (bool): Return just the page IDs rather then the actual pages? (default=false)

@return PageArray|array

@since 3.0.218
