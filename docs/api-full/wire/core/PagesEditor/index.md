# PagesEditor

Source: `wire/core/PagesEditor.php`

Inherits: `Wire`

## Summary

ProcessWire Pages Editor

Common methods:
- [`isCloning()`](method-iscloning.md)
- [`add()`](method-add.md)
- [`isSaveable()`](method-issaveable.md)
- [`isMoveable()`](method-ismoveable.md)
- [`isDeleteable()`](method-isdeleteable.md)

Pages Editor
`$pages->editor`
Implements page editing and manipulation methods for the `$pages` API variable.
Please always use `$pages->method()` rather than `$pages->editor->method()` in cases where there is overlap.

## Methods
- [`__construct(Pages $pages)`](method-__construct.md) Construct
- [`isCloning(bool $getDepth = false): bool|int`](method-iscloning.md) Are we currently in a page clone?
- [`add(string|Template $template, string|int|Page $parent, string $name = '', array $values = array()): Page`](method-add.md) Add a new page using the given template to the given parent
- [`isSaveable(Page $page, string &$reason, string|Field $fieldName = '', array $options = array()): bool`](method-issaveable.md) Is the given page in a state where it can be saved from the API?
- [`isMoveable(Page $page, Page $oldParent, Page $newParent, string &$reason): bool`](method-ismoveable.md) Return whether given Page is moveable from `$oldParent` to `$newParent`
- [`isDeleteable(Page $page, bool $throw = false): bool`](method-isdeleteable.md) Is the given page deleteable from the API?
- [`setupNew(Page $page)`](method-setupnew.md) Auto-populate some fields for a new page that does not yet exist
- [`setupPageName(Page $page, array $options = array()): string`](method-setuppagename.md) Auto-assign a page name to gven page
- [`save(Page $page, array $options = array()): bool`](method-save.md) Save a page object and it's fields to database.
- [`savePageQuery(Page $page, array $options): bool`](method-savepagequery.md) Execute query to save to pages table
- [`savePageQueryException(Page $page, \PDOStatement $query, \PDOException|\Exception $exception, array $options): bool`](method-savepagequeryexception.md) Handle Exception for savePageQuery()
- [`savePageFinish(Page $page, bool $isNew, array $options): bool`](method-savepagefinish.md) Save individual Page fields and supporting actions
- [`saveField(Page $page, $field, $options = array())`](method-savefield.md) TBD Identify if parent changed and call saveParentsTable() where appropriate
- [`saveField(Page $page, string|Field $field, array|string $options = array()): bool`](method-savefield.md) Save just a field from the given page
- [`saveFields(Page $page, array|string|string[]|Field[] $fields, array $options = array()): array`](method-savefields.md) Save multiple named fields from given page
- [`addStatus(Page $page, int $status): bool`](method-addstatus.md) Silently add status flag to a Page and save
- [`removeStatus(Page $page, int $status): bool`](method-removestatus.md) Silently remove status flag from a Page and save
- [`saveStatus(Page $page): bool`](method-savestatus.md) Silently save whatever the given Page’s status currently is
- [`savePageStatus(int|array|Page|PageArray $pageID, int $status, bool $recursive = false, bool|int $remove = false): int`](method-savepagestatus.md) Add or remove a Page status and commit to DB, optionally recursive with the children, grandchildren, and so on.
- [`delete(Page $page, bool|array $recursive = false, array $options = array()): bool|int`](method-delete.md) Permanently delete a page and its fields.
- [`_clone(Page $page, ?Page $parent = null, bool $recursive = true, array|string $options = array()): Page|NullPage`](method-_clone.md) Clone an entire page (including fields, file assets, and optionally children) and return it.
- [`touch(Page|PageArray|array $pages, null|int|string|array $options = null, string $type = 'modified'): bool`](method-touch.md) Update page modified/created/published time to now (or given time)
- [`move(Page $child, Page|int|string $parent, array $options = array()): bool`](method-move.md) Move page to specified parent (work in progress)
- [`sortPage(Page $page, int|null $sort = null, bool $after = false): int`](method-sortpage.md) Set page `$sort` value and increment siblings having same or greater sort value
- [`insertBefore(Page $page, Page $sibling, bool $after = false)`](method-insertbefore.md) Sort one page before another (for pages using manual sort)
- [`sortRebuild(Page $parent): int`](method-sortrebuild.md) Rebuild the “sort” values for all children of the given `$parent` page, fixing duplicates and gaps
- [`replace(Page $oldPage, Page $newPage): Page`](method-replace.md) Replace one page with another (work in progress)
- [`clear(Page $page, array $options = array()): bool`](method-clear.md) Clear a page of its data
