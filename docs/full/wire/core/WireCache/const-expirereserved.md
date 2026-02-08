# WireCache::expireReserved

Source: `wire/core/WireCache.php`

Cache should never expire and should not be deleted during deleteAll() calls (for PW internal system use)
Can only be deleted by delete() calls that specify it directly or match it specifically with a wildcard.
