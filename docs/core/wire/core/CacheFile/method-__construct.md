# $cacheFile->__construct($path, $id, $cacheTimeSeconds)

Source: `wire/core/CacheFile.php`

Construct the CacheFile

## Arguments

- string $path Path where cache files will be created
- string|int $id An identifier for this particular cache, unique from others. Or leave blank if you are instantiating this class for no purpose except to expire cache files (optional).
- int $cacheTimeSeconds The number of seconds that this cache file remains valid

## Throws

- WireException
