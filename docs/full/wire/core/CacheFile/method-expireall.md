# CacheFile::expireAll()

Source: `wire/core/CacheFile.php`

Causes all cache files in this type to be immediately expired

Note it does not remove any files, only places a globalExpireFile with an mtime newer than the cache files
