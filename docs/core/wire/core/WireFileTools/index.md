# WireFileTools

Source: `wire/core/WireFileTools.php`

Inherits: `Wire`


Groups:
Group: [other](group-other.md)

ProcessWire File Tools ($files API variable)

Helpers for working with files and directories.

Methods:
- [`__destruct()`](method-__destruct.md)
- [`mkdir(string $path, bool|string $recursive = false, string|null|bool $chmod = null): bool`](method-mkdir.md)
- [`rmdir(string $path, bool $recursive = false, array|bool|string $options = array()): bool`](method-rmdir.md)
- [`chmod(string $path, bool|string $recursive = false, string|null|bool $chmod = null): bool`](method-chmod.md)
- [`copy(string $src, string $dst, bool|array $options = array()): bool`](method-copy.md)
- [`unlink(string $filename, string|bool $limitPath = false, bool $throw = false): bool`](method-unlink.md)
- [`rename(string $oldName, string $newName, array|bool|string $options = array()): bool`](method-rename.md)
- [`renameCopy(string $oldName, string $newName, array $options = array()): bool`](method-renamecopy.md)
- [`exists(string $filename, array|string $options = ''): bool`](method-exists.md)
- [`size(string $path, array|bool $options = array()): int|string`](method-size.md)
- [`tempDir(Object|string $name = '', array|int $options = array()): WireTempDir`](method-tempdir.md)
- [`find(string $path, array $options = array()): array`](method-find.md)
- [`unzip(string $zipFile, string $destinationPath, array $options = []): array`](method-unzip.md)
- [`zip(string $zipfile, array|string $files, array $options = array()): array`](method-zip.md)
- [`send(string|bool $filename, array $options = array(), array $headers = array()): int`](method-send.md)
- [`filePutContents(string $filename, string|mixed $contents, int $flags = 0): int|bool`](method-fileputcontents.md)
- [`fileGetContents(string $filename, int $offset = 0, int $maxlen = 0): bool|string`](method-filegetcontents.md)
- [`getCSV(string $filename, array $options = array()): array|false`](method-getcsv.md)
- [`getAllCSV(string $filename, array $options = array()): array`](method-getallcsv.md)
- [`render(string $filename, array $vars = array(), array $options = array()): string|bool`](method-render.md)
- [`include(string $filename, array $vars = array(), array $options = array()): bool`](method-___include.md) (hookable)
- [`includeOnce(string $filename, array $vars = array(), array $options = array()): bool`](method-includeonce.md)
- [`getNamespace(string $file, bool $fileIsContents = false): string`](method-getnamespace.md)
- [`unixDirName(string $dir, bool $trailingSlash = true): string`](method-unixdirname.md)
- [`unixFileName(string $file): string`](method-unixfilename.md)
- [`fileInPath(string $file, string $path): bool`](method-fileinpath.md)
- [`currentPath(): string`](method-currentpath.md)
