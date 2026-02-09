# $wireFileTools->copy($src, $dst, $options = array()): bool

Source: `wire/core/WireFileTools.php`

Copy all files recursively from one directory ($src) to another directory ($dst)

Unlike PHP's `copy()` function, this method performs a recursive copy by default,
ensuring that all files and directories in the source ($src) directory are duplicated
in the destination ($dst) directory.

This method can also be used to copy single files. If a file is specified for $src, and
only a path is specified for $dst, then the original filename will be retained in $dst.

## Example

~~~~~
// Copy everything from /site/assets/cache/foo/ to /site/assets/cache/bar/
$copyFrom = $config->paths->cache . "foo/";
$copyTo = $config->paths->cache . "bar/";
$files->copy($copyFrom, $copyTo);
~~~~~

## Usage

~~~~~
// basic usage
$bool = $wireFileTools->copy($src, $dst);

// usage with all arguments
$bool = $wireFileTools->copy($src, $dst, $options = array());
~~~~~

## Arguments

- `$src` `string` Path to copy files from, or filename to copy.
- `$dst` `string` Path (or filename) to copy file(s) to. Directory is created if it doesn't already exist.
- `$options` (optional) `bool|array` Array of options: - `recursive` (bool): Whether to copy directories within recursively. (default=true) - `allowEmptyDirs` (boolean): Copy directories even if they are empty? (default=true) - `limitPath` (bool|string|array): Limit copy to within path given here, or true for site assets path. The limitPath option requires core 3.0.118+. (default=false). - `hidden` (bool): Also copy hidden files/directories within given $src directory? (applies only if $src is dir) The hidden option requires core 3.0.180+. (default=true) - If a boolean is specified for $options, it is assumed to be the `recursive` option.

## Return value

- `bool` True on success, false on failure.

## Exceptions

- `WireException` if `limitPath` option is used and either $src or $dst is not allowed
