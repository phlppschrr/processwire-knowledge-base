# PagesLoaderCache::getSelectorCache()

Source: `wire/core/PagesLoaderCache.php`

Retrieve any cached page IDs for the given selector and options OR false if none found.

You may specify a third param as TRUE, which will cause this to just return the selector string (with hashed options)


@param string $selector

@param array $options

@param bool $returnSelector default false

@return array|null|string|PageArray
