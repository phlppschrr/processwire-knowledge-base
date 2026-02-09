# CacheFile

Source: `wire/core/CacheFile.php`

Inherits: `Wire`

ProcessWire CacheFile

Class to manage individual cache files

Each cache file creates it's own directory based on the '$id' given.
The dir is created so that secondary cache files can be created too,
and these are automatically removed when the remove() method is called.

This file is licensed under the MIT license
https://processwire.com/about/license/mit/

Methods:
Method: [__construct()](method-__construct.md)
Method: [setSecondaryID()](method-setsecondaryid.md)
Method: [buildFilename()](method-buildfilename.md)
Method: [exists()](method-exists.md)
Method: [get()](method-get.md)
Method: [isCacheFileExpired()](method-iscachefileexpired.md)
Method: [save()](method-save.md)
Method: [remove()](method-remove.md)
Method: [removeFilename()](method-removefilename.md)
Method: [expireAll()](method-expireall.md)
Method: [setChmodFile()](method-setchmodfile.md)
Method: [setChmodDir()](method-setchmoddir.md)
Method: [__toString()](method-__tostring.md)

Constants:
Const: [maxCacheFiles](const-maxcachefiles.md)
