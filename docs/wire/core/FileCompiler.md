# FileCompiler

Source: `wire/core/FileCompiler.php`

FileCompiler

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

@todo determine whether we should make storage in dedicated table rather than using wire('cache').

@todo handle race conditions for multiple requests attempting to compile the same file(s).

## other

@method string compile($sourceFile)

@method string compileData($data, $sourceFile)

## __construct()

Construct

@param string $sourcePath Path where source files are located

@param array $options Indicate which compilations should be performed (default='includes' and 'namespace')

## wired()

Wired to instance

## init()

Initialize paths

@throws WireException

## mkdir()

Make a directory with proper permissions

@param string $path Path of directory to create

@param bool $recursive Default is true

@return bool

## chmod()

Change file to correct mode for FileCompiler

@param string $filename

@return bool

## initTargetPath()

Initialize the target path, making sure that it exists and creating it if not

@throws WireException

## initRawPHP()

Populate the $this->rawPHP data which contains only raw php without quoted values

@param string $data

## allowCompile()

Allow the given filename to be compiled?

@param string $filename Full path and filename to compile (this property can be modified by the function).

@param string $basename Just the basename (this property can be modified by the function).

@return bool

## ___compile()

Compile given source file and return compiled destination file

@param string $sourceFile Source file to compile (relative to sourcePath given in constructor)

@return string Full path and filename of compiled file. Returns sourceFile is compilation is not necessary.

@throws WireException if given invalid sourceFile

## ___compileData()

Compile the given string of data

@param string $data

@param string $sourceFile

@return string

## compileComments()

Compile comments so that they can be easily identified by other compiler methods

@todo this is a work in progress, not yet in use

@param $data

## compileIncludes()

Compile include(), require() (and variations) to refer to compiled files where possible

@param string $data

@param string $sourceFile

## compileIncludesValidLineOpen()

Test the given line $open preceding an include statement for validity

@param string $open

@return bool Returns true if valid, false if not

## compileIncludesFileMatchType()

Returns fileMatch type of 'var', 'file', 'func' or boolean false if not valid

@param string $fileMatch The $fileMatch var from compileIncludes() method

@param string $funcMatch include function name

@return string|bool

## compileNamespace()

Compile global class/interface/function references to namespaced versions

@param string $data

@return bool Whether or not namespace changes were compiled

## copyAllNewerFiles()

Recursively copy all files from $source to $target, but only if $source file is $newer

@param string $source

@param string $target

@param bool $recursive

@return int Number of files copied

## getNumCacheFiles()

Get a count of how many files are in the cache

@param bool $all Specify true to get a count for all file compiler caches

@param string $targetPath for internal recursion use, public calls should omit this

@return int

## clearCache()

Clear all file compiler caches

@param bool $all Specify true to clear for all FileCompiler caches

@return bool

## maintenance()

Run maintenance on the FileCompiler cache

This should be called at the end of each request.

@param int $interval Number of seconds between maintenance runs (default=86400)

@return bool Whether or not it was necessary to run maintenance

## _maintenance()

Implementation for maintenance on a given path

Logs maintenance actions to logs/file-compiler.txt

@param $sourcePath

@param $targetPath

@return bool

## optionsToString()

Given an array of $options convert to an PHP-code array() string

@param array $options

@return string

## addExclusion()

Exclude a file or path from compilation

@param string $pathname

## touch()

Same as PHP touch() but with fallbacks for cases where touch() does not work

@param string $filename

@param null|int $time

@return bool
