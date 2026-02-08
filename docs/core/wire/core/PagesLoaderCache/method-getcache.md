# PagesLoaderCache::getCache()

Source: `wire/core/PagesLoaderCache.php`

Given a Page ID, return it if it's cached, or NULL of it's not.

If no ID is provided, then this will return an array copy of the full cache.

You may also pass in the string "id=123", where 123 is the page_id


@param int|string|null $id

@return Page|array|null
