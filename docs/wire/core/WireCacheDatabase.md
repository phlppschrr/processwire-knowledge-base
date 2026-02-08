# WireCacheDatabase

Source: `wire/core/WireCacheDatabase.php`

Database cache handler for WireCache

ProcessWire 3.x, Copyright 2024 by Ryan Cramer
https://processwire.com

@since 2.0.218

## find()

Find caches by names or expirations and return requested values

@param array $options
 - `names` (array): Names of caches to find (OR condition), optionally appended with wildcard `*`.
 - `expires` (array): Expirations of caches to match in ISO-8601 date format, prefixed with operator and space (see expiresMode mode below).
 - `expiresMode` (string): Whether it should match any one condition 'OR', or all conditions 'AND' (default='OR')
 - `get` (array): Properties to get in return value, one or more of [ `name`, `expires`, `data`, `size` ] (default=all)

@return array Returns array of associative arrays, each containing requested properties

## save()

Save a cache

@param string $name Name of cache

@param string $data Data to save in cache

@param string $expire String in ISO-8601 date format

@return bool

## delete()

Delete a cache by name

@param string $name

@return bool

## deleteAll()

Delete all caches (except those reserved by the system)

@return int

## expireAll()

Expire all caches (except those that should never expire)

@return int

## _deleteAll()

Implementation for deleteAll and expireAll methods

@param bool $expireAll

@return int

@throws WireException

## executeQuery()

Execute query

@param \PDOStatement $query

@return bool

## maintenance()

Database cache maintenance (every 10 minutes)

@param Template|Page $obj

@return bool

@throws WireException

@since 3.0.242

## install()

Create the caches table if it happens to have been deleted
