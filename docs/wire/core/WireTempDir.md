# WireTempDir

Source: `wire/core/WireTempDir.php`

ProcessWire Temporary Directory Manager

ProcessWire 3.x, Copyright 2018 by Ryan Cramer
https://processwire.com

## hiddenFileName

File automatically placed in created temp dirs for verification, contains timestamp

## __construct()

Construct

@param string|object $name DEPRECATED (Call 'init' method instead)

@param string $basePath DEPRECATED (Call 'init' method instead)

## __destruct()

Destruct

## init()

Initialize temporary directory

This method should only be called once per instance of this class. If you specified a $name argument
in the constructor, then you should not call this method because it will have already been called.

@param string|object $name Recommend providing the object that is using the temp dir, but can also be any string

@param string $basePath Base path where temp dirs should be created. Omit to use default (recommended).

@throws WireException if given a $root that doesn't exist

@return string Returns the root of the temporary directory. Use the get() method to get a dir for use.

## classRootPath()

Return the class root path for cache files (i.e. /path/to/site/assets/cache/WireTempDir/)

@param bool $createIfNotExists Create the directory if it does not exist? (default=false)

@param string $basePath Path to start from (default=/path/to/site/assets/cache/)

@return string

@throws WireException

@since 3.0.175

## createName()

Create a randomized name for runtime temp dir

@param string $prefix Optional prefix for name

@return string

## setRemove()

Call this with 'false' to prevent temp dir from being removed automatically when object is destructed

If you do this, then you accept responsibility for removing the directory by calling $tempDir->remove();
If you do not remove it yourself, WireTempDir will remove as part of the daily maintenance.

@param bool $remove

@return $this

## get()

Returns a temporary directory (path)

@param string $id Optional identifier to use (default=autogenerate)

@return string Returns path

@throws WireException If can't create temporary dir

## remove()

Removes the temporary directory created by this object

Note that the directory is automatically removed when this object is destructed.

@return bool

## removeExpiredDirs()

Remove expired directories in the given $path

Also removes $path if it's found that everything in it is expired.

@param string $path

@param int Max age in seconds

@return bool

## getNewestModTime()

Get the newest modification time of a file in $path, recursively

@param string $path Path to start from

@param int $maxDepth

@return int

## removeAll()

Clear all temporary directories created by this class

## __toString()

Accessing this object as a string returns the temp dir

@return string

## mkdir()

Create a temporary directory

@param string $dir

@param bool $recursive

@return bool

## rmdir()

Remove a temporary directory

@param string $dir

@param bool $recursive

@return bool

## isTempDir()

Is given directory/path created by this class?

@param string $dir

@return bool

## maintenance()

Perform maintenance by cleaning up old temporary directories

Note: This is done automatically if any temporary directories are created during the request.

@throws WireException

@return bool

@since 3.0.175

## create()

@deprecated Use init() method instead

@param string $name

@param string $basePath

@return string
