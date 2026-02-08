# $wireCacheDatabase->find(array $options): array

Source: `wire/core/WireCacheDatabase.php`

Find caches by names or expirations and return requested values

## Arguments

- `$options` `array` - `names` (array): Names of caches to find (OR condition), optionally appended with wildcard `*`. - `expires` (array): Expirations of caches to match in ISO-8601 date format, prefixed with operator and space (see expiresMode mode below). - `expiresMode` (string): Whether it should match any one condition 'OR', or all conditions 'AND' (default='OR') - `get` (array): Properties to get in return value, one or more of [ `name`, `expires`, `data`, `size` ] (default=all)

## Return value

array Returns array of associative arrays, each containing requested properties
