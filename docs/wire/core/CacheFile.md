# CacheFile

Source: `wire/core/CacheFile.php`

ProcessWire CacheFile

Class to manage individual cache files

Each cache file creates it's own directory based on the '$id' given.
The dir is created so that secondary cache files can be created too,
and these are automatically removed when the remove() method is called.

This file is licensed under the MIT license
https://processwire.com/about/license/mit/

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com

## maxCacheFiles

Max secondaryID cache files that will be allowed in a directory before it starts removing them.

## __construct()

Construct the CacheFile

@param string $path Path where cache files will be created

@param string|int $id An identifier for this particular cache, unique from others.
	Or leave blank if you are instantiating this class for no purpose except to expire cache files (optional).

@param int $cacheTimeSeconds The number of seconds that this cache file remains valid

@throws WireException

## setSecondaryID()

An extra part to be appended to the filename

When a call to remove the cache is included, then all 'secondary' versions of it will be included too

@param string|int $id

## buildFilename()

Build a filename for use by the cache

Filename takes this form: /path/primaryID/primaryID.cache
Or /path/primaryID/secondaryID.cache

@return string

## exists()

Does the cache file exist?

@return bool

## get()

Get the contents of the cache based on the primary or secondary ID

@return string

## isCacheFileExpired()

Is the given cache filename expired?

@param string $filename

@return bool

## save()

Saves $data to the cache

@param string $data

@return bool

## remove()

Removes all cache files for primaryID

If any secondaryIDs were used, those are removed too

## removeFilename()

Removes just the given file, as opposed to remove() which removes the entire cache for primaryID

@param string $filename

## expireAll()

Causes all cache files in this type to be immediately expired

Note it does not remove any files, only places a globalExpireFile with an mtime newer than the cache files

## setChmodFile()

Set the octal mode for files created by CacheFile

@param string $mode

@deprecated No longer used

## setChmodDir()

Set the octal mode for dirs created by CacheFile

@param string $mode

@deprecated No longer used

## __toString()

CacheFile classes return a string of their cache filename
