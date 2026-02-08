# WireCache::preload()

Source: `wire/core/WireCache.php`

Preload the given caches, so that they will be returned without query on the next get() call

After a preloaded cache is returned from a get() call, it is removed from local storage.


@param array $names

@param int|string|null $expire

@deprecated
