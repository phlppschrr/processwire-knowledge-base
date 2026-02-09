# PagefilesManager

Source: `wire/core/PagefilesManager.php`

Inherits: `Wire`


Groups:
Group: [other](group-other.md)

ProcessWire PagefilesManager

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

Methods:
- [`__construct(Page $page)`](method-__construct.md)
- [`getFiles(): array`](method-getfiles.md)
- [`getFile(string $name): Pagefile|Pageimage|null`](method-getfile.md)
- [`_copyFiles(string $fromPath, string $toPath, bool $rename = false): int`](method-_copyfiles.md)
- [`copyFiles($toPath): int`](method-copyfiles.md)
- [`importFiles(string $fromPath, bool $move = false): int`](method-importfiles.md)
- [`replaceFiles(string $fromPath, bool $move = false): int`](method-replacefiles.md)
- [`moveFiles($toPath): int`](method-movefiles.md)
- [`_createPath(string $path): bool`](method-_createpath.md)
- [`emptyPath(bool $rmdir = false, bool $recursive = true): bool`](method-emptypath.md)
- [`emptyAllPaths(): bool`](method-emptyallpaths.md)
- [`path(): string`](method-path.md)
- [`url(): string`](method-url.md)
- [`save()`](method-___save.md) (hookable)
- [`__get(string $name): mixed`](method-__get.md)
- [`getTempPath(): string`](method-gettemppath.md)

Constants:
- [`defaultSecurePathPrefix`](const-defaultsecurepathprefix.md)
- [`extendedDirName`](const-extendeddirname.md)
