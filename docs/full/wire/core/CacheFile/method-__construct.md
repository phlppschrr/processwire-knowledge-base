# $cacheFile->__construct($path, $id, $cacheTimeSeconds)

Source: `wire/core/CacheFile.php`

Construct the CacheFile

## Usage

~~~~~
// basic usage
$result = $cacheFile->__construct($path, $id, $cacheTimeSeconds);
~~~~~

## Arguments

- `$path` `string` Path where cache files will be created
- `$id` (optional) `string|int` An identifier for this particular cache, unique from others. Or leave blank if you are instantiating this class for no purpose except to expire cache files (optional).
- `$cacheTimeSeconds` `int` The number of seconds that this cache file remains valid

## Exceptions

- `WireException`
