# PagesEditor

Source: `wire/core/PagesEditor.php`

ProcessWire Pages Editor

Pages Editor
$pages->editor
Implements page editing and manipulation methods for the $pages API variable.
Please always use `$pages->method()` rather than `$pages->editor->method()` in cases where there is overlap.

ProcessWire 3.x, Copyright 2025 by Ryan Cramer
https://processwire.com

## __construct()

Construct

@param Pages $pages

## isCloning()

Are we currently in a page clone?


@param bool $getDepth Get depth (int) rather than state (bool)?

@return bool|int

## add()

Add a new page using the given template to the given parent

If no name is specified one will be assigned based on the current timestamp.


@param string|Template $template Template name or Template object

@param string|int|Page $parent Parent path, ID or Page object

@param string $name Optional name or title of page. If none provided, one will be automatically assigned based on microtime stamp.
	If you want to specify a different name and title then specify the $name argument, and $values['title'].

@param array $values Field values to assign to page (optional). If $name is omitted, this may also be 3rd param.

@return Page Returned page has output formatting off.

@throws WireException When some criteria prevents the page from being saved.

## isSaveable()

Is the given page in a state where it can be saved from the API?


@param Page $page

@param string $reason Text containing the reason why it can't be saved (assuming it's not saveable)

@param string|Field $fieldName Optional fieldname to limit check to.

@param array $options Options array given to the original save method (optional)

@return bool True if saveable, False if not

## isMoveable()

Return whether given Page is moveable from $oldParent to $newParent


@param Page $page Page to move

@param Page $oldParent Current/old parent page

@param Page $newParent New requested parent page

@param string $reason Populated with reason why page is not moveable, if return value is false.

@return bool

## isDeleteable()

Is the given page deleteable from the API?

Note: this does not account for user permission checking.
It only checks if the page is in a state to be deleteable via the API.


@param Page $page

@param bool $throw Throw WireException with additional details?

@return bool True if deleteable, False if not

@throws WireException If requested to do so via $throw argument

## setupNew()

Auto-populate some fields for a new page that does not yet exist

Currently it does this:

- Assigns a parent if one is not already assigned.
- Sets up a unique page->name based on the format or title if one isn't provided already.
- Assigns a sort value.
- Populates any default values for fields.


@param Page $page

@throws \Exception|WireException|\PDOException if failure occurs while in DB transaction

## setupPageName()

Auto-assign a page name to gven page

Typically this would be used only if page had no name or if it had a temporary untitled name.

Page will be populated with the name given. This method will not populate names to pages that
already have a name, unless the name is "untitled"


@param Page $page

@param array $options
	- format: Optionally specify the format to use, or leave blank to auto-determine.

@return string If a name was generated it is returned. If no name was generated blank is returned.

## save()

Save a page object and it's fields to database.

If the page is new, it will be inserted. If existing, it will be updated.

This is the same as calling $page->save()

If you want to just save a particular field in a Page, use $page->save($fieldName) instead.


@param Page $page Page to save

@param array $options Optional array with the following optional elements:
	- `uncacheAll` (bool): Whether the memory cache should be cleared (default=true)
	- `resetTrackChanges` (bool): Whether the page's change tracking should be reset (default=true)
	- `quiet` (bool): When true, created/modified time+user will use values from $page rather than current user+time (default=false)
	- `adjustName` (bool): Adjust page name to ensure it is unique within its parent (default=true)
	- `forceID` (integer): Use this ID instead of an auto-assigned on (new page) or current ID (existing page)
	- `ignoreFamily` (bool): Bypass check of allowed family/parent settings when saving (default=false)
 - `noHooks` (bool): Prevent before/after save hooks from being called (default=false)
 - `noFields` (bool): Bypass saving of custom fields (default=false)
 - `caller` (string): Optional name of calling function (i.e. 'pages.trash'), for internal use (default='') 3.0.235+
 - `callback` (string|callable): Hook method name from $pages or callable to trigger after save.
    It receives a single $page argument. For internal use. (default='') 3.0.235+

@return bool True on success, false on failure

@throws WireException

## savePageQuery()

Execute query to save to pages table

triggers hooks: addReady, saveReady, statusChangeReady (when status changed)

@param Page $page

@param array $options

@return bool

@throws WireException|\Exception

## savePageQueryException()

Handle Exception for savePageQuery()

While setupNew() already attempts to uniqify a page name with an incrementing
number, there is a chance that two processes running at once might end up with
the same number, so we account for the possibility here by re-trying queries
that trigger duplicate-entry exceptions.

Example of actual exception text, for reference:
Integrity constraint violation: 1062 Duplicate entry 'background-3552' for key 'name3894_parent_id'

@param Page $page

@param \PDOStatement $query

@param \PDOException|\Exception $exception

@param array $options

@return bool True if it should give $query another shot, false if not

## savePageFinish()

Save individual Page fields and supporting actions

triggers hooks: saved, added, moved, renamed, templateChanged

@param Page $page

@param bool $isNew

@param array $options

@return bool

@throws \Exception|WireException|\PDOException If any field-saving failure occurs while in a DB transaction

## saveField()

TBD Identify if parent changed and call saveParentsTable() where appropriate

@param Page $page Page to save parent(s) for

@param bool $isNew If page is newly created during this save this should be true, otherwise false

protected function savePageParent(Page $page, $isNew) {

if($page->parentPrevious || $page->_forceSaveParents || $isNew) {
$this->pages->parents()->rebuild($page);
}

// saveParentsTable option is always true unless manually disabled from a hook
if($page->parentPrevious && !$isNew && $page->numChildren > 0) {
// existing page was moved and it has children
if($page->parent->numChildren == 1) {
// first child of new parent
$this->pages->parents()->rebuildPage($page->parent);
} else {
$this->pages->parents()->rebuildPage($page);
}

} else if(($page->parentPrevious && $page->parent->numChildren == 1) ||
($isNew && $page->parent->numChildren == 1) ||
($page->_forceSaveParents)) {
// page is moved and is the first child of its new parent
// OR page is NEW and is the first child of its parent
// OR $page->_forceSaveParents is set (debug/debug, can be removed later)
$this->pages->parents()->rebuildPage($page->parent);

} else if($page->parentPrevious && $page->parent->numChildren > 1 && $page->parent->parent_id > 1) {
$this->pages->parents()->rebuildPage($page->parent->parent);
}

if($page->parentPrevious && $page->parentPrevious->numChildren == 0) {
// $page was moved and its previous parent is now left with no children, this ensures the old entries get deleted
$this->pages->parents()->rebuild($page->parentPrevious->id);
}
}

## saveField()

Save just a field from the given page

This is the method used by by the `$page->save($field)` method.

This function is public, but the preferred manner to call it is with `$page->save($field)`


@param Page $page

@param string|Field $field Field object or name (string)

@param array|string $options Specify options:
 - `quiet` (bool): Specify true to bypass updating of modified_users_id and modified time (default=false).
 - `noHooks` (bool): Specify true to bypass calling of before/after save hooks (default=false).

@return bool True on success

@throws WireException

@see Page::save()

## saveFields()

Save multiple named fields from given page

~~~~~
// you can specify field names as array…
$a = $pages->saveFields($page, [ 'title', 'body', 'summary' ]);

// …or a CSV string of field names:
$a = $pages->saveFields($page, 'title, body, summary');

// return value is array of saved field/property names
print_r($a); // outputs: array( 'title', 'body', 'summary' )
~~~~~


@param Page $page Page to save

@param array|string|string[]|Field[] $fields Array of field names to save or CSV/space separated field names to save.
  These should only be Field names and not native page property names.

@param array|string $options Optionally specify one or more of the following to modify default behavior:
 - `quiet` (bool): Specify true to bypass updating of modified user and time (default=false).
 - `noHooks` (bool): Prevent before/after save hooks, please also use `$pages->___saveFields()` for call. (default=false)
 - See $options argument in `Pages::save()` for additional options.

@return array Array of saved field names (may also include property names if they were modified)

@throws WireException

@since 3.0.242

## addStatus()

Silently add status flag to a Page and save

This action does not update the Page modified date.
It updates the status for both the given instantiated Page object and the value in the DB.


@param Page $page

@param int $status Use Page::status* constants

@return bool

@since 3.0.146

@see PagesEditor::setStatus(), PagesEditor::removeStatus()

## removeStatus()

Silently remove status flag from a Page and save

This action does not update the Page modified date.
It updates the status for both the given instantiated Page object and the value in the DB.


@param Page $page

@param int $status Use Page::status* constants

@return bool

@since 3.0.146

@see PagesEditor::setStatus(), PagesEditor::addStatus(), PagesEditor::saveStatus()

## saveStatus()

Silently save whatever the given Page’s status currently is

This action does not update the Page modified date.


@param Page $page

@return bool

@since 3.0.146

## savePageStatus()

Add or remove a Page status and commit to DB, optionally recursive with the children, grandchildren, and so on.

While this can be performed with other methods, this is here just to make it fast for internal/non-api use.
See the trash and restore methods for an example.

This action does not update the Page modified date. If given a Page or PageArray, also note that it does not update
the status properties of those instantiated Page objects, it only updates the DB value.

Note: Please use addStatus() or removeStatus() instead, unless you need to perform a recursive add/remove status.


@param int|array|Page|PageArray $pageID Page ID, Page, array of page IDs, or PageArray

@param int $status Status per flags in Page::status* constants. Status will be OR'd with existing status, unless $remove is used.

@param bool $recursive Should the status descend into the page's children, and grandchildren, etc? (default=false)

@param bool|int $remove Should the status be removed rather than added? Use integer 2 to overwrite (default=false)

@return int Number of pages updated

## delete()

Permanently delete a page and its fields.

Unlike trash(), pages deleted here are not restorable.

If you attempt to delete a page with children, and don't specifically set the $recursive param to True, then
this method will throw an exception. If a recursive delete fails for any reason, an exception will be thrown.


@param Page $page

@param bool|array $recursive If set to true, then this will attempt to delete all children too.
  If you don't need this argument, optionally provide $options array instead.

@param array $options Optional settings to change behavior:
- `uncacheAll` (bool): Whether to clear memory cache after delete (default=false)
- `recursive` (bool): Same as $recursive argument, may be specified in $options array if preferred.

@return bool|int Returns true (success), or integer of quantity deleted if recursive mode requested.

@throws WireException on fatal error

## _clone()

Clone an entire page (including fields, file assets, and optionally children) and return it.


@param Page $page Page that you want to clone

@param Page|null $parent New parent, if different (default=same parent)

@param bool $recursive Clone the children too? (default=true)

@param array|string $options Optional options that can be passed to clone or save
	- `forceID` (int): force a specific ID
	- `set` (array): Array of properties to set to the clone (you can also do this later)
	- `recursionLevel` (int): recursion level, for internal use only.

@return Page|NullPage the newly cloned page or a NullPage() with id=0 if unsuccessful.

@throws WireException|\Exception on fatal error

## touch()

Update page modified/created/published time to now (or given time)


@param Page|PageArray|array $pages May be Page, PageArray or array of page IDs (integers)

@param null|int|string|array $options Omit (null) to update to now, or unix timestamp or strtotime() recognized time string,
 or if you do not need this argument, you may optionally substitute the $type argument here,
 or in 3.0.183+ you can also specify array of options here instead:
 - `time` (string|int|null): Unix timestamp or strtotime() recognized string to use, omit for use current time (default=null)
 - `type` (string): One of 'modified', 'created', 'published' (default='modified')
 - `user` (bool|User): True to also update modified/created user to current user, or specify User object to use (default=false)

@param string $type Date type to update, one of 'modified', 'created' or 'published' (default='modified') Added 3.0.147
 Skip this argument if using options array for previous argument or if using the default type 'modified'.

@throws WireException|\PDOException if given invalid format for $modified argument or failed database query

@return bool True on success, false on fail

## move()

Move page to specified parent (work in progress)

This method is the same as changing a page parent and saving, but provides a useful shortcut
for some cases with less code. This method:

- Does not save the other custom fields of a page (if any are changed).
- Does not require that output formatting be off (it manages that internally).


@param Page $child Page that you want to move.

@param Page|int|string $parent Parent to move it under (may be Page object, path string, or ID integer).

@param array $options Options to modify behavior (see PagesEditor::save for options).

@return bool True on success or false if not necessary.

@throws WireException if given parent does not exist, or move is not allowed

## sortPage()

Set page $sort value and increment siblings having same or greater sort value

- This method is primarily applicable if configured sortfield is manual “sort” (or “none”).
- This is typically used after a move, sort, clone or delete operation.


@param Page $page Page that you want to set the sort value for

@param int|null $sort New sort value for page or null to pull from $page->sort

@param bool $after If another page already has the sort, make $page go after it rather than before it? (default=false)

@throws WireException if given invalid arguments

@return int Number of sibling pages that had to have sort adjusted

## insertBefore()

Sort one page before another (for pages using manual sort)

Note that if given $sibling parent is different from `$page` parent, then the `$pages->save()`
method will also be called to perform that movement.


@param Page $page Page to move/sort

@param Page $sibling Sibling that page will be moved/sorted before

@param bool $after Specify true to make $page move after $sibling instead of before (default=false)

@throws WireException When conditions don't allow page insertions

## sortRebuild()

Rebuild the “sort” values for all children of the given $parent page, fixing duplicates and gaps

If used on a $parent not currently sorted by by “sort” then it will update the “sort” index to be
consistent with whatever the pages are sorted by.


@param Page $parent

@return int

## replace()

Replace one page with another (work in progress)


@param Page $oldPage

@param Page $newPage

@return Page

@throws WireException

@since 3.0.189 But not yet available in public API

## clear()

Clear a page of its data


@param Page $page

@param array $options

@return bool

@throws WireException

@since 3.0.189
