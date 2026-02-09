# Pages

Source: `wire/core/Pages.php`

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

HOOKABLE METHODS
================

- [find($selectorString, array $options = array(): PageArray](method-___find.md) ) Find and return all pages matching the given selector string. Returns a PageArray.

- [save(Page $page, $options = array(): bool](method-___save.md) ) Save any changes made to the given $page. Same as $page->save(); Returns true on success.

- [saveField(Page $page, $field, array $options = array(): bool](method-___savefield.md) ) Save just the named field from $page. Same as: $page->save('field')

- [saveFields(Page $page, $fields, array $options = array(): array](method-___savefields.md) ) Saved multiple named fields for $page. @since 3.0.242

- [trash(Page $page, $save = true): bool](method-___trash.md) Move a page to the trash. If you have already set the parent to somewhere in the trash, then this method won't attempt to set it again.

- [restore(Page $page, $save = true): bool](method-___restore.md) Restore a trashed page to its original location.

- [emptyTrash(array $options = array(): int|array](method-___emptytrash.md) ) Empty the trash and return number of pages deleted.

- [delete(Page $page, $recursive = false, array $options = array(): bool](method-___delete.md) ) Permanently delete a page and it's fields. Unlike trash(), pages deleted here are not restorable. If you attempt to delete a page with children, and don't specifically set the $recursive param to True, then this method will throw an exception. If a recursive delete fails for any reason, an exception will be thrown.

- [clone(Page $page, Page $parent = null, $recursive = true, $options = array(): Page|NullPage](method-___clone.md) ) Clone an entire page, it's assets and children and return it.

- [add($template, $parent, $name = '', array $values = array(): Page|NullPage](method-___add.md) )

- [sort(Page $page, $value = false): int](method-___sort.md) Set the “sort” value for given $page while adjusting siblings, or re-build sort for its children.

- [insertBefore(Page $page, Page $beforePage): void](method-___insertbefore.md) Insert one page as a sibling before another.

- [insertAfter(Page $page, Page $afterPage): void](method-___insertafter.md) Insert one page as a sibling after another.

- [touch($pages, $options = null, $type = 'modified'): bool](method-___touch.md) Update page modification time to now (or the given modification time).

METHODS PURELY FOR HOOKS
========================
You can hook these methods, but you should not call them directly.
See the phpdoc in the actual methods for more details about arguments and additional properties that can be accessed.

- [saveReady(Page $page): array](method-___saveready.md) Hook called just before a page is saved.

- [saved(Page $page, array $changes = array()](method-___saved.md) , $values = array()) Hook called after a page is successfully saved.

- [addReady(Page $page)](method-___addready.md)

- [added(Page $page)](method-___added.md) Hook called when a new page has been added.

- [moveReady(Page $page)](method-___moveready.md) Hook called when a page is about to be moved to another parent.

- [moved(Page $page)](method-___moved.md) Hook called when a page has been moved from one parent to another.

- [templateChanged(Page $page)](method-___templatechanged.md) Hook called when a page template has been changed.

- [trashReady(Page $page)](method-___trashready.md) Hook called when a page is about to be moved to the trash.

- [trashed(Page $page)](method-___trashed.md) Hook called when a page has been moved to the trash.

- [restoreReady(Page $page)](method-___restoreready.md) Hook called when a page is about to be restored out of the trash.

- [restored(Page $page)](method-___restored.md) Hook called when a page has been moved OUT of the trash.

- [deleteReady(Page $page, array $options)](method-___deleteready.md) Hook called just before a page is deleted.

- [deleted(Page $page, array $options)](method-___deleted.md) Hook called after a page has been deleted.

- [deleteBranchReady(Page $page, array $options)](method-___deletebranchready.md) Hook called before a branch of pages deleted, on initiating page only.

- [deletedBranch(Page $page, array $options, $numDeleted)](method-___deletedbranch.md) Hook called after branch of pages deleted, on initiating page only.

- [cloneReady(Page $page, Page $copy)](method-___cloneready.md) Hook called just before a page is cloned.

- [cloned(Page $page, Page $copy)](method-___cloned.md) Hook called after a page has been successfully cloned.

- [renameReady(Page $page)](method-___renameready.md) Hook called when a page is about to be renamed.

- [renamed(Page $page)](method-___renamed.md) Hook called after a page has been successfully renamed.

- [sorted(Page $page, $children = false, $total = 0)](method-___sorted.md) Hook called after $page has been sorted.

- [statusChangeReady(Page $page)](method-___statuschangeready.md) Hook called when a page's status has changed and is about to be saved.

- [statusChanged(Page $page)](method-___statuschanged.md) Hook called after a page status has been changed and saved.

- [publishReady(Page $page)](method-___publishready.md) Hook called just before an unpublished page is published.

- [published(Page $page)](method-___published.md) Hook called after an unpublished page has just been published.

- [unpublishReady(Page $page)](method-___unpublishready.md) Hook called just before a pubished page is unpublished.

- [unpublished(Page $page)](method-___unpublished.md) Hook called after a published page has just been unpublished.

- [saveFieldReady(Page $page, Field $field)](method-___savefieldready.md) Hook called just before a saveField() method saves a page fied.

- [savedField(Page $page, Field $field)](method-___savedfield.md) Hook called after saveField() method successfully executes.

- [savePageOrFieldReady(Page $page, $fieldName = '')](method-___savepageorfieldready.md) Hook inclusive of both saveReady() and saveFieldReady().

- [savedPageOrField(Page $page, array $changes)](method-___savedpageorfield.md) Hook inclusive of both saved() and savedField().

- [found(PageArray $pages, array $details)](method-___found.md) Hook called at the end of a $pages->find().

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
