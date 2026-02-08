# PagesVersionsFiles

Source: `wire/modules/Pages/PagesVersions/PagesVersionsFiles.php`

File management for PagesVersions

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## __construct()

Construct

## copyPageVersionFiles()

*****************************************************************************
API SUPPORT METHODS FOR FILES BY ENTIRE DIRECTORY

## copyPageVersionFiles()

Copy files for given $page into version directory

@param Page $page

@param int $version

@return bool|int

## deletePageVersionFiles()

Delete files for given version

@param Page $page

@param int $version

@return bool

## restorePageVersionFiles()

Restore files from version into live $page

@param Page $page

@param int $version

@return int

## copyPageFieldVersionFiles()

*****************************************************************************
API SUPPORT METHODS FOR FILES BY FIELD

## copyPageFieldVersionFiles()

Copy files for given $page and field into version directory

@param Page $page

@param Field $field

@param int $version

@return int

## deletePageFieldVersionFiles()

Delete files for given page and field version

@todo is this method even needed?

@param Page $page

@param Field $field

@param int $version

@return int

## restorePageFieldVersionFiles()

Restore files for given field from version into live $page

@param Page $page

@param Field $field

@param int $version

@return int

## getFileFields()

Get all fields that can support files

@param Page $page

@param array $options
 - `populated` (bool): Only return populated file fields with 1+ files in them? (default=false)
 - `names` (array): Limit check to these field names or omit for all. (default=[])

@return Field[] Returned fields array is indexed by field name

## fieldSupportsFiles()

Does given field support files?

@param Field|string|int $field

@return bool

## useFilesByField()

Copy/restore files individually by field for given page?

- Return true if files should be copied/restored individually by field.
- Returns false if entire page directory should be copied/restored at once.

@param Page $page

@param Field[]|string[] $names Optionally limit check to these fields

@return bool

## pageVersion()

Ensure that given page is given version, and return version page if it isn't already

@param Page $page

@param int $version Page version or 0 to get live page

@return NullPage|Page

## hookPagefilesManagerPath()

*****************************************************************************
HOOKS
