# $pagesEditor->save(Page $page, $options = array()): bool

Source: `wire/core/PagesEditor.php`

Save a page object and it's fields to database.

If the page is new, it will be inserted. If existing, it will be updated.

This is the same as calling $page->save()

If you want to just save a particular field in a Page, use $page->save($fieldName) instead.

## Arguments

- Page $page Page to save
- array $options Optional array with the following optional elements: - `uncacheAll` (bool): Whether the memory cache should be cleared (default=true) - `resetTrackChanges` (bool): Whether the page's change tracking should be reset (default=true) - `quiet` (bool): When true, created/modified time+user will use values from $page rather than current user+time (default=false) - `adjustName` (bool): Adjust page name to ensure it is unique within its parent (default=true) - `forceID` (integer): Use this ID instead of an auto-assigned on (new page) or current ID (existing page) - `ignoreFamily` (bool): Bypass check of allowed family/parent settings when saving (default=false) - `noHooks` (bool): Prevent before/after save hooks from being called (default=false) - `noFields` (bool): Bypass saving of custom fields (default=false) - `caller` (string): Optional name of calling function (i.e. 'pages.trash'), for internal use (default='') 3.0.235+ - `callback` (string|callable): Hook method name from $pages or callable to trigger after save. It receives a single $page argument. For internal use. (default='') 3.0.235+

## Return value

bool True on success, false on failure

## Throws

- WireException
