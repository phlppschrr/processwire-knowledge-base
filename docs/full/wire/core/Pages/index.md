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

ProcessWire 3.x, Copyright 2024 by Ryan Cramer
https://processwire.com

@link http://processwire.com/api/variables/pages/ Offical $pages Documentation

@link http://processwire.com/api/selectors/ Official Selectors Documentation


PROPERTIES
==========

HOOKABLE METHODS
================

@method PageArray find($selectorString, array $options = array()) Find and return all pages matching the given selector string. Returns a PageArray.

@method bool save(Page $page, $options = array()) Save any changes made to the given $page. Same as $page->save(); Returns true on success.

@method bool saveField(Page $page, $field, array $options = array()) Save just the named field from $page. Same as: $page->save('field')

@method array saveFields(Page $page, $fields, array $options = array()) Saved multiple named fields for $page. @since 3.0.242

@method bool trash(Page $page, $save = true) Move a page to the trash. If you have already set the parent to somewhere in the trash, then this method won't attempt to set it again.

@method bool restore(Page $page, $save = true) Restore a trashed page to its original location.

@method int|array emptyTrash(array $options = array()) Empty the trash and return number of pages deleted.

@method bool delete(Page $page, $recursive = false, array $options = array()) Permanently delete a page and it's fields. Unlike trash(), pages deleted here are not restorable. If you attempt to delete a page with children, and don't specifically set the $recursive param to True, then this method will throw an exception. If a recursive delete fails for any reason, an exception will be thrown.

@method Page|NullPage clone(Page $page, Page $parent = null, $recursive = true, $options = array()) Clone an entire page, it's assets and children and return it.

@method Page|NullPage add($template, $parent, $name = '', array $values = array())

@method int sort(Page $page, $value = false) Set the “sort” value for given $page while adjusting siblings, or re-build sort for its children.

@method void insertBefore(Page $page, Page $beforePage) Insert one page as a sibling before another.

@method void insertAfter(Page $page, Page $afterPage) Insert one page as a sibling after another.

@method bool touch($pages, $options = null, $type = 'modified') Update page modification time to now (or the given modification time).

METHODS PURELY FOR HOOKS
========================
You can hook these methods, but you should not call them directly.
See the phpdoc in the actual methods for more details about arguments and additional properties that can be accessed.

@method array saveReady(Page $page) Hook called just before a page is saved.

@method saved(Page $page, array $changes = array(), $values = array()) Hook called after a page is successfully saved.

@method addReady(Page $page)

@method added(Page $page) Hook called when a new page has been added.

@method moveReady(Page $page) Hook called when a page is about to be moved to another parent.

@method moved(Page $page) Hook called when a page has been moved from one parent to another.

@method templateChanged(Page $page) Hook called when a page template has been changed.

@method trashReady(Page $page) Hook called when a page is about to be moved to the trash.

@method trashed(Page $page) Hook called when a page has been moved to the trash.

@method restoreReady(Page $page) Hook called when a page is about to be restored out of the trash.

@method restored(Page $page) Hook called when a page has been moved OUT of the trash.

@method deleteReady(Page $page, array $options) Hook called just before a page is deleted.

@method deleted(Page $page, array $options) Hook called after a page has been deleted.

@method deleteBranchReady(Page $page, array $options) Hook called before a branch of pages deleted, on initiating page only.

@method deletedBranch(Page $page, array $options, $numDeleted) Hook called after branch of pages deleted, on initiating page only.

@method cloneReady(Page $page, Page $copy) Hook called just before a page is cloned.

@method cloned(Page $page, Page $copy) Hook called after a page has been successfully cloned.

@method renameReady(Page $page) Hook called when a page is about to be renamed.

@method renamed(Page $page) Hook called after a page has been successfully renamed.

@method sorted(Page $page, $children = false, $total = 0) Hook called after $page has been sorted.

@method statusChangeReady(Page $page) Hook called when a page's status has changed and is about to be saved.

@method statusChanged(Page $page) Hook called after a page status has been changed and saved.

@method publishReady(Page $page) Hook called just before an unpublished page is published.

@method published(Page $page) Hook called after an unpublished page has just been published.

@method unpublishReady(Page $page) Hook called just before a pubished page is unpublished.

@method unpublished(Page $page) Hook called after a published page has just been unpublished.

@method saveFieldReady(Page $page, Field $field) Hook called just before a saveField() method saves a page fied.

@method savedField(Page $page, Field $field) Hook called after saveField() method successfully executes.

@method savePageOrFieldReady(Page $page, $fieldName = '') Hook inclusive of both saveReady() and saveFieldReady().

@method savedPageOrField(Page $page, array $changes) Hook inclusive of both saved() and savedField().

@method found(PageArray $pages, array $details) Hook called at the end of a $pages->find().

Methods:
Method: [__construct()](method-__construct.md)
Method: [count()](method-count.md)
Method: [count()](method-count.md)
Method: [___find()](method-___find.md)
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
Method: [___save()](method-___save.md)
Method: [___saveField()](method-___savefield.md)
Method: [___saveFields()](method-___savefields.md)
Method: [___add()](method-___add.md)
Method: [___new()](method-___new.md)
Method: [___clone()](method-___clone.md)
Method: [___delete()](method-___delete.md)
Method: [___trash()](method-___trash.md)
Method: [___restore()](method-___restore.md)
Method: [___emptyTrash()](method-___emptytrash.md)
Method: [___emptyTrash()](method-___emptytrash.md)
Method: [getById()](method-getbyid.md)
Method: [getOneById()](method-getonebyid.md)
Method: [getPath()](method-getpath.md)
Method: [_path()](method-_path.md)
Method: [getByPath()](method-getbypath.md)
Method: [getInfoByPath()](method-getinfobypath.md)
Method: [___touch()](method-___touch.md)
Method: [___sort()](method-___sort.md)
Method: [___insertBefore()](method-___insertbefore.md)
Method: [___insertAfter()](method-___insertafter.md)
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
Method: [___saveReady()](method-___saveready.md)
Method: [___saveReady()](method-___saveready.md)
Method: [___saved()](method-___saved.md)
Method: [___addReady()](method-___addready.md)
Method: [___added()](method-___added.md)
Method: [___moveReady()](method-___moveready.md)
Method: [___moved()](method-___moved.md)
Method: [___templateChanged()](method-___templatechanged.md)
Method: [___trashReady()](method-___trashready.md)
Method: [___trashed()](method-___trashed.md)
Method: [___restoreReady()](method-___restoreready.md)
Method: [___restored()](method-___restored.md)
Method: [___deleteReady()](method-___deleteready.md)
Method: [___deleted()](method-___deleted.md)
Method: [___deleteBranchReady()](method-___deletebranchready.md)
Method: [___deletedBranch()](method-___deletedbranch.md)
Method: [___cloneReady()](method-___cloneready.md)
Method: [___cloned()](method-___cloned.md)
Method: [___renameReady()](method-___renameready.md)
Method: [___renamed()](method-___renamed.md)
Method: [___sorted()](method-___sorted.md)
Method: [___statusChanged()](method-___statuschanged.md)
Method: [___statusChangeReady()](method-___statuschangeready.md)
Method: [___published()](method-___published.md)
Method: [___unpublished()](method-___unpublished.md)
Method: [___publishReady()](method-___publishready.md)
Method: [___unpublishReady()](method-___unpublishready.md)
Method: [___found()](method-___found.md)
Method: [___saveFieldReady()](method-___savefieldready.md)
Method: [___savedField()](method-___savedfield.md)
Method: [___savePageOrFieldReady()](method-___savepageorfieldready.md)
Method: [___savedPageOrField()](method-___savedpageorfield.md)

Constants:
Const: [nameMaxLength](const-namemaxlength.md)
Const: [defaultRootName](const-defaultrootname.md)
