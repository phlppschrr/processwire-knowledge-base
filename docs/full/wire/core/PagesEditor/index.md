# PagesEditor

Source: `wire/core/PagesEditor.php`

Inherits: `Wire`

ProcessWire Pages Editor

Pages Editor
$pages->editor
Implements page editing and manipulation methods for the $pages API variable.
Please always use `$pages->method()` rather than `$pages->editor->method()` in cases where there is overlap.

Methods:
- [`__construct(Pages $pages)`](method-__construct.md)
- [`isCloning(bool $getDepth = false): bool|int`](method-iscloning.md)
- [`add(string|Template $template, string|int|Page $parent, string $name = '', array $values = array()): Page`](method-add.md)
- [`isSaveable(Page $page, string &$reason, string|Field $fieldName = '', array $options = array()): bool`](method-issaveable.md)
- [`isMoveable(Page $page, Page $oldParent, Page $newParent, string &$reason): bool`](method-ismoveable.md)
- [`isDeleteable(Page $page, bool $throw = false): bool`](method-isdeleteable.md)
- [`setupNew(Page $page)`](method-setupnew.md)
- [`setupPageName(Page $page, array $options = array()): string`](method-setuppagename.md)
- [`save(Page $page, array $options = array()): bool`](method-save.md)
- [`savePageQuery(Page $page, array $options): bool`](method-savepagequery.md)
- [`savePageQueryException(Page $page, \PDOStatement $query, \PDOException|\Exception $exception, array $options): bool`](method-savepagequeryexception.md)
- [`savePageFinish(Page $page, bool $isNew, array $options): bool`](method-savepagefinish.md)
- [`saveField(Page $page, $field, $options = array())`](method-savefield.md)
- [`saveField(Page $page, string|Field $field, array|string $options = array()): bool`](method-savefield.md)
- [`saveFields(Page $page, array|string|string[]|Field[] $fields, array $options = array()): array`](method-savefields.md)
- [`addStatus(Page $page, int $status): bool`](method-addstatus.md)
- [`removeStatus(Page $page, int $status): bool`](method-removestatus.md)
- [`saveStatus(Page $page): bool`](method-savestatus.md)
- [`savePageStatus(int|array|Page|PageArray $pageID, int $status, bool $recursive = false, bool|int $remove = false): int`](method-savepagestatus.md)
- [`delete(Page $page, bool|array $recursive = false, array $options = array()): bool|int`](method-delete.md)
- [`_clone(Page $page, ?Page $parent = null, bool $recursive = true, array|string $options = array()): Page|NullPage`](method-_clone.md)
- [`touch(Page|PageArray|array $pages, null|int|string|array $options = null, string $type = 'modified'): bool`](method-touch.md)
- [`move(Page $child, Page|int|string $parent, array $options = array()): bool`](method-move.md)
- [`sortPage(Page $page, int|null $sort = null, bool $after = false): int`](method-sortpage.md)
- [`insertBefore(Page $page, Page $sibling, bool $after = false)`](method-insertbefore.md)
- [`sortRebuild(Page $parent): int`](method-sortrebuild.md)
- [`replace(Page $oldPage, Page $newPage): Page`](method-replace.md)
- [`clear(Page $page, array $options = array()): bool`](method-clear.md)
