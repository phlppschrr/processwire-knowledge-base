# CacheFile::__construct()

Source: `wire/core/CacheFile.php`

Construct the CacheFile

@param string $path Path where cache files will be created

@param string|int $id An identifier for this particular cache, unique from others.
	Or leave blank if you are instantiating this class for no purpose except to expire cache files (optional).

@param int $cacheTimeSeconds The number of seconds that this cache file remains valid

@throws WireException
