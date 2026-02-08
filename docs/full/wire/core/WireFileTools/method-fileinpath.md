# $wireFileTools->fileInPath($file, $path): bool

Source: `wire/core/WireFileTools.php`

Is given $file name in given $path name? (aka: is $file a subdirectory somewhere within $path)

This is purely for string comparison purposes, it does not check if file/path actually exists.
Note that if $file and $path are identical, this method returns false.

## Arguments

- string $file May be a file or a directory
- string $path

## Return value

bool
