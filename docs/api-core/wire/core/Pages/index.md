# Pages

Source: `wire/core/Pages.php`

Inherits: `Wire`

## Summary

ProcessWire Pages (`$pages` API variable)

Common methods:
- [`init()`](method-init.md)
- [`count()`](method-count.md)
- [`find()`](method-___find.md)
- [`findOne()`](method-findone.md)
- [`findMany()`](method-findmany.md)

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


## Properties

## Hookable Methods

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

## Methods Purely For Hooks
You can hook these methods, but you should not call them directly.
See the phpdoc in the actual methods for more details about arguments and additional properties that can be accessed.

- [`saveReady(Page $page): array`](method-___saveready.md) Hook called just before a page is saved.
- [`saved(Page $page, array $changes = array(), $values = array())`](method-___saved.md) Hook called after a page is successfully saved.
- [`addReady(Page $page)`](method-___addready.md)
- [`added(Page $page)`](method-___added.md) Hook called when a new page has been added.
- [`moveReady(Page $page)`](method-___moveready.md) Hook called when a page is about to be moved to another parent.
- [`moved(Page $page)`](method-___moved.md) Hook called when a page has been moved from one parent to another.
- [`templateChanged(Page $page)`](method-___templatechanged.md) Hook called when a page template has been changed.
- [`trashReady(Page $page)`](method-___trashready.md) Hook called when a page is about to be moved to the trash.
- [`trashed(Page $page)`](method-___trashed.md) Hook called when a page has been moved to the trash.
- [`restoreReady(Page $page)`](method-___restoreready.md) Hook called when a page is about to be restored out of the trash.
- [`restored(Page $page)`](method-___restored.md) Hook called when a page has been moved OUT of the trash.
- [`deleteReady(Page $page, array $options)`](method-___deleteready.md) Hook called just before a page is deleted.
- [`deleted(Page $page, array $options)`](method-___deleted.md) Hook called after a page has been deleted.
- [`deleteBranchReady(Page $page, array $options)`](method-___deletebranchready.md) Hook called before a branch of pages deleted, on initiating page only.
- [`deletedBranch(Page $page, array $options, $numDeleted)`](method-___deletedbranch.md) Hook called after branch of pages deleted, on initiating page only.
- [`cloneReady(Page $page, Page $copy)`](method-___cloneready.md) Hook called just before a page is cloned.
- [`cloned(Page $page, Page $copy)`](method-___cloned.md) Hook called after a page has been successfully cloned.
- [`renameReady(Page $page)`](method-___renameready.md) Hook called when a page is about to be renamed.
- [`renamed(Page $page)`](method-___renamed.md) Hook called after a page has been successfully renamed.
- [`sorted(Page $page, $children = false, $total = 0)`](method-___sorted.md) Hook called after $page has been sorted.
- [`statusChangeReady(Page $page)`](method-___statuschangeready.md) Hook called when a page's status has changed and is about to be saved.
- [`statusChanged(Page $page)`](method-___statuschanged.md) Hook called after a page status has been changed and saved.
- [`publishReady(Page $page)`](method-___publishready.md) Hook called just before an unpublished page is published.
- [`published(Page $page)`](method-___published.md) Hook called after an unpublished page has just been published.
- [`unpublishReady(Page $page)`](method-___unpublishready.md) Hook called just before a pubished page is unpublished.
- [`unpublished(Page $page)`](method-___unpublished.md) Hook called after a published page has just been unpublished.
- [`saveFieldReady(Page $page, Field $field)`](method-___savefieldready.md) Hook called just before a saveField() method saves a page fied.
- [`savedField(Page $page, Field $field)`](method-___savedfield.md) Hook called after saveField() method successfully executes.
- [`savePageOrFieldReady(Page $page, $fieldName = '')`](method-___savepageorfieldready.md) Hook inclusive of both saveReady() and saveFieldReady().
- [`savedPageOrField(Page $page, array $changes)`](method-___savedpageorfield.md) Hook inclusive of both saved() and savedField().
- [`found(PageArray $pages, array $details)`](method-___found.md) Hook called at the end of a $pages->find().

## Methods
- [`__construct(ProcessWire $wire)`](method-__construct.md) Create the Pages object
- [`count(string|array|Selectors $selector = '', array|string $options = array()): int`](method-count.md) Count and return how many pages will match the given selector.
- [`find(string|int|array|Selectors $selector, array|string $options = array()): PageArray|array`](method-___find.md) (hookable) Given a Selector string, return the Page objects that match in a PageArray.
- [`findOne(string|array|Selectors $selector, array|string $options = array()): Page|NullPage`](method-findone.md) Like find() but returns only the first match as a Page object (not PageArray).
- [`findMany(string|array|Selectors $selector, array $options = array()): PageArray`](method-findmany.md) Like find(), but with “lazy loading” to support giant result sets without running out of memory.
- [`findJoin(string|array|Selectors $selector, array|string|bool $joinFields, array $options = array()): PageArray`](method-findjoin.md) Find pages and specify which fields to join (overriding configured autojoin settings)
- [`findIDs(string|array|Selectors $selector, array|bool|int|string $options = array()): array`](method-findids.md) Like find() except returns array of IDs rather than Page objects
- [`findRaw(string|array|Selectors|int $selector, string|array|Field $field = '', array $options = array()): array`](method-findraw.md) Find pages and return raw data from them in a PHP array
- [`get(string|array|Selectors|int $selector, array $options = array()): Page|NullPage`](method-get.md) Returns the first page matching the given selector with no exclusions
- [`getRaw(string|array|Selectors|int $selector, string|array|Field $field = '', array $options = array()): array`](method-getraw.md) Get single page and return raw data in an associative array
- [`getFresh(Page|string|array|Selectors|int $selectorOrPage, array $options = array()): Page|NullPage`](method-getfresh.md) Get a fresh, non-cached copy of a Page from the database
- [`getID(string|array|Selectors $selector, bool|array $options = array()): int|array`](method-getid.md) Get one ID of page matching given selector with no exclusions, like get() but returns ID rather than a Page
- [`getByIDs(array|string|WireArray $ids, array $options = array()): PageArray|Page`](method-getbyids.md) Given array or CSV string of Page IDs, return a PageArray
- [`has(string|int|array|Selectors $selector, bool $verbose = false): array|int`](method-has.md) Is there any page that matches the given $selector in the system? (with no exclusions)
- [`save(Page $page, array $options = array()): bool`](method-___save.md) (hookable) Save a page object and its fields to database.
- [`saveField(Page $page, string|Field $field, array|string $options = array()): bool`](method-___savefield.md) (hookable) Save only a field from the given page
- [`saveFields(Page $page, array|string|string[]|Field[] $fields, array $options = array()): array`](method-___savefields.md) (hookable) Save multiple named fields from given page
- [`add(string|Template $template, string|int|Page $parent, string $name = '', array $values = array()): Page`](method-___add.md) (hookable) Add a new page using the given template and parent
- [`new(string|array $selector = ''): Page`](method-___new.md) (hookable) Create a new Page populated from selector string or array and save to database
- [`clone(Page $page, ?Page $parent = null, bool $recursive = true, array|string $options = array()): Page|NullPage`](method-___clone.md) (hookable) Clone entire page and return it
- [`delete(Page $page, bool|array $recursive = false, array $options = array()): bool|int`](method-___delete.md) (hookable) Permanently delete a page, its fields and assets.
- [`trash(Page $page, bool $save = true): bool`](method-___trash.md) (hookable) Move a page to the trash
- [`restore(Page $page, bool $save = true): bool`](method-___restore.md) (hookable) Restore a page in the trash back to its original location and state
- [`emptyTrash(array $options = array()): int|array`](method-___emptytrash.md) (hookable) Delete all pages in the trash
- [`getById(array|WireArray|string|int $_ids, Template|array|null $template = null, int|null $parent_id = null): PageArray|Page`](method-getbyid.md) Given an array or CSV string of Page IDs, return a PageArray (internal API)
- [`getOneById(int $id, array $options = array()): Page|NullPage`](method-getonebyid.md) Get one page by ID
- [`getPath(int|Page $id, null|array|Language|int|string $options = array()): string`](method-getpath.md) Given an ID, return a path to a page, without loading the actual page
- [`_path(int $id): string`](method-_path.md) Alias of getPath method for backwards compatibility
- [`getByPath(string $path, array|bool $options = array()): Page|int`](method-getbypath.md) Get a page by its path, similar to $pages->get('/path/to/page/') but with more options
- [`getInfoByPath(string $path, array $options = array()): array`](method-getinfobypath.md) Get verbose array of info about a given page path
- [`touch(Page|PageArray|array $pages, null|int|string|array $options = null, string $type = 'modified'): bool`](method-___touch.md) (hookable) Update page modification time to now (or the given modification time)
- [`sort(Page $page, int|bool $value = false): int`](method-___sort.md) (hookable) Set the “sort” value for given $page while adjusting siblings, or re-build sort for its children
- [`insertBefore(Page $page, Page $beforePage)`](method-___insertbefore.md) (hookable) Sort/move one page above another (for manually sorted pages)
- [`insertAfter(Page $page, Page $afterPage)`](method-___insertafter.md) (hookable) Sort/move one page after another (for manually sorted pages)
- [`getCache(int|string|null $id = null): Page|array|null`](method-getcache.md) Given a Page ID, return it if it's cached, or NULL of it's not.
- [`uncache(Page|PageArray|int|null $page = null, array $options = array()): int`](method-uncache.md) Remove the given page(s) from the cache, or uncache all by omitting $page argument
- [`uncacheAll(?Page $page = null, array $options = array()): int`](method-uncacheall.md) Remove all pages from the cache (to clear memory)
- [`__get(string $name): mixed`](method-__get.md) Return a fuel or other property set to the Pages instance
- [`of(null|bool $of = null): bool`](method-of.md) Get or set the current output formatting state
- [`newPage(array|string|Template $options = array()): Page`](method-newpage.md) Return a new Page object without saving it to the database
- [`__invoke(string|int|array $key): Page|Pages|PageArray`](method-__invoke.md) Enables use of $pages(123), $pages('/path/') or $pages('selector string')
- [`loader(): PagesLoader`](method-loader.md) Get PagesLoader instance which provides methods for finding and loading pages
- [`editor(): PagesEditor`](method-editor.md) Get PagesEditor instance which provides methods for saving pages to the database
- [`names(): PagesNames`](method-names.md) Get PagesNames instance which provides API methods specific to generating and modifying page names
- [`cacher(): PagesLoaderCache`](method-cacher.md) Get PagesLoaderCache instance which provides methods for caching pages in memory
- [`trasher(): PagesTrash`](method-trasher.md) Get PagesTrash instance which provides methods for managing the Pages trash
- [`parents(): PagesParents`](method-parents.md) Get PagesParents instance which provides methods for managing parent/child relationships in the pages_parents table
- [`porter(): PagesExportImport`](method-porter.md) Get new instance of PagesExportImport for exporting and importing pages
- [`raw(): PagesRaw`](method-raw.md) Get the PagesRaw instance which provides methods for findind and loading raw pages data
- [`request(): PagesRequest`](method-request.md) Get the PagesRequest instance which provides methods for identifying and loading page from current request URL
- [`pathFinder(): PagesPathFinder`](method-pathfinder.md) Get the PagesPathFinder instance which provides methods for finding pages by paths
- [`saveReady(Page $page): array`](method-___saveready.md) (hookable) Hook called just before a page is saved
- [`saved(Page $page, array $changes = array(), array $values = array())`](method-___saved.md) (hookable) Hook called after a page is successfully saved
- [`addReady(Page $page)`](method-___addready.md) (hookable) Hook called when a new page is about to be added and saved to the database
- [`added(Page $page)`](method-___added.md) (hookable) Hook called after a new page has been added
- [`moveReady(Page $page)`](method-___moveready.md) (hookable) Hook called when a page is about to be moved to another parent
- [`moved(Page $page)`](method-___moved.md) (hookable) Hook called when a page has been moved from one parent to another
- [`templateChanged(Page $page)`](method-___templatechanged.md) (hookable) Hook called when a page's template has been changed
- [`trashReady(Page $page)`](method-___trashready.md) (hookable) Hook called when a Page is about to be trashed
- [`trashed(Page $page)`](method-___trashed.md) (hookable) Hook called when a page has been moved to the trash
- [`restoreReady(Page $page)`](method-___restoreready.md) (hookable) Hook called when a page is about to be moved OUT of the trash (restored)
- [`restored(Page $page)`](method-___restored.md) (hookable) Hook called when a page has been moved OUT of the trash (restored)
- [`deleteReady(Page $page, array $options = array())`](method-___deleteready.md) (hookable) Hook called when a page is about to be deleted, but before data has been touched
- [`deleted(Page $page, array $options = array())`](method-___deleted.md) (hookable) Hook called after a page and its data have been deleted
- [`deleteBranchReady(Page $page, array $options)`](method-___deletebranchready.md) (hookable) Hook called before a branch of pages is about to be deleted, called on root page of branch only
- [`deletedBranch(Page $page, array $options, int $numDeleted)`](method-___deletedbranch.md) (hookable) Hook called after a a branch of pages has been deleted, called on root page of branch only
- [`cloneReady(Page $page, Page $copy)`](method-___cloneready.md) (hookable) Hook called when a page is about to be cloned, but before data has been touched
- [`cloned(Page $page, Page $copy)`](method-___cloned.md) (hookable) Hook called when a page has been cloned
- [`renameReady(Page $page)`](method-___renameready.md) (hookable) Hook called when a page is about to be renamed i.e. had its name field change)
- [`renamed(Page $page)`](method-___renamed.md) (hookable) Hook called when a page has been renamed (i.e. had its name field change)
- [`sorted(Page $page, bool $children = false, int $total = 0)`](method-___sorted.md) (hookable) Hook called after a page has been sorted, or had its children re-sorted
- [`statusChanged(Page $page)`](method-___statuschanged.md) (hookable) Hook called when a page status has been changed and saved
- [`statusChangeReady(Page $page)`](method-___statuschangeready.md) (hookable) Hook called when a page's status is about to be changed and saved
- [`published(Page $page)`](method-___published.md) (hookable) Hook called after an unpublished page has just been published
- [`unpublished(Page $page)`](method-___unpublished.md) (hookable) Hook called after published page has just been unpublished
- [`publishReady(Page $page)`](method-___publishready.md) (hookable) Hook called right before an unpublished page is published and saved
- [`unpublishReady(Page $page)`](method-___unpublishready.md) (hookable) Hook called right before a published page is unpublished and saved
- [`found(PageArray $pages, array $details)`](method-___found.md) (hookable) Hook called at the end of a $pages->find(), includes extra info not seen in the resulting PageArray
- [`saveFieldReady(Page $page, Field $field)`](method-___savefieldready.md) (hookable) Hook called when Pages::saveField is ready to execute
- [`savedField(Page $page, Field $field)`](method-___savedfield.md) (hookable) Hook called after Pages::saveField successfully executes
- [`savePageOrFieldReady(Page $page, string $fieldName = '')`](method-___savepageorfieldready.md) (hookable) Hook called when either of Pages::save or Pages::saveField is ready to execute
- [`savedPageOrField(Page $page, array $changes = array())`](method-___savedpageorfield.md) (hookable) Hook called after either of Pages::save or Pages::saveField successfully executes

## Constants
- [`nameMaxLength = 128`](const-namemaxlength.md)
- [`defaultRootName = 'home'`](const-defaultrootname.md)
