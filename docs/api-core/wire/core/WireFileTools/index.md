# WireFileTools

Source: `wire/core/WireFileTools.php`

Inherits: `Wire`

## Summary

ProcessWire File Tools (`$files` API variable)

Common methods:
- [`mkdir()`](method-mkdir.md)
- [`rmdir()`](method-rmdir.md)
- [`chmod()`](method-chmod.md)
- [`copy()`](method-copy.md)
- [`unlink()`](method-unlink.md)

Groups:
Group: [other](group-other.md)

Helpers for working with files and directories.

## Methods
- [`__destruct()`](method-__destruct.md) Destruct
- [`mkdir(string $path, bool|string $recursive = false, string|null|bool $chmod = null): bool`](method-mkdir.md) Create a directory that is writable to ProcessWire and uses the defined $config chmod settings
- [`rmdir(string $path, bool $recursive = false, array|bool|string $options = array()): bool`](method-rmdir.md) Remove a directory and optionally everything within it (recursively)
- [`chmod(string $path, bool|string $recursive = false, string|null|bool $chmod = null): bool`](method-chmod.md) Change the read/write mode of a file or directory, consistent with ProcessWire's configuration settings
- [`copy(string $src, string $dst, bool|array $options = array()): bool`](method-copy.md) Copy all files recursively from one directory ($src) to another directory ($dst)
- [`unlink(string $filename, string|bool $limitPath = false, bool $throw = false): bool`](method-unlink.md) Unlink/delete file with additional protections relative to PHP unlink()
- [`rename(string $oldName, string $newName, array|bool|string $options = array()): bool`](method-rename.md) Rename a file or directory and update permissions
- [`renameCopy(string $oldName, string $newName, array $options = array()): bool`](method-renamecopy.md) Rename by first copying files to destination and then deleting source files
- [`exists(string $filename, array|string $options = ''): bool`](method-exists.md) Does the given file/link/dir exist?
- [`size(string $path, array|bool $options = array()): int|string`](method-size.md) Get size of file or directory (in bytes)
- [`tempDir(Object|string $name = '', array|int $options = array()): WireTempDir`](method-tempdir.md) Return a new temporary directory/path ready to use for files
- [`find(string $path, array $options = array()): array`](method-find.md) Find all files in the given $path recursively, and return a flat array of all found filenames
- [`unzip(string $zipFile, string $destinationPath, array $options = []): array`](method-unzip.md) Unzips the given ZIP file to the destination directory
- [`zip(string $zipfile, array|string $files, array $options = array()): array`](method-zip.md) Creates a ZIP file
- [`send(string|bool $filename, array $options = array(), array $headers = array()): int`](method-send.md) Send the contents of the given filename to the current http connection
- [`filePutContents(string $filename, string|mixed $contents, int $flags = 0): int|bool`](method-fileputcontents.md) Create (overwrite or append) a file, put the $contents in it, and adjust permissions
- [`fileGetContents(string $filename, int $offset = 0, int $maxlen = 0): bool|string`](method-filegetcontents.md) Get contents of file
- [`getCSV(string $filename, array $options = array()): array|false`](method-getcsv.md) Get next row from a CSV file
- [`getAllCSV(string $filename, array $options = array()): array`](method-getallcsv.md) Get all rows from a CSV file
- [`render(string $filename, array $vars = array(), array $options = array()): string|bool`](method-render.md) Given a filename, render it as a ProcessWire template file
- [`include(string $filename, array $vars = array(), array $options = array()): bool`](method-___include.md) (hookable) Include a PHP file passing it all API variables and optionally your own specified variables
- [`includeOnce(string $filename, array $vars = array(), array $options = array()): bool`](method-includeonce.md) Same as include() method except that file will not be executed if it as previously been included
- [`getNamespace(string $file, bool $fileIsContents = false): string`](method-getnamespace.md) Get the namespace used in the given .php or .module file
- [`unixDirName(string $dir, bool $trailingSlash = true): string`](method-unixdirname.md) Convert given directory name to use unix slashes and enforce trailing or no-trailing slash
- [`unixFileName(string $file): string`](method-unixfilename.md) Convert given file name to use unix slashes (if it isn’t already)
- [`fileInPath(string $file, string $path): bool`](method-fileinpath.md) Is given $file name in given $path name? (aka: is $file a subdirectory somewhere within $path)
- [`currentPath(): string`](method-currentpath.md) Get the current path / work directory
