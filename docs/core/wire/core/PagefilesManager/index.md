# PagefilesManager

Source: `wire/core/PagefilesManager.php`

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


ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com

Groups:
Group: [other](group-other.md)

Methods:
Method: [__construct()](method-__construct.md)
Method: [getFiles()](method-getfiles.md)
Method: [getFile()](method-getfile.md)
Method: [_copyFiles()](method-_copyfiles.md)
Method: [copyFiles()](method-copyfiles.md)
Method: [importFiles()](method-importfiles.md)
Method: [replaceFiles()](method-replacefiles.md)
Method: [moveFiles()](method-movefiles.md)
Method: [_createPath()](method-_createpath.md)
Method: [emptyPath()](method-emptypath.md)
Method: [emptyAllPaths()](method-emptyallpaths.md)
Method: [path()](method-path.md)
Method: [url()](method-url.md)
Method: [save()](method-___save.md) (hookable)
Method: [__get()](method-__get.md)
Method: [getTempPath()](method-gettemppath.md)

Constants:
Const: [defaultSecurePathPrefix](const-defaultsecurepathprefix.md)
Const: [extendedDirName](const-extendeddirname.md)
