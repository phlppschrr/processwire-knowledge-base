# Pages

Source: `wire/core/Pages.php`

Inherits: `Wire`

ProcessWire Pages ($pages API variable)

Pages
The $pages API variable enables loading and manipulation of Page objects, to and from the database.
Manages Page instances, providing find, load, save and delete capabilities.
The implementation for most of the methods in this class are delegated to other classes (helpers)
but this class provides the common and hookable interface to all of them.
The `$pages` API variable is the most used object in the ProcessWire API.
The most commonly used API methods include:
- `$pages->find($selector);` Finds and returns multiple pages.
- `$pages->get($selector);` Finds a single page with no exclusions.
- `$pages->save($page);` Saves given page.


@link http://processwire.com/api/variables/pages/ Offical $pages Documentation

@link http://processwire.com/api/selectors/ Official Selectors Documentation


PROPERTIES
==========

Methods:
- [`__construct(ProcessWire $wire)`](method-__construct.md)
- [`count($selector = '', $options = array())`](method-count.md)
- [`count(string|array|Selectors $selector = '', array|string $options = array()): int`](method-count.md)
- [`find(string|int|array|Selectors $selector, array|string $options = array()): PageArray|array`](method-___find.md) (hookable)
- [`findOne(string|array|Selectors $selector, array|string $options = array()): Page|NullPage`](method-findone.md)
- [`findMany(string|array|Selectors $selector, array $options = array()): PageArray`](method-findmany.md)
- [`findJoin(string|array|Selectors $selector, array|string|bool $joinFields, array $options = array()): PageArray`](method-findjoin.md)
- [`findIDs(string|array|Selectors $selector, array|bool|int|string $options = array()): array`](method-findids.md)
- [`findRaw(string|array|Selectors|int $selector, string|array|Field $field = '', array $options = array()): array`](method-findraw.md)
- [`get(string|array|Selectors|int $selector, array $options = array()): Page|NullPage`](method-get.md)
- [`getRaw(string|array|Selectors|int $selector, string|array|Field $field = '', array $options = array()): array`](method-getraw.md)
- [`getFresh(Page|string|array|Selectors|int $selectorOrPage, array $options = array()): Page|NullPage`](method-getfresh.md)
- [`getID(string|array|Selectors $selector, bool|array $options = array()): int|array`](method-getid.md)
- [`getByIDs(array|string|WireArray $ids, array $options = array()): PageArray|Page`](method-getbyids.md)
- [`has(string|int|array|Selectors $selector, bool $verbose = false): array|int`](method-has.md)
- [`save(Page $page, array $options = array()): bool`](method-___save.md) (hookable)
- [`saveField(Page $page, string|Field $field, array|string $options = array()): bool`](method-___savefield.md) (hookable)
- [`saveFields(Page $page, array|string|string[]|Field[] $fields, array $options = array()): array`](method-___savefields.md) (hookable)
- [`add(string|Template $template, string|int|Page $parent, string $name = '', array $values = array()): Page`](method-___add.md) (hookable)
- [`new(string|array $selector = ''): Page`](method-___new.md) (hookable)
- [`clone(Page $page, ?Page $parent = null, bool $recursive = true, array|string $options = array()): Page|NullPage`](method-___clone.md) (hookable)
- [`delete(Page $page, bool|array $recursive = false, array $options = array()): bool|int`](method-___delete.md) (hookable)
- [`trash(Page $page, bool $save = true): bool`](method-___trash.md) (hookable)
- [`restore(Page $page, bool $save = true): bool`](method-___restore.md) (hookable)
- [`emptyTrash(array $options = array())`](method-___emptytrash.md) (hookable)
- [`emptyTrash(array $options = array()): int|array`](method-___emptytrash.md) (hookable)
- [`getById(array|WireArray|string|int $_ids, Template|array|null $template = null, int|null $parent_id = null): PageArray|Page`](method-getbyid.md)
- [`getOneById(int $id, array $options = array()): Page|NullPage`](method-getonebyid.md)
- [`getPath(int|Page $id, null|array|Language|int|string $options = array()): string`](method-getpath.md)
- [`_path(int $id): string`](method-_path.md)
- [`getByPath(string $path, array|bool $options = array()): Page|int`](method-getbypath.md)
- [`getInfoByPath(string $path, array $options = array()): array`](method-getinfobypath.md)
- [`touch(Page|PageArray|array $pages, null|int|string|array $options = null, string $type = 'modified'): bool`](method-___touch.md) (hookable)
- [`sort(Page $page, int|bool $value = false): int`](method-___sort.md) (hookable)
- [`insertBefore(Page $page, Page $beforePage)`](method-___insertbefore.md) (hookable)
- [`insertAfter(Page $page, Page $afterPage)`](method-___insertafter.md) (hookable)
- [`getCache(int|string|null $id = null): Page|array|null`](method-getcache.md)
- [`uncache(Page|PageArray|int|null $page = null, array $options = array()): int`](method-uncache.md)
- [`uncacheAll(?Page $page = null, array $options = array()): int`](method-uncacheall.md)
- [`__get(string $name): mixed`](method-__get.md)
- [`of(null|bool $of = null): bool`](method-of.md)
- [`newPage(array|string|Template $options = array()): Page`](method-newpage.md)
- [`__invoke(string|int|array $key): Page|Pages|PageArray`](method-__invoke.md)
- [`loader(): PagesLoader`](method-loader.md)
- [`editor(): PagesEditor`](method-editor.md)
- [`names(): PagesNames`](method-names.md)
- [`cacher(): PagesLoaderCache`](method-cacher.md)
- [`trasher(): PagesTrash`](method-trasher.md)
- [`parents(): PagesParents`](method-parents.md)
- [`porter(): PagesExportImport`](method-porter.md)
- [`raw(): PagesRaw`](method-raw.md)
- [`request(): PagesRequest`](method-request.md)
- [`pathFinder(): PagesPathFinder`](method-pathfinder.md)
- [`saveReady(Page $page)`](method-___saveready.md) (hookable)
- [`saveReady(Page $page): array`](method-___saveready.md) (hookable)
- [`saved(Page $page, array $changes = array(), array $values = array())`](method-___saved.md) (hookable)
- [`addReady(Page $page)`](method-___addready.md) (hookable)
- [`added(Page $page)`](method-___added.md) (hookable)
- [`moveReady(Page $page)`](method-___moveready.md) (hookable)
- [`moved(Page $page)`](method-___moved.md) (hookable)
- [`templateChanged(Page $page)`](method-___templatechanged.md) (hookable)
- [`trashReady(Page $page)`](method-___trashready.md) (hookable)
- [`trashed(Page $page)`](method-___trashed.md) (hookable)
- [`restoreReady(Page $page)`](method-___restoreready.md) (hookable)
- [`restored(Page $page)`](method-___restored.md) (hookable)
- [`deleteReady(Page $page, array $options = array())`](method-___deleteready.md) (hookable)
- [`deleted(Page $page, array $options = array())`](method-___deleted.md) (hookable)
- [`deleteBranchReady(Page $page, array $options)`](method-___deletebranchready.md) (hookable)
- [`deletedBranch(Page $page, array $options, int $numDeleted)`](method-___deletedbranch.md) (hookable)
- [`cloneReady(Page $page, Page $copy)`](method-___cloneready.md) (hookable)
- [`cloned(Page $page, Page $copy)`](method-___cloned.md) (hookable)
- [`renameReady(Page $page)`](method-___renameready.md) (hookable)
- [`renamed(Page $page)`](method-___renamed.md) (hookable)
- [`sorted(Page $page, bool $children = false, int $total = 0)`](method-___sorted.md) (hookable)
- [`statusChanged(Page $page)`](method-___statuschanged.md) (hookable)
- [`statusChangeReady(Page $page)`](method-___statuschangeready.md) (hookable)
- [`published(Page $page)`](method-___published.md) (hookable)
- [`unpublished(Page $page)`](method-___unpublished.md) (hookable)
- [`publishReady(Page $page)`](method-___publishready.md) (hookable)
- [`unpublishReady(Page $page)`](method-___unpublishready.md) (hookable)
- [`found(PageArray $pages, array $details)`](method-___found.md) (hookable)
- [`saveFieldReady(Page $page, Field $field)`](method-___savefieldready.md) (hookable)
- [`savedField(Page $page, Field $field)`](method-___savedfield.md) (hookable)
- [`savePageOrFieldReady(Page $page, string $fieldName = '')`](method-___savepageorfieldready.md) (hookable)
- [`savedPageOrField(Page $page, array $changes = array())`](method-___savedpageorfield.md) (hookable)

Constants:
- [`nameMaxLength`](const-namemaxlength.md)
- [`defaultRootName`](const-defaultrootname.md)

HOOKABLE METHODS
================

- [`find($selectorString, array $options = array()): PageArray`](method-___find.md) Find and return all pages matching the given selector string. Returns a PageArray.
- [`save(Page $page, $options = array()): bool`](method-___save.md) Save any changes made to the given $page. Same as $page->save(); Returns true on success.
- [`saveField(Page $page, $field, array $options = array()): bool`](method-___savefield.md) Save just the named field from $page. Same as: $page->save('field')
- [`saveFields(Page $page, $fields, array $options = array()): array`](method-___savefields.md) Saved multiple named fields for $page. @since 3.0.242
- [`trash(Page $page, $save = true): bool`](method-___trash.md) Move a page to the trash. If you have already set the parent to somewhere in the trash, then this method won't attempt to set it again.
- [`restore(Page $page, $save = true): bool`](method-___restore.md) Restore a trashed page to its original location.
- [`emptyTrash(array $options = array()): int|array`](method-___emptytrash.md) Empty the trash and return number of pages deleted.
- [`delete(Page $page, $recursive = false, array $options = array()): bool`](method-___delete.md) Permanently delete a page and it's fields. Unlike trash(), pages deleted here are not restorable. If you attempt to delete a page with children, and don't specifically set the $recursive param to True, then this method will throw an exception. If a recursive delete fails for any reason, an exception will be thrown.
- [`clone(Page $page, Page $parent = null, $recursive = true, $options = array()): Page|NullPage`](method-___clone.md) Clone an entire page, it's assets and children and return it.
- [`add($template, $parent, $name = '', array $values = array()): Page|NullPage`](method-___add.md)
- [`sort(Page $page, $value = false): int`](method-___sort.md) Set the “sort” value for given $page while adjusting siblings, or re-build sort for its children.
- [`insertBefore(Page $page, Page $beforePage): void`](method-___insertbefore.md) Insert one page as a sibling before another.
- [`insertAfter(Page $page, Page $afterPage): void`](method-___insertafter.md) Insert one page as a sibling after another.
- [`touch($pages, $options = null, $type = 'modified'): bool`](method-___touch.md) Update page modification time to now (or the given modification time).

METHODS PURELY FOR HOOKS
========================
You can hook these methods, but you should not call them directly.
See the phpdoc in the actual methods for more details about arguments and additional properties that can be accessed.

- [`saveReady(Page $page): array`](method-___saveready.md) Hook called just before a page is saved.
- `@method saved(Page $page, array $changes = array(), $values = array()) Hook called after a page is successfully saved.` saved(Page $page, array $changes = array(), $values = array()) Hook called after a page is successfully saved.
- `@method addReady(Page $page)` addReady(Page $page)
- `@method added(Page $page) Hook called when a new page has been added.` added(Page $page) Hook called when a new page has been added.
- `@method moveReady(Page $page) Hook called when a page is about to be moved to another parent.` moveReady(Page $page) Hook called when a page is about to be moved to another parent.
- `@method moved(Page $page) Hook called when a page has been moved from one parent to another.` moved(Page $page) Hook called when a page has been moved from one parent to another.
- `@method templateChanged(Page $page) Hook called when a page template has been changed.` templateChanged(Page $page) Hook called when a page template has been changed.
- `@method trashReady(Page $page) Hook called when a page is about to be moved to the trash.` trashReady(Page $page) Hook called when a page is about to be moved to the trash.
- `@method trashed(Page $page) Hook called when a page has been moved to the trash.` trashed(Page $page) Hook called when a page has been moved to the trash.
- `@method restoreReady(Page $page) Hook called when a page is about to be restored out of the trash.` restoreReady(Page $page) Hook called when a page is about to be restored out of the trash.
- `@method restored(Page $page) Hook called when a page has been moved OUT of the trash.` restored(Page $page) Hook called when a page has been moved OUT of the trash.
- `@method deleteReady(Page $page, array $options) Hook called just before a page is deleted.` deleteReady(Page $page, array $options) Hook called just before a page is deleted.
- `@method deleted(Page $page, array $options) Hook called after a page has been deleted.` deleted(Page $page, array $options) Hook called after a page has been deleted.
- `@method deleteBranchReady(Page $page, array $options) Hook called before a branch of pages deleted, on initiating page only.` deleteBranchReady(Page $page, array $options) Hook called before a branch of pages deleted, on initiating page only.
- `@method deletedBranch(Page $page, array $options, $numDeleted) Hook called after branch of pages deleted, on initiating page only.` deletedBranch(Page $page, array $options, $numDeleted) Hook called after branch of pages deleted, on initiating page only.
- `@method cloneReady(Page $page, Page $copy) Hook called just before a page is cloned.` cloneReady(Page $page, Page $copy) Hook called just before a page is cloned.
- `@method cloned(Page $page, Page $copy) Hook called after a page has been successfully cloned.` cloned(Page $page, Page $copy) Hook called after a page has been successfully cloned.
- `@method renameReady(Page $page) Hook called when a page is about to be renamed.` renameReady(Page $page) Hook called when a page is about to be renamed.
- `@method renamed(Page $page) Hook called after a page has been successfully renamed.` renamed(Page $page) Hook called after a page has been successfully renamed.
- `@method sorted(Page $page, $children = false, $total = 0) Hook called after $page has been sorted.` sorted(Page $page, $children = false, $total = 0) Hook called after $page has been sorted.
- `@method statusChangeReady(Page $page) Hook called when a page's status has changed and is about to be saved.` statusChangeReady(Page $page) Hook called when a page's status has changed and is about to be saved.
- `@method statusChanged(Page $page) Hook called after a page status has been changed and saved.` statusChanged(Page $page) Hook called after a page status has been changed and saved.
- `@method publishReady(Page $page) Hook called just before an unpublished page is published.` publishReady(Page $page) Hook called just before an unpublished page is published.
- `@method published(Page $page) Hook called after an unpublished page has just been published.` published(Page $page) Hook called after an unpublished page has just been published.
- `@method unpublishReady(Page $page) Hook called just before a pubished page is unpublished.` unpublishReady(Page $page) Hook called just before a pubished page is unpublished.
- `@method unpublished(Page $page) Hook called after a published page has just been unpublished.` unpublished(Page $page) Hook called after a published page has just been unpublished.
- `@method saveFieldReady(Page $page, Field $field) Hook called just before a saveField() method saves a page fied.` saveFieldReady(Page $page, Field $field) Hook called just before a saveField() method saves a page fied.
- `@method savedField(Page $page, Field $field) Hook called after saveField() method successfully executes.` savedField(Page $page, Field $field) Hook called after saveField() method successfully executes.
- `@method savePageOrFieldReady(Page $page, $fieldName = '') Hook inclusive of both saveReady() and saveFieldReady().` savePageOrFieldReady(Page $page, $fieldName = '') Hook inclusive of both saveReady() and saveFieldReady().
- `@method savedPageOrField(Page $page, array $changes) Hook inclusive of both saved() and savedField().` savedPageOrField(Page $page, array $changes) Hook inclusive of both saved() and savedField().
- `@method found(PageArray $pages, array $details) Hook called at the end of a $pages->find().` found(PageArray $pages, array $details) Hook called at the end of a $pages->find().
