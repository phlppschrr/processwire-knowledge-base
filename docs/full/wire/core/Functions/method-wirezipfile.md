# $functions->wireZipFile($zipfile, $files, array $options = array()): array

Source: `wire/core/Functions.php`

Create a ZIP file from given files

This is procedural version of the `$files->zip()` method. See that method for all options.

## Arguments

- string $zipfile Full path and filename to create or update (i.e. /path/to/myfile.zip)
- array|string $files Array of files to add (full path and filename), or directory (string) to add. If given a directory, it will recursively add everything in that directory.
- array $options Options modify default behavior: - `allowHidden` (bool|array): allow hidden files? May be boolean, or array of hidden files (basenames) you allow. (default=false) Note that if you actually specify a hidden file in your $files argument, then that overrides this. - `allowEmptyDirs` (bool): allow empty directories in the ZIP file? (default=true) - `overwrite` (bool): Replaces ZIP file if already present (rather than adding to it) (default=false) - `exclude` (array): Files or directories to exclude - `dir` (string): Directory name to prepend to added files in the ZIP

## Return value

array Returns associative array of: - `files` (array): all files that were added - `errors` (array): files that failed to add, if any

## Throws

- WireException Original ZIP file creation error conditions result in WireException being thrown.

## See also

- [WireFileTools::zip()](../WireFileTools/method-zip.md)
