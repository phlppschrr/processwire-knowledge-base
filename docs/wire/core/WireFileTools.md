# WireFileTools

Source: `wire/core/WireFileTools.php`

ProcessWire File Tools ($files API variable)

Helpers for working with files and directories.

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com

## other

@method bool include($filename, array $vars = array(), array $options = array())

## __destruct()

Destruct

## mkdir()

Create a directory that is writable to ProcessWire and uses the defined $config chmod settings

Unlike PHP's `mkdir()` function, this function manages the read/write mode consistent with ProcessWire's
setting `$config->chmodDir`, and it can create directories recursively. Meaning, if you want to create directory /a/b/c/
and directory /a/ doesn't yet exist, this method will take care of creating /a/, /a/b/, and /a/b/c/.

The `$recursive` and `$chmod` arguments may optionally be swapped (since 3.0.34).

~~~~~
// Create a new directory in ProcessWire's cache dir
if($files->mkdir($config->paths->cache . 'foo-bar/')) {
  // directory created: /site/assets/cache/foo-bar/
}
~~~~~


@param string $path Directory you want to create

@param bool|string $recursive If set to true, all directories will be created as needed to reach the end.

@param string|null|bool $chmod Optional mode to set directory to (default: $config->chmodDir), format must be a string i.e. "0755"
  If omitted, then ProcessWire's `$config->chmodDir` setting is used instead.

@return bool True on success, false on failure

## rmdir()

Remove a directory and optionally everything within it (recursively)

Unlike PHP's `rmdir()` function, this method provides a recursive option, which can be enabled by specifying true
for the `$recursive` argument. You should be careful with this option, as it can easily wipe out an entire
directory tree in a flash.

Note that the $options argument was added in 3.0.118.

~~~~~
// Remove directory /site/assets/cache/foo-bar/ and everything in it
$files->rmdir($config->paths->cache . 'foo-bar/', true);

// Remove directory after ensuring $pathname is somewhere within /site/assets/
$files->rmdir($pathname, true, [ 'limitPath' => $config->paths->assets ]);
~~~~~


@param string $path Path/directory you want to remove

@param bool $recursive If set to true, all files and directories in $path will be recursively removed as well (default=false).

@param array|bool|string $options Optional settings to adjust behavior or (bool|string) for limitPath option:
 - `limitPath` (string|bool|array): Must be somewhere within given path, boolean true for site assets, or false to disable (default=false).
 - `throw` (bool): Throw verbose WireException (rather than return false) when potentially consequential fail (default=false).

@return bool True on success, false on failure

## chmod()

Change the read/write mode of a file or directory, consistent with ProcessWire's configuration settings

Unless a specific mode is provided via the `$chmod` argument, this method uses the `$config->chmodDir`
and `$config->chmodFile` settings in /site/config.php.

This method also provides the option of going recursive, adjusting the read/write mode for an entire
file/directory tree at once.

The `$recursive` or `$chmod` arguments may be optionally swapped in order (since 3.0.34).

~~~~~
// Update the mode of /site/assets/cache/foo-bar/ recursively
$files->chmod($config->paths->cache . 'foo-bar/', true);
~~~~~


@param string $path Path or file that you want to adjust mode for (may be a path/directory or a filename).

@param bool|string $recursive If set to true, all files and directories in $path will be recursively set as well (default=false).

@param string|null|bool $chmod If you want to set the mode to something other than ProcessWire's chmodFile/chmodDir settings,
you may override it by specifying it here. Ignored otherwise. Format should be a string, like "0755".

@return bool Returns true if all changes were successful, or false if at least one chmod failed.

@throws WireException when it receives incorrect chmod format

## copy()

Copy all files recursively from one directory ($src) to another directory ($dst)

Unlike PHP's `copy()` function, this method performs a recursive copy by default,
ensuring that all files and directories in the source ($src) directory are duplicated
in the destination ($dst) directory.

This method can also be used to copy single files. If a file is specified for $src, and
only a path is specified for $dst, then the original filename will be retained in $dst.

~~~~~
// Copy everything from /site/assets/cache/foo/ to /site/assets/cache/bar/
$copyFrom = $config->paths->cache . "foo/";
$copyTo = $config->paths->cache . "bar/";
$files->copy($copyFrom, $copyTo);
~~~~~


@param string $src Path to copy files from, or filename to copy.

@param string $dst Path (or filename) to copy file(s) to. Directory is created if it doesn't already exist.

@param bool|array $options Array of options:
 - `recursive` (bool): Whether to copy directories within recursively. (default=true)
 - `allowEmptyDirs` (boolean): Copy directories even if they are empty? (default=true)
 - `limitPath` (bool|string|array): Limit copy to within path given here, or true for site assets path.
    The limitPath option requires core 3.0.118+. (default=false).
 - `hidden` (bool): Also copy hidden files/directories within given $src directory? (applies only if $src is dir)
    The hidden option requires core 3.0.180+. (default=true)
 - If a boolean is specified for $options, it is assumed to be the `recursive` option.

@return bool True on success, false on failure.

@throws WireException if `limitPath` option is used and either $src or $dst is not allowed

## unlink()

Unlink/delete file with additional protections relative to PHP unlink()

- This method requires a full pathname to a file to unlink and does not
  accept any kind of relative path traversal.

- This method will be limited to unlink files only in /site/assets/ if you
  specify `true` for the `$limitPath` option (recommended).


@param string $filename

@param string|bool $limitPath Limit only to files within some starting path? (default=false)
 - Boolean true to limit unlink operations to somewhere within /site/assets/ (only known always writable path).
 - Boolean false to disable to security feature. (default)
 - An alternative path (string) that represents the starting path (full disk path) to limit deletions to.
 - An array with multiple of the above string option.

@param bool $throw Throw exception on error?

@return bool True on success, false on fail

@throws WireException If file is not allowed to be removed or unlink fails

@since 3.0.118

## rename()

Rename a file or directory and update permissions

Note that this method will fail if pathname given by $newName argument already exists.


@param string $oldName Old pathname, must be full disk path.

@param string $newName New pathname, must be full disk path OR can be basename to assume same path as $oldName.

@param array|bool|string $options Options array to modify behavior or substitute `limitPath` (bool or string) option here.
 - `limitPath` (bool|string|array): Limit renames to within this path, or boolean TRUE for site/assets, or FALSE to disable (default=false).
 - `throw` (bool): Throw WireException with verbose details on error? (default=false)
 - `chmod` (bool): Adjust permissions to be consistent with $config after rename? (default=true)
 - `copy` (bool): Use copy-then-delete method rather than a file system rename. (default=false) 3.0.178+
 - `retry` (bool): Retry with 'copy' method if regular rename files, applies only if copy option is false. (default=true) 3.0.178+
 - If given a bool or string for $options the `limitPath` option is assumed.

@return bool True on success, false on fail (or WireException if throw option specified).

@throws WireException If error occurs and $throw argument was true.

@since 3.0.118

## renameCopy()

Rename by first copying files to destination and then deleting source files

The operation is considered successful so long as the source files were able to be copied to the destination.
If source files cannot be deleted afterwards, the warning is logged, plus a warning notice is also shown when in debug mode.


@param string $oldName Old pathname, must be full disk path.

@param string $newName New pathname, must be full disk path OR can be basename to assume same path as $oldName.

@param array $options See options for rename() method

@return bool

@throws WireException

@since 3.0.178

## exists()

Does the given file/link/dir exist?

Thie method accepts an `$options` argument that can be specified as an array
or a string (space or comma separated). The examples here demonstrate usage as
a string since it is the simplest for readability.

- This function may return false for symlinks pointing to non-existing
  files, unless you specify `link` as the `type`.
- Specifying `false` for the `readable` or `writable` argument disables the
  option from being used, it doesn’t perform a NOT condition.
- The `writable` option may also be written as `writeable`, if preferred.

~~~~~
// 1. check if exists
$exists = $files->exists('/path/file.ext');

// 2. check if exists and is readable (or writable)
$exists = $files->exists('/path/file.ext', 'readable');
$exists = $files->exists('/path/file.ext', 'writable');

// 3. check if exists and is file, link or dir
$exists = $files->exists('/path/file.ext', 'file');
$exists = $files->exists('/path/file.ext', 'link');
$exists = $files->exists('/path/file.ext', 'dir');

// 4. check if exists and is writable file or dir
$exists = $files->exists('/path/file.ext', 'writable file');
$exists = $files->exists('/path/dir/', 'writable dir');

// 5. check if exists and is readable and writable file
$exists = $files->exists('/path/file.ext', 'readable writable file');
~~~~~


@param string $filename

@param array|string $options Can be specified as array or string:
 - `type` (string): Verify it is of type: 'file', 'link', 'dir' (default='')
 - `readable` (bool): Verify it is readable? (default=false)
 - `writable` (bool): Also verify the file is writable? (default=false)
 - `writeable` (bool): Alias of writable (default=false)
 - When specified as string, you can use any combination of the words:
   `readable, writable, file, link, dir` (separated by space or comma).

@return bool

@throws WireException if given invalid or unrecognized $options

@since 3.0.180

## size()

Get size of file or directory (in bytes)

@param string $path File or directory path

@param array|bool $options Options array, or boolean true for getString option:
 - `getString` (bool): Get string that summarizes bytes, kB, MB, etc.? (default=false)

@return int|string

@since 3.0.214

## tempDir()

Return a new temporary directory/path ready to use for files

- The temporary directory will be automatically removed at the end of the request.
- Temporary directories are not http accessible.
- If you call this with the same non-empty `$name` argument more than once in the
  same request, the same `WireTempDir` instance will be returned.


~~~~~
$tempDir = $files->tempDir();
$path = $tempDir->get();
file_put_contents($path . 'some-file.txt', 'Hello world');
~~~~~

@param Object|string $name Any one of the following: (default='')
 - Omit this argument for auto-generated name, 3.0.178+
 - Name/word that you specify using fieldName format, i.e. [_a-zA-Z0-9].
 - Object instance that needs the temp dir.

@param array|int $options Deprecated argument. Call `WireTempDir` methods if you need more options.

@return WireTempDir Returns a WireTempDir instance. If you typecast return value to a string,
   it is the temp dir path (with trailing slash).

@see WireTempDir

## find()

Find all files in the given $path recursively, and return a flat array of all found filenames


@param string $path Path to start from (required).

@param array $options Options to affect what is returned (optional):
 - `recursive` (int|bool): How many levels of subdirectories this method should descend into beyond the 1 given.
    Specify 1 to remain at the one directory level given, or 2+ to descend into subdirectories. (default=10)
    In 3.0.180+ you may also specify true for no limit, or false to disable descending into any subdirectories.
 - `extensions` (array|string): Only include files having these extensions, or omit to include all (default=[]).
    In 3.0.180+ the extensions argument may also be a string (space or comma separated).
 - `excludeDirNames` (array): Do not descend into directories having these names (default=[]).
 - `excludeHidden` (bool): Exclude hidden files? (default=false).
 - `allowDirs` (bool): Allow directories in returned files (except for '.' and '..')? Note that returned
    directories have a trailing slash. (default=false) 3.0.180+
 - `returnRelative` (bool): Make returned array have filenames relative to given start $path? (default=false)

@return array Flat array of filenames

@since 3.0.96

## unzip()

Unzips the given ZIP file to the destination directory

~~~~~
// Unzip a file
$zip = $config->paths->cache . "my-file.zip";
$dst = $config->paths->cache . "my-files/";
$items = $files->unzip($zip, $dst);
if(count($items)) {
  // $items is an array of filenames that were unzipped into $dst
}
~~~~~


@param string $zipFile ZIP file to extract

@param string $destinationPath Directory where files should be unzipped into. Directory is created if it doesn't exist.

@param array $options Options to modify default behavior (3.0.254+):
 - `extractFiles` (array): Filenames or regex patterns for files to extract, ignoring all others. (default=[])
 - `extractExtensions` (array): Only extract these file extensions, ignoring all others. (default=[])
 - `ignoreFiles` (array): Basenames or regex patterns matching basenames to skip/ignore (default=[ '.DS_Store', '__MACOSX' ])
 - `ignoreExtensions` (array): Extensions to skip/ignore for files in the ZIP (default=[ 'zip' ])
 - `minFiles` (int): Minimum number files that must be present inside the ZIP for it to be valid. (default=1)
 - `maxFiles` (int): Maximum number of files allowed in ZIP (default=1000)
 - `maxDepth` (int): $maxDepth Maximum allowed folder/directory depth in ZIP (default=8)
 - `maxFileMegabytes` (int): Maximum allowed uncompressed size of any individual file in ZIP, in MB. (default=20)
 - `maxTotalMegabytes` (int): Maximum allowed total uncompressed size of all files in ZIP, in MB. (default=100)
 - `maxErrors` (int): Maximum number of errors to report (default=10)
 - `requireFiles` (array): File names or regex patterns that must be present in at least one file for ZIP to be valid.
    For example `!\.json$!` would require that a `.json` file is present in the ZIP. default=[]
 - `fatalFiles` (array): Strings or regex patterns that when matched, cause entire ZIP to fail validation.
    If not given a regex, it matches any part of the filename. (default=[])
 - `maxCompRatio` (int): Max allowed compression ratio or 0 to ignore (default=0)
 - `test` (bool|string): Do not actually unzip but return the filenames that would be unzipped.
    Specify 'verbose' rather than true to return verbose array of info instead of filenames. (default=false)
 - For the `extractFiles`, `ignoreFiles`, `requireFiles` and `fatalFiles` options, You can optionally specify
   a regex pattern by using a `!` as your regex starting and ending delimiter.

@return array Returns an array of filenames (excluding $dst) that were unzipped.

@throws WireException All error conditions result in WireException being thrown.

@see WireFileTools::zip()

## zip()

Creates a ZIP file

~~~~~
// Create zip of all files in directory $dir to file $zip
$dir = $config->paths->cache . "my-files/";
$zip = $config->paths->cache . "my-file.zip";
$result = $files->zip($zip, $dir);

echo "<h3>These files were added to the ZIP:</h3>";
foreach($result['files'] as $file) {
  echo "<li>" $sanitizer->entities($file) . "</li>";
}

if(count($result['errors'])) {
  echo "<h3>There were errors:</h3>";
  foreach($result['errors'] as $error) {
    echo "<li>" . $sanitizer->entities($error) . "</li>";
  }
}
~~~~~


@param string $zipfile Full path and filename to create or update (i.e. /path/to/myfile.zip)

@param array|string $files Array of files to add (full path and filename), or directory (string) to add.
  If given a directory, it will recursively add everything in that directory.

@param array $options Associative array of options to modify default behavior:
 - `allowHidden` (boolean or array): allow hidden files? May be boolean, or array of hidden files (basenames) you allow. (default=false)
   Note that if you actually specify a hidden file in your $files argument, then that overrides this.
 - `allowEmptyDirs` (boolean): allow empty directories in the ZIP file? (default=true)
 - `overwrite` (boolean): Replaces ZIP file if already present (rather than adding to it) (default=false)
 - `maxDepth` (int): Max dir depth 0 for no limit (default=0). Specify 1 to stay only in dirs listed in $files.
 - `exclude` (array): Files or directories to exclude
 - `dir` (string): Directory name to prepend to added files in the ZIP

@return array Returns associative array of:
 - `files` (array): all files that were added
 - `errors` (array): files that failed to add, if any

@throws WireException Original ZIP file creation error conditions result in WireException being thrown.

@see WireFileTools::unzip()

## send()

Send the contents of the given filename to the current http connection

This function utilizes the `$config->fileContentTypes` to match file extension to content type headers
and force-download state.

This function throws a `WireException` if the file can’t be sent for some reason. Set the `throw` option to
false if you want it to instead return integer 0 when errors occur.


@param string|bool $filename Full path and filename to send or boolean false if provided in `$options[data]`.

@param array $options Optional options to modify default behavior:
  - `exit` (bool): Halt program execution after file send (default=true).
  - `partial` (bool): Allow use of partial downloads via HTTP_RANGE requests? Since 3.0.131 (default=true)
  - `forceDownload` (bool|null): Whether file should force download, or null to let content-type header decide (default=null).
  - `downloadFilename` (string): Filename you want the download to show on user’s computer, or omit to use existing (default='').
  - `headers` (array): The $headers argument to this method can also be provided as an option right here (default=[]). Since 3.0.131.
  - `data` (string): String of data to send rather than file, $filename argument must be false (default=''). Since 3.0.132.
  - `limitPath` (string|bool): Prefix disk path $filename must be within, false to disable, true for site/assets (default=false). Since 3.0.169.
  - `throw` (bool): Throw exceptions on error? When false, it will instead return integer 0 on errors (default=true). Since 3.0.169.

@param array $headers Optional headers that are sent, below are the defaults:
  - `pragma`: public
  - `expires`: 0
  - `cache-control`: must-revalidate, post-check=0, pre-check=0
  - `content-type`: {content-type} (replaced with actual content type)
  - `content-transfer-encoding`: binary
  - `content-length`: {filesize} (replaced with actual filesize)
  - To remove a header completely, make its value NULL.
  - If preferred, the above headers can be specified in `$options[headers]` instead.

@return int Returns bytes sent, only if `exit` option is false (since 3.0.169)

@throws WireException

@see WireHttp::sendFile()

## filePutContents()

Create (overwrite or append) a file, put the $contents in it, and adjust permissions

This is the same as PHP’s `file_put_contents()` except that it’s preferable to use this in
ProcessWire because it adjusts the file permissions configured with `$config->chmodFile`.


@param string $filename Filename to write to

@param string|mixed $contents Contents to write to file

@param int $flags Flags to modify behavior:
 - `FILE_APPEND` (constant): Append to file if it already exists.
 - `LOCK_EX` (constant): Acquire exclusive lock to file while writing.

@return int|bool Number of bytes written or boolean false on fail

@throws WireException if given invalid $filename (since 3.0.118)

@see WireFileTools::fileGetContents()

## fileGetContents()

Get contents of file

This is the same as PHP’s `file_get_contents()` except that the arguments are simpler and
it may be preferable to use this in ProcessWire for future cases where the file system may be
abstracted from the installation.


@param string $filename Full path and filename to read

@param int $offset The offset where the reading starts on the original stream. Negative offsets count from the end of the stream.

@param int $maxlen Maximum length of data read. The default is to read until end of file is reached.

@return bool|string Returns the read data (string) or boolean false on failure.

@since 3.0.167

@see WireFileTools::filePutContents()

## getCSV()

Get next row from a CSV file

This simplifies the reading of a CSV file by abstracting file-open, get-header, get-rows and file-close
operations into a single method call, where all those operations are handled internally. All you have to
do is keep calling the `$files->getCSV($filename)` method until it returns false. This method will also
skip over blank rows by default, unlike PHP’s fgetcsv() which will return a 1-column row with null value.

This method should always be used in a loop, meaning you must keep calling it until it returns false.
Otherwise a CSV file may be unintentionally left open. If you can't do that then use getAllCSV() instead.

For the method `$options` argument note that the `length`, `separator`, `enclosure` and `escape` options
all correspond to the identically named PHP [fgetcsv](https://www.php.net/manual/en/function.fgetcsv.php)
arguments.

Example foods.csv file (first row is header):
~~~~~
Food,Type,Color
Apple,Fruit,Red
Banana,Fruit,Yellow
Spinach,Vegetable,Green
~~~~~
Example of reading the foods.csv file above:
~~~~~
while($row = $files->getCSV('/path/to/foods.csv')) {
  echo "Food: $row[Food] ";
  echo "Type: $row[Type] ";
  echo "Color: $row[Color] ";
}
~~~~~


@param string $filename CSV filename to read from

@param array $options
 - `header` (bool|array): Indicate whether CSV has header and how it should be used (default=true):
    True to treat first line as header and return rows as associative arrays indexed by the header values.
    False to indicate there is no header and/or to indicate it should return regular non-associative PHP arrays for rows.
    Array to use it as the header and return rows as associative arrays indexed by your values.
 - `length` (int): Optional. When specified, must be greater than the longest line (in characters) to be found in the CSV file
    (allowing for trailing line-end characters). Otherwise the line is split in chunks of length characters, unless the split
    would occur inside an enclosure. Omitting this parameter (or setting it to 0, or null in PHP 8.0.0 or later) the maximum
    line length is not limited, which is slightly slower. (default=0)
 - `separator` (string): The field separator/delimiter, one single-byte character only. (default=',')
 - `enclosure` (string): The field enclosure character, one single-byte character only. (default='"')
 - `escape` (string): The escape character, at most one single-byte character. An empty string ("") disables the proprietary
    escape mechanism. (default="\\")
 - `blanks` (bool): Allow blank rows? (default=false)
 - `convert` (bool): Convert digit-only strings to integers? (default=false)

@return array|false Returns array for next row or boolean false when there are no more rows.

@see https://www.php.net/manual/en/function.fgetcsv.php

@see getAllCSV()

@since 3.0.197

## getAllCSV()

Get all rows from a CSV file

This simplifies the reading of a CSV file by abstracting file-open, get-header, get-rows and file-close
operations into a single method call, where all those operations are handled internally. All you have to
do is call the `$files->getAllCSV($filename)` method once and it will return an array of arrays (one per row).
This method will also skip over blank rows by default, unlike PHP’s fgetcsv() which will return a 1-column row
with null value.

This method is limited by available memory, so when working with potentially large files, you should use the
`$files->getCSV()` method instead, which reads the CSV file row-by-row rather than all at once.

Note for the method `$options` argument that the `length`, `separator`, `enclosure` and `escape` options
all correspond to the identically named PHP [fgetcsv](https://www.php.net/manual/en/function.fgetcsv.php)
arguments.

Example foods.csv file (first row is header):
~~~~~
Food,Type,Color
Apple,Fruit,Red
Banana,Fruit,Yellow
Spinach,Vegetable,Green
~~~~~
Example of reading the foods.csv file above:
~~~~~
$rows = $files->getAllCSV('/path/to/foods.csv');
foreach($rows as $row) {
  echo "Food: $row[Food] ";
  echo "Type: $row[Type] ";
  echo "Color: $row[Color] ";
}
~~~~~


@param string $filename CSV filename to read from

@param array $options
 - `header` (bool|array): Indicate whether CSV has header and how it should be used (default=true):
    True to treat first line as header and return rows as associative arrays indexed by the header values.
    False to indicate there is no header and/or to indicate it should return regular non-associative PHP arrays for rows.
    Array to use it as the header and return rows as associative arrays indexed by your values.
 - `length` (int): Optional. When specified, must be greater than the longest line (in characters) to be found in the CSV file
    (allowing for trailing line-end characters). Otherwise the line is split in chunks of length characters, unless the split
    would occur inside an enclosure. Omitting this parameter (or setting it to 0, or null in PHP 8.0.0 or later) the maximum
    line length is not limited, which is slightly slower. (default=0)
 - `separator` (string): The field separator/delimiter, one single-byte character only. (default=',')
 - `enclosure` (string): The field enclosure character, one single-byte character only. (default='"')
 - `escape` (string): The escape character, at most one single-byte character. An empty string ("") disables the proprietary
    escape mechanism. (default="\\")
 - `convert` (bool): Convert digit-only strings to integers? (default=false)
 - `blanks` (bool): Allow blank rows? (default=false)

@return array

@see https://www.php.net/manual/en/function.fgetcsv.php

@see getCSV()

@since 3.0.197

## render()

Given a filename, render it as a ProcessWire template file

This is a shortcut to using the TemplateFile class.

File is assumed relative to `/site/templates/` (or a directory within there) unless you specify a full path.
If you specify a full path, it will accept files in or below any of the following:

- /site/templates/
- /site/modules/
- /wire/modules/

Note this function returns the output to you, so that you can send the output wherever you want (delayed output).
For direct output, use the `$files->include()` function instead.


@param string $filename Assumed relative to /site/templates/ unless you provide a full path name with the filename.
 If you provide a path, it must resolve somewhere in site/templates/, site/modules/ or wire/modules/.

@param array $vars Optional associative array of variables to send to template file.
 Please note that all template files automatically receive all API variables already (you don't have to provide them).

@param array $options Associative array of options to modify behavior:
 - `defaultPath` (string): Path where files are assumed to be when only filename or relative filename is specified (default=/site/templates/)
 - `autoExtension` (string): Extension to assume when no ext in filename, make blank for no auto assumption (default=php)
 - `allowedPaths` (array): Array of paths that are allowed (default is templates, core modules and site modules)
 - `allowDotDot` (bool): Allow use of ".." in paths? (default=false)
 - `throwExceptions` (bool): Throw exceptions when fatal error occurs? (default=true)
 - `cache` (int|string|Page): Specify non-zero value to cache rendered result for this many seconds, or see the `WireCache::renderFile()`
    method `$expire` argument for more options you can specify here. (default=0, no cache) *Note: this option added in 3.0.130*

@return string|bool Rendered template file or boolean false on fatal error (and throwExceptions disabled)

@throws WireException if template file doesn't exist

@see WireFileTools::include()

## ___include()

Include a PHP file passing it all API variables and optionally your own specified variables

This is the same as PHP’s `include()` function except for the following:

- It receives all API variables and optionally your custom variables
- If your filename is not absolute, it doesn’t look in PHP’s include path, only in the current dir.
- It only allows including files that are part of the PW installation: templates, core modules or site modules
- It will assume a “.php” extension if filename has no extension.

Note this function produces direct output. To retrieve output as a return value, use the
`$files->render()` function instead.


@param string $filename Filename to include

@param array $vars Optional variables you want to hand to the include (associative array)

@param array $options Array of options to modify behavior:
 - `func` (string): Function to use: include, include_once, require or require_once (default=include)
 - `autoExtension` (string): Extension to assume when no ext in filename, make blank for no auto assumption (default=php)
 - `allowedPaths` (array): Array of start paths include files are allowed from. Note current dir is always allowed.

@return bool Always returns true

@throws WireException if file doesn’t exist or is not allowed

## includeOnce()

Same as include() method except that file will not be executed if it as previously been included

See the `WireFileTools::include()` method for details, arguments and options.


@param string $filename

@param array $vars

@param array $options

@return bool

@see WireFileTools::include()

@since 3.0.96

## getNamespace()

Get the namespace used in the given .php or .module file


@param string $file File name or file data (if file data, specify true for 2nd argument)

@param bool $fileIsContents Specify true if the given $file is actually the contents of the file, rather than file name.

@return string Actual found namespace or "\" (root namespace) if none found

## unixDirName()

Convert given directory name to use unix slashes and enforce trailing or no-trailing slash


@param string $dir Directory name to adust (if it needs it)

@param bool $trailingSlash True to force trailing slash, false to force no trailing slash (default=true)

@return string Adjusted directory name

## unixFileName()

Convert given file name to use unix slashes (if it isn’t already)


@param string $file File name to adjust (if it needs it)

@return string Adjusted file name

## fileInPath()

Is given $file name in given $path name? (aka: is $file a subdirectory somewhere within $path)

This is purely for string comparison purposes, it does not check if file/path actually exists.
Note that if $file and $path are identical, this method returns false.


@param string $file May be a file or a directory

@param string $path

@return bool

## currentPath()

Get the current path / work directory

This is like PHP’s getcwd() function except that is in ProcessWire format as unix path with trailing slash.


@return string

@since 3.0.130
