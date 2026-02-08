# Template: cache

Source: `wire/core/Template.php`

@property int $cacheTime Number of seconds pages using this template should cache for, or 0 for no cache. Negative values indicates setting used for external caching engine like ProCache.

@property string $noCacheGetVars GET vars that trigger disabling the cache (only when cache_time > 0)

@property string $noCachePostVars POST vars that trigger disabling the cache (only when cache_time > 0)

@property int $useCacheForUsers Use cache for: 0 = only guest users, 1 = guests and logged in users

@property int $cacheExpire Expire the cache for all pages when page using this template is saved? (1 = yes, 0 = no- only current page)

@property array $cacheExpirePages Array of Page IDs that should be expired, when cacheExpire == Template::cacheExpireSpecific

@property string $cacheExpireSelector Selector string matching pages that should be expired, when cacheExpire == Template::cacheExpireSelector
