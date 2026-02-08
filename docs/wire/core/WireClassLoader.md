# WireClassLoader

Source: `wire/core/WireClassLoader.php`

ProcessWire class autoloader

Similar to a PSR-4 autoloader but with knowledge of modules.

The ProcessWire $classLoader API variable handles autoloading of classes and modules.
This class loader is similar to a PSR-4 autoloader but with knowledge of modules.

This file is licensed under the MIT license
https://processwire.com/about/license/mit/

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com

## __construct()

@param ProcessWire $wire

## path()

Normalize a path

@param string $path

@return string

@since 3.0.152

## addExtension()

Add a recognized file extension for PHP files

Note: ".php" is already assumed, so does not need to be added.


@param string $ext

## addSuffix()

Map a class suffix to a path

This is used as a helper/fallback and class is not required to be in given path,
but the path will be added as another to check when not found in namespace path(s).

@param string $suffix Case sensitive suffix specific to class name (not namespace).

@param string $path

## addPrefix()

Map a class prefix to a path

This is used as a helper/fallback and class is not required to be in given path,
but the path will be added as another to check when not found in namespace path(s).

@param string $prefix Case sensitive prefix specific to class name (not namespace).

@param string $path

## addNamespace()

Add a namespace to point to a path root

Multiple root paths may be specified for a single namespace by calling this method more than once.

~~~~~
$classLoader->addNamespace('HelloWorld', '/path/to/that/');
~~~~~

@param string $namespace

@param string $path Full system path

## getNamespace()

Return array of paths for the given namespace, or empty array if none found

@param string $namespace

@return array of paths or empty array if none found

## hasNamespace()

Return true if namespace is defined with paths or false if not

@param string $namespace

@return bool

## removeNamespace()

Remove defined paths (or single path) for given namespace

@param string $namespace

@param string $path Optionally specify path to remove (default=remove all)

## findClassFile()

Find filename for given class name (primarily for API testing/debugging purposes)

@param string $className Class name with namespace

@return bool|string Returns file on success or boolean false when not found

@since 3.0.152

## loadClass()

Load the file for the given class


@param string $className

## findClassInPaths()

Find class file among given paths and return full pathname to file if found

@param string $name Class name without namespace

@param string|array $paths Path(s) to check

@param string $dir Optional directory string to append to each path, must not start with slash but must end with slash, i.e. "dir/"

@return string|bool Returns full path+filename when found or boolean false when not found

@since 3.0.152

## findInPrefixSuffixPaths()

Check prefix and suffix definition paths for given class name and return file if found

@param string $name Class name without namespace

@return bool|string Returns filename on success or boolean false if not found

@since 3.0.152
