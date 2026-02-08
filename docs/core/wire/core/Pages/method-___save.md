# $pages->___save(Page $page, $options = array()): bool

Source: `wire/core/Pages.php`

Save a page object and its fields to database.

If the page is new, it will be inserted. If existing, it will be updated.
This is the same as calling `$page->save()`. If you want to just save a particular field
in a Page, use `$page->save($fieldName)` instead.

~~~~~~
// Modify a page and save it
$p = $pages->get('/festivals/decatur/beer/');
$p->of(false); // turn off output formatting, if it's on
$p->title = "Decatur Beer Festival";
$p->summary = "Come and enjoy fine beer and good company at the Decatur Beer Festival.";
$pages->save($p);
~~~~~~

## Arguments

- Page $page Page object to save
- array $options Optional array to modify default behavior, with one or more of the following: - `uncacheAll` (boolean): Whether the memory cache should be cleared (default=true). - `resetTrackChanges` (boolean): Whether the page's change tracking should be reset (default=true). - `quiet` (boolean): When true, modified date and modified_users_id won't be updated (default=false). - `adjustName` (boolean): Adjust page name to ensure it is unique within its parent (default=true). - `forceID` (integer): Use this ID instead of an auto-assigned one (new page) or current ID (existing page). - `ignoreFamily` (boolean): Bypass check of allowed family/parent settings when saving (default=false). - `noHooks` (boolean): Prevent before/after save hooks (default=false), please also use $pages->___save() for call. - `noFields` (boolean): Bypass saving of custom fields, leaving only native properties to be saved (default=false).

## Return value

bool True on success, false on failure

## Throws

- WireException

## See also

- [Page::save()](../Page/method-save.md)
- [Pages::saveField()](method-___savefield.md)
