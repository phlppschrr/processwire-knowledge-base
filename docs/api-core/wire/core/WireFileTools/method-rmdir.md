# $wireFileTools->rmdir($path, $recursive = false, $options = array()): bool

Source: `wire/core/WireFileTools.php`

Remove a directory and optionally everything within it (recursively)

Unlike PHP's `rmdir()` function, this method provides a recursive option, which can be enabled by specifying true
for the `$recursive` argument. You should be careful with this option, as it can easily wipe out an entire
directory tree in a flash.

Note that the $options argument was added in 3.0.118.

## Example

~~~~~
// Remove directory /site/assets/cache/foo-bar/ and everything in it
$files->rmdir($config->paths->cache . 'foo-bar/', true);

// Remove directory after ensuring $pathname is somewhere within /site/assets/
$files->rmdir($pathname, true, [ 'limitPath' => $config->paths->assets ]);
~~~~~

## Usage

~~~~~
// basic usage
$bool = $wireFileTools->rmdir($path);

// usage with all arguments
$bool = $wireFileTools->rmdir($path, $recursive = false, $options = array());
~~~~~

## Arguments

- `$path` `string` Path/directory you want to remove
- `$recursive` (optional) `bool` If set to true, all files and directories in $path will be recursively removed as well (default=false).
- `$options` (optional) `array|bool|string` Optional settings to adjust behavior or (bool|string) for limitPath option: - `limitPath` (string|bool|array): Must be somewhere within given path, boolean true for site assets, or false to disable (default=false). - `throw` (bool): Throw verbose WireException (rather than return false) when potentially consequential fail (default=false).

## Return value

- `bool` True on success, false on failure
