# WireTempDir::init()

Source: `wire/core/WireTempDir.php`

Initialize temporary directory

This method should only be called once per instance of this class. If you specified a $name argument
in the constructor, then you should not call this method because it will have already been called.

@param string|object $name Recommend providing the object that is using the temp dir, but can also be any string

@param string $basePath Base path where temp dirs should be created. Omit to use default (recommended).

@throws WireException if given a $root that doesn't exist

@return string Returns the root of the temporary directory. Use the get() method to get a dir for use.
