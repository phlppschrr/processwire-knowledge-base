# PagefilesManager

Source: `wire/core/PagefilesManager.php`

ProcessWire PagefilesManager

Manages files and file directories for a page independent of a particular field.
These methods are not connected with a particular instance and may only be called statically.
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

## other

@method save()

@property string $path

@property string $url

@property Page $page Page that this files manager is for.

## defaultSecurePathPrefix

Default prefix for secure paths when not defined by config.php

## extendedDirName

Prefix to all extended path directories

## __construct()

Construct the PagefilesManager and ensure all needed paths are created

@param Page $page

## getFiles()

Get an array of all published filenames on the current Page.

@return array Array of file basenames

## getFile()

Get the Pagefile object containing the given filename.

@param string $name Name of file to get:
  - If given a URL or path, this will traverse to other pages.
  - If given a basename, it will stay with current page.

@return Pagefile|Pageimage|null Returns Pagefile or Pageimage object if found, or null if not.

## _copyFiles()

Recursively copy all files in $fromPath to $toPath, for internal use

@param string $fromPath Path to copy from

@param string $toPath Path to copy to

@param bool $rename Rename files rather than copy? (makes this perform like a move rather than copy)

@return int Number of files copied

## copyFiles()

Recursively copy all files managed by this PagefilesManager into a new path.


@param $toPath string Path to copy files into.

@return int Number of files/directories copied.

## importFiles()

Copy/import files from given path into the page’s files directory


@param string $fromPath Path to copy/import files from.

@param bool $move Move files into directory rather than copy?

@return int Number of files/directories copied.

@since 3.0.114

## replaceFiles()

Replace all page’s files with those from given path


@param string $fromPath

@param bool $move Move files to destination rather than copy? (default=false)

@return int Number of files/directories copied.

@throws WireException if given a path that does not exist.

@since 3.0.114

## moveFiles()

Recursively move all files managed by this PagefilesManager into a new path.


@param $toPath string Path to move files into.

@return int Number of files/directories moved.

## _createPath()

Create a directory with proper permissions, for internal use.

@param string $path Path to create

@return bool True on success, false if not

## emptyPath()

Empty out the published files (delete all of them)


@param bool $rmdir Remove the directory too? (default=false)

@param bool $recursive Recursively do the same for subdirectories? (default=true)

@return bool True on success, false on error (since 3.0.17, previous versions had no return value).

## emptyAllPaths()

Empties all file paths related to the Page, and removes the directories

This is the same as calling the `PagefilesManager:emptyPath()` method with the
`$rmdir` and `$recursive` options as both true.


@return bool True on success, false on error (since 3.0.17, previous versions had no return value).

## path()

Get the published path for files


@return string

@throws WireException if attempting to access this on a Page that doesn't yet exist in the database

## url()

Get the published URL for files


@return string

@throws WireException if attempting to access this on a Page that doesn't yet exist in the database

## ___save()

For hooks to listen to on page save action, for file-specific operations

Executed before a page draft/published assets are moved around, when changes to files may be best to execute.

There are no arguments or return values here.
Hooks may retrieve the Page object being saved from `$event->object->page`.

## __get()

Handle non-function versions of some properties

@param string $name

@return mixed

## getTempPath()

Return a path where temporary files can be stored unique to this ProcessWire instance

@return string
