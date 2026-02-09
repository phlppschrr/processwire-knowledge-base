# Template: cache

Source: `wire/core/Template.php`

- $cacheTime: int Number of seconds pages using this template should cache for, or 0 for no cache. Negative values indicates setting used for external caching engine like ProCache.
- $noCacheGetVars: string GET vars that trigger disabling the cache (only when cache_time > 0)
- $noCachePostVars: string POST vars that trigger disabling the cache (only when cache_time > 0)
- $useCacheForUsers: int Use cache for: 0 = only guest users, 1 = guests and logged in users
- $cacheExpire: int Expire the cache for all pages when page using this template is saved? (1 = yes, 0 = no- only current page)
- $cacheExpirePages: array Array of Page IDs that should be expired, when cacheExpire == Template::cacheExpireSpecific
- $cacheExpireSelector: string Selector string matching pages that should be expired, when cacheExpire == Template::cacheExpireSelector
