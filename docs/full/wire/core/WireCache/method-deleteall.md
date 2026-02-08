# WireCache::deleteAll()

Source: `wire/core/WireCache.php`

Delete all caches (where allowed)

This method deletes all caches other than those with `WireCache::expireReserved` status.

@return int Quantity of caches deleted

@since 3.0.130
