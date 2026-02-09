# PagefilesManager

Source: `wire/core/PagefilesManager.php`

Inherits: `Wire`

## Summary

ProcessWire PagefilesManager

Common methods:
- [`init()`](method-init.md)
- [`setPage()`](method-setpage.md)
- [`getFiles()`](method-getfiles.md)
- [`getFile()`](method-getfile.md)
- [`_copyFiles()`](method-_copyfiles.md)

Groups:
Group: [other](group-other.md)

Manages files and file directories for a page independent of a particular field.
Files in ProcessWire are always connected with a particular `Field` on a `Page`. This is typically
a `FieldtypeFile` field or a `FieldtypeImage` field, which exist as `Pagefiles` or `Pageimages`
values on the Page. Sometimes it is necessary to manage all files connected with a page as a
group, and this files manager class provides that. Likewise, something needs to manage the paths
and URLs where these files live, and that is where this files manager comes into play as well.

**Summary of what PagefilesManager does**

- Provides methods for movement of all files connected with a page as a group.
- Ensures that file directories for a page are created (and removed) when applicable.
- Manages secured vs. normal page file paths (see `$config->pagefileSecure`).
- Manages extended vs. normal page file paths (see `$config->pagefileExtendedPaths`).

**How to access the Page files manager**

The Page files manager can be accessed from any page’s `Page::filesManager()` method or property.

~~~~~
// Example of getting a Page’s dedicated file path and URL
$filesPath = $page->filesManager->path();
$filesURL = $page->filesManager->url();
~~~~~

## Methods
- [`__construct(Page $page)`](method-__construct.md) Construct the PagefilesManager and ensure all needed paths are created
- [`getFiles(): array`](method-getfiles.md) Get an array of all published filenames on the current Page.
- [`getFile(string $name): Pagefile|Pageimage|null`](method-getfile.md) Get the Pagefile object containing the given filename.
- [`_copyFiles(string $fromPath, string $toPath, bool $rename = false): int`](method-_copyfiles.md) Recursively copy all files in $fromPath to $toPath, for internal use
- [`copyFiles($toPath): int`](method-copyfiles.md) Recursively copy all files managed by this PagefilesManager into a new path.
- [`importFiles(string $fromPath, bool $move = false): int`](method-importfiles.md) Copy/import files from given path into the page’s files directory
- [`replaceFiles(string $fromPath, bool $move = false): int`](method-replacefiles.md) Replace all page’s files with those from given path
- [`moveFiles($toPath): int`](method-movefiles.md) Recursively move all files managed by this PagefilesManager into a new path.
- [`_createPath(string $path): bool`](method-_createpath.md) Create a directory with proper permissions, for internal use.
- [`emptyPath(bool $rmdir = false, bool $recursive = true): bool`](method-emptypath.md) Empty out the published files (delete all of them)
- [`emptyAllPaths(): bool`](method-emptyallpaths.md) Empties all file paths related to the Page, and removes the directories
- [`path(): string`](method-path.md) Get the published path for files
- [`url(): string`](method-url.md) Get the published URL for files
- [`save()`](method-___save.md) (hookable) For hooks to listen to on page save action, for file-specific operations
- [`__get(string $name): mixed`](method-__get.md) Handle non-function versions of some properties
- [`getTempPath(): string`](method-gettemppath.md) Return a path where temporary files can be stored unique to this ProcessWire instance

## Constants
- [`defaultSecurePathPrefix = '.'`](const-defaultsecurepathprefix.md)
- [`extendedDirName = '0/'`](const-extendeddirname.md)
