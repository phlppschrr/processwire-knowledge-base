# PagesTrash

Source: `wire/core/PagesTrash.php`

ProcessWire Pages Trash

Pages Trash
$pages->trasher
Implements page trash/restore/empty methods for the $pages API variable.

ProcessWire 3.x, Copyright 2024 by Ryan Cramer
https://processwire.com

## __construct()

Construct

@param Pages $pages

## trash()

Move a page to the trash

If you have already set the parent to somewhere in the trash, then this method won't attempt to set it again.


@param Page $page

@param bool $save Set to false if you will perform the save() call, as is the case when called from the Pages::save() method.

@return bool

@throws WireException

## restore()

Restore a page from the trash back to a non-trash state

Note that this method assumes already have set a new parent, but have not yet saved.
If you do not set a new parent, then it will restore to the original parent, when possible.


@param Page $page

@param bool $save Set to false if you only want to prep the page for restore (i.e. being saved elsewhere)

@return bool

## getRestoreInfo()

Get info needed to restore a Page that is in the trash

Returns array with the following info:
 - `restorable` (bool): Is the page restorable to a previous known/existing parent?
 - `notes` (array): Any additional notes to explain restore info (like reason why not restorable, or why name changed, etc.)
 - `parent` (Page|NullPage): Parent page that it should restore to
 - `parent_id` (int): ID of parent page that it should restore to
 - `sort` (int): Sort order that should be restored to page
 - `name` (string): Name that should be restored to page’s “name” property.
 - `namePrevious` (string): Previous name, if we had to modify the original name to make it restorable.
 - `name{id}` (string): Name that should be restored  to language where {id} is language ID (if appliable).


@param Page $page Page to restore

@param bool $populateToPage Populate this information to given page? (default=false)

@return array

## parseTrashPageName()

Parse a trashed page name into an array of its components


@param string $name

@return array|bool Returns array of info if name is a trash/restore name, or boolean false if not

## emptyTrash()

Delete all pages in the trash

Populates error notices when there are errors deleting specific pages.


@param array $options
 - `chunkSize` (int): Pages will be deleted in chunks of this many pages per chunk (default=100).
 - `chunkTimeLimit` (int): Maximum seconds allowed to process deletion of each chunk (default=600).
 - `chunkLimit' (int): Maximum chunks to process in an emptyTrash() call (default=1000);
 - `pageLimit` (int): Maximum pages to delete per emptyTrash() call (default=0, no limit).
 - `timeLimit` (int): Maximum time (in seconds) to allow for trash empty (default=3600).
 - `pass2` (bool): Perform a secondary pass using alternate method as a backup? (default=true)
    Note: pass2 is always disabled when a pageLimit is in use or timeLimit has been exceeded.
 - `verbose` (bool): Return verbose array of information about the trash empty process? For debug/dev purposes (default=false)

@return int|array Returns integer (default) or array in verbose mode.
 - By default, returns total number of pages deleted from trash. This number is negative or 0 if not
   all pages could be deleted and error notices may be present.
 - Returns associative array with verbose information if verbose option is chosen.

## emptyTrashPass2()

Secondary pass for trash deletion

This works by finding the children of the trash page and performing a recursive delete on them.

@param array $options Options passed to emptyTrash() method

@param array $result Verbose array, modified directly

@return int

## getTrashTotal()

Get total number of pages in trash


@return int

## getTrashPage()

Return the root parent trash page


@return Page

@throws WireException if trash page cannot be located (highly unlikely)
