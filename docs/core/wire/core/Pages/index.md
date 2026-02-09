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
Method: [__construct()](method-__construct.md)
Method: [count()](method-count.md)
Method: [count()](method-count.md)
Method: [find()](method-___find.md) (hookable)
Method: [findOne()](method-findone.md)
Method: [findMany()](method-findmany.md)
Method: [findJoin()](method-findjoin.md)
Method: [findIDs()](method-findids.md)
Method: [findRaw()](method-findraw.md)
Method: [get()](method-get.md)
Method: [getRaw()](method-getraw.md)
Method: [getFresh()](method-getfresh.md)
Method: [getID()](method-getid.md)
Method: [getByIDs()](method-getbyids.md)
Method: [has()](method-has.md)
Method: [save()](method-___save.md) (hookable)
Method: [saveField()](method-___savefield.md) (hookable)
Method: [saveFields()](method-___savefields.md) (hookable)
Method: [add()](method-___add.md) (hookable)
Method: [new()](method-___new.md) (hookable)
Method: [clone()](method-___clone.md) (hookable)
Method: [delete()](method-___delete.md) (hookable)
Method: [trash()](method-___trash.md) (hookable)
Method: [restore()](method-___restore.md) (hookable)
Method: [emptyTrash()](method-___emptytrash.md) (hookable)
Method: [emptyTrash()](method-___emptytrash.md) (hookable)
Method: [getById()](method-getbyid.md)
Method: [getOneById()](method-getonebyid.md)
Method: [getPath()](method-getpath.md)
Method: [_path()](method-_path.md)
Method: [getByPath()](method-getbypath.md)
Method: [getInfoByPath()](method-getinfobypath.md)
Method: [touch()](method-___touch.md) (hookable)
Method: [sort()](method-___sort.md) (hookable)
Method: [insertBefore()](method-___insertbefore.md) (hookable)
Method: [insertAfter()](method-___insertafter.md) (hookable)
Method: [getCache()](method-getcache.md)
Method: [uncache()](method-uncache.md)
Method: [uncacheAll()](method-uncacheall.md)
Method: [__get()](method-__get.md)
Method: [of()](method-of.md)
Method: [newPage()](method-newpage.md)
Method: [__invoke()](method-__invoke.md)
Method: [loader()](method-loader.md)
Method: [editor()](method-editor.md)
Method: [names()](method-names.md)
Method: [cacher()](method-cacher.md)
Method: [trasher()](method-trasher.md)
Method: [parents()](method-parents.md)
Method: [porter()](method-porter.md)
Method: [raw()](method-raw.md)
Method: [request()](method-request.md)
Method: [pathFinder()](method-pathfinder.md)
Method: [saveReady()](method-___saveready.md) (hookable)
Method: [saveReady()](method-___saveready.md) (hookable)
Method: [saved()](method-___saved.md) (hookable)
Method: [addReady()](method-___addready.md) (hookable)
Method: [added()](method-___added.md) (hookable)
Method: [moveReady()](method-___moveready.md) (hookable)
Method: [moved()](method-___moved.md) (hookable)
Method: [templateChanged()](method-___templatechanged.md) (hookable)
Method: [trashReady()](method-___trashready.md) (hookable)
Method: [trashed()](method-___trashed.md) (hookable)
Method: [restoreReady()](method-___restoreready.md) (hookable)
Method: [restored()](method-___restored.md) (hookable)
Method: [deleteReady()](method-___deleteready.md) (hookable)
Method: [deleted()](method-___deleted.md) (hookable)
Method: [deleteBranchReady()](method-___deletebranchready.md) (hookable)
Method: [deletedBranch()](method-___deletedbranch.md) (hookable)
Method: [cloneReady()](method-___cloneready.md) (hookable)
Method: [cloned()](method-___cloned.md) (hookable)
Method: [renameReady()](method-___renameready.md) (hookable)
Method: [renamed()](method-___renamed.md) (hookable)
Method: [sorted()](method-___sorted.md) (hookable)
Method: [statusChanged()](method-___statuschanged.md) (hookable)
Method: [statusChangeReady()](method-___statuschangeready.md) (hookable)
Method: [published()](method-___published.md) (hookable)
Method: [unpublished()](method-___unpublished.md) (hookable)
Method: [publishReady()](method-___publishready.md) (hookable)
Method: [unpublishReady()](method-___unpublishready.md) (hookable)
Method: [found()](method-___found.md) (hookable)
Method: [saveFieldReady()](method-___savefieldready.md) (hookable)
Method: [savedField()](method-___savedfield.md) (hookable)
Method: [savePageOrFieldReady()](method-___savepageorfieldready.md) (hookable)
Method: [savedPageOrField()](method-___savedpageorfield.md) (hookable)

Constants:
Const: [nameMaxLength](const-namemaxlength.md)
Const: [defaultRootName](const-defaultrootname.md)

HOOKABLE METHODS
================

- [find($selectorString, array $options = array()): PageArray](method-___find.md) Find and return all pages matching the given selector string. Returns a PageArray.
- [save(Page $page, $options = array()): bool](method-___save.md) Save any changes made to the given $page. Same as $page->save(); Returns true on success.
- [saveField(Page $page, $field, array $options = array()): bool](method-___savefield.md) Save just the named field from $page. Same as: $page->save('field')
- [saveFields(Page $page, $fields, array $options = array()): array](method-___savefields.md) Saved multiple named fields for $page. @since 3.0.242
- [trash(Page $page, $save = true): bool](method-___trash.md) Move a page to the trash. If you have already set the parent to somewhere in the trash, then this method won't attempt to set it again.
- [restore(Page $page, $save = true): bool](method-___restore.md) Restore a trashed page to its original location.
- [emptyTrash(array $options = array()): int|array](method-___emptytrash.md) Empty the trash and return number of pages deleted.
- [delete(Page $page, $recursive = false, array $options = array()): bool](method-___delete.md) Permanently delete a page and it's fields. Unlike trash(), pages deleted here are not restorable. If you attempt to delete a page with children, and don't specifically set the $recursive param to True, then this method will throw an exception. If a recursive delete fails for any reason, an exception will be thrown.
- [clone(Page $page, Page $parent = null, $recursive = true, $options = array()): Page|NullPage](method-___clone.md) Clone an entire page, it's assets and children and return it.
- [add($template, $parent, $name = '', array $values = array()): Page|NullPage](method-___add.md)
- [sort(Page $page, $value = false): int](method-___sort.md) Set the “sort” value for given $page while adjusting siblings, or re-build sort for its children.
- [insertBefore(Page $page, Page $beforePage): void](method-___insertbefore.md) Insert one page as a sibling before another.
- [insertAfter(Page $page, Page $afterPage): void](method-___insertafter.md) Insert one page as a sibling after another.
- [touch($pages, $options = null, $type = 'modified'): bool](method-___touch.md) Update page modification time to now (or the given modification time).

METHODS PURELY FOR HOOKS
========================
You can hook these methods, but you should not call them directly.
See the phpdoc in the actual methods for more details about arguments and additional properties that can be accessed.

- [saveReady(Page $page): array](method-___saveready.md) Hook called just before a page is saved.
- @method saved(Page $page, array $changes = array(), $values = array()) Hook called after a page is successfully saved. saved(Page $page, array $changes = array(), $values = array()) Hook called after a page is successfully saved.
- @method addReady(Page $page) addReady(Page $page)
- @method added(Page $page) Hook called when a new page has been added. added(Page $page) Hook called when a new page has been added.
- @method moveReady(Page $page) Hook called when a page is about to be moved to another parent. moveReady(Page $page) Hook called when a page is about to be moved to another parent.
- @method moved(Page $page) Hook called when a page has been moved from one parent to another. moved(Page $page) Hook called when a page has been moved from one parent to another.
- @method templateChanged(Page $page) Hook called when a page template has been changed. templateChanged(Page $page) Hook called when a page template has been changed.
- @method trashReady(Page $page) Hook called when a page is about to be moved to the trash. trashReady(Page $page) Hook called when a page is about to be moved to the trash.
- @method trashed(Page $page) Hook called when a page has been moved to the trash. trashed(Page $page) Hook called when a page has been moved to the trash.
- @method restoreReady(Page $page) Hook called when a page is about to be restored out of the trash. restoreReady(Page $page) Hook called when a page is about to be restored out of the trash.
- @method restored(Page $page) Hook called when a page has been moved OUT of the trash. restored(Page $page) Hook called when a page has been moved OUT of the trash.
- @method deleteReady(Page $page, array $options) Hook called just before a page is deleted. deleteReady(Page $page, array $options) Hook called just before a page is deleted.
- @method deleted(Page $page, array $options) Hook called after a page has been deleted. deleted(Page $page, array $options) Hook called after a page has been deleted.
- @method deleteBranchReady(Page $page, array $options) Hook called before a branch of pages deleted, on initiating page only. deleteBranchReady(Page $page, array $options) Hook called before a branch of pages deleted, on initiating page only.
- @method deletedBranch(Page $page, array $options, $numDeleted) Hook called after branch of pages deleted, on initiating page only. deletedBranch(Page $page, array $options, $numDeleted) Hook called after branch of pages deleted, on initiating page only.
- @method cloneReady(Page $page, Page $copy) Hook called just before a page is cloned. cloneReady(Page $page, Page $copy) Hook called just before a page is cloned.
- @method cloned(Page $page, Page $copy) Hook called after a page has been successfully cloned. cloned(Page $page, Page $copy) Hook called after a page has been successfully cloned.
- @method renameReady(Page $page) Hook called when a page is about to be renamed. renameReady(Page $page) Hook called when a page is about to be renamed.
- @method renamed(Page $page) Hook called after a page has been successfully renamed. renamed(Page $page) Hook called after a page has been successfully renamed.
- @method sorted(Page $page, $children = false, $total = 0) Hook called after $page has been sorted. sorted(Page $page, $children = false, $total = 0) Hook called after $page has been sorted.
- @method statusChangeReady(Page $page) Hook called when a page's status has changed and is about to be saved. statusChangeReady(Page $page) Hook called when a page's status has changed and is about to be saved.
- @method statusChanged(Page $page) Hook called after a page status has been changed and saved. statusChanged(Page $page) Hook called after a page status has been changed and saved.
- @method publishReady(Page $page) Hook called just before an unpublished page is published. publishReady(Page $page) Hook called just before an unpublished page is published.
- @method published(Page $page) Hook called after an unpublished page has just been published. published(Page $page) Hook called after an unpublished page has just been published.
- @method unpublishReady(Page $page) Hook called just before a pubished page is unpublished. unpublishReady(Page $page) Hook called just before a pubished page is unpublished.
- @method unpublished(Page $page) Hook called after a published page has just been unpublished. unpublished(Page $page) Hook called after a published page has just been unpublished.
- @method saveFieldReady(Page $page, Field $field) Hook called just before a saveField() method saves a page fied. saveFieldReady(Page $page, Field $field) Hook called just before a saveField() method saves a page fied.
- @method savedField(Page $page, Field $field) Hook called after saveField() method successfully executes. savedField(Page $page, Field $field) Hook called after saveField() method successfully executes.
- @method savePageOrFieldReady(Page $page, $fieldName = '') Hook inclusive of both saveReady() and saveFieldReady(). savePageOrFieldReady(Page $page, $fieldName = '') Hook inclusive of both saveReady() and saveFieldReady().
- @method savedPageOrField(Page $page, array $changes) Hook inclusive of both saved() and savedField(). savedPageOrField(Page $page, array $changes) Hook inclusive of both saved() and savedField().
- @method found(PageArray $pages, array $details) Hook called at the end of a $pages->find(). found(PageArray $pages, array $details) Hook called at the end of a $pages->find().
