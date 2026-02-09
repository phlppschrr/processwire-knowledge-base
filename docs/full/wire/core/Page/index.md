# Page

Source: `wire/core/Page.php`

Inherits: `WireData`
Implements: `Countable`, `WireMatchable`


Groups:
Group: [common](group-common.md)
Group: [traversal](group-traversal.md)
Group: [date-time](group-date-time.md)
Group: [status](group-status.md)
Group: [system](group-system.md)
Group: [files](group-files.md)
Group: [other](group-other.md)
Group: [previous](group-previous.md)
Group: [urls](group-urls.md)
Group: [users](group-users.md)

ProcessWire Page

Page is the class used by all instantiated pages and it provides functionality for:

1. Providing get/set access to the Page's properties
2. Accessing the related hierarchy of pages (i.e. parents, children, sibling pages)


Class used by all Page objects in ProcessWire.
$page
The `$page` API variable represents the current page being viewed. However, the documentation
here also applies to all Page objects that you may work with in the API. We use `$page` as the most common example
throughout the documentation, but you can substitute that with any variable name representing a Page.

@link http://processwire.com/api/ref/page/ Offical $page Documentation

@link http://processwire.com/api/selectors/ Official Selectors Documentation




Methods:
- [`__construct(?Template $tpl = null)`](method-__construct.md) Create a new page in memory.
- [`__destruct()`](method-__destruct.md) Destruct this page instance
- [`__clone()`](method-__clone.md) Clone this page instance
- [`set(string $key, mixed $value): Page|WireData`](method-set.md) Set the value of a page property
- [`setQuietly(string $key, mixed $value): $this`](method-setquietly.md) Quietly set the value of a page property.
- [`get(string $key): mixed`](method-get.md) Get the value of a Page property (see details for several options)
- [`getMultiple(array|string $keys, bool $assoc = false): array`](method-getmultiple.md) Get multiple Page property/field values in an array
- [`getField(string|int|Field $field): Field|null`](method-getfield.md) Get a Field object in context or NULL if not valid for this page
- [`getFields(): FieldsArray`](method-getfields.md) Returns a FieldsArray of all Field objects in the context of this Page
- [`hasField(int|string|Field|array $field): bool|string`](method-hasfield.md) Returns whether or not given $field name, ID or object is valid for this Page
- [`getFieldSubfieldValue($key): mixed|null`](method-getfieldsubfieldvalue.md) If given a field.subfield string, returns the associated value
- [`preload(array $fieldNames = array(), array $options = array()): array`](method-preload.md) Preload multiple fields together as a group (experimental)
- [`getUnknown(string $key): null|mixed`](method-___getunknown.md) (hookable) Hookable method called when a request to a field was made that didn't match anything
- [`getFieldFirstValue(string $multiKey, bool $getKey = false): null|mixed`](method-getfieldfirstvalue.md) Given a Multi Key, determine if there are multiple keys requested and return the first non-empty value
- [`getFieldValue(string $key, string $selector = ''): null|mixed`](method-getfieldvalue.md) Get the value for a non-native page field, and call upon Fieldtype to join it if not autojoined
- [`formatFieldValue(Field $field, mixed $value): mixed`](method-formatfieldvalue.md) Return a value consistent with the page’s output formatting state
- [`if(string|bool|int $key, string|callable|mixed $yes = '', string|callable|mixed $no = ''): mixed|string|bool`](method-___if.md) (hookable) If value is available for $key return or call $yes condition (with optional $no condition)
- [`getMarkup(string $key): string`](method-___getmarkup.md) (hookable) Return the markup value for a given field name or {tag} string
- [`getText(string $key, bool $oneLine = false, bool|null $entities = null): string`](method-gettext.md) Same as getMarkup() except returned value is plain text
- [`setUnformatted(string $key, mixed $value): self`](method-setunformatted.md) Set the unformatted value of a field, regardless of current output formatting state
- [`getUnformatted(string $key): mixed`](method-getunformatted.md) Get the unformatted value of a field, regardless of current output formatting state
- [`getFormatted(string $key): mixed`](method-getformatted.md) Get the formatted value of a field, regardless of output formatting state
- [`__get(string $key): mixed`](method-__get.md) Direct access get method
- [`__set(string $key, mixed $value)`](method-__set.md) Direct access set method
- [`callUnknown(string $method, array $arguments): null|mixed`](method-___callunknown.md) (hookable) If method call resulted in no handler, this hookable method is called.
- [`setName(string $value, Language|string|int|null $language = null): $this`](method-setname.md) Set the page name, optionally for specific language
- [`template(null|Template|string|int $template = null): Template|null`](method-template.md) Get or set template
- [`setUser(User|int|string $user, string $userType): $this`](method-setuser.md) Set either the createdUser or the modifiedUser
- [`getUser(string $userType): User|NullPage`](method-getuser.md) Get page’s created or modified user
- [`find(string|array $selector = '', array $options = array()): PageArray`](method-find.md) Find descendant pages matching given selector
- [`findOne(string|array $selector = '', array $options = array()): Page|NullPage`](method-findone.md) Find one descendant page matching given selector
- [`children(string $selector = '', array $options = array()): PageArray|array`](method-children.md) Return this page’s children, optionally filtered by a selector
- [`numChildren(bool|string|array $selector = null): int`](method-numchildren.md) Return number of all children, optionally with conditions
- [`hasChildren(bool|string|array $selector = true): int`](method-haschildren.md) Return the number of visible children, optionally with conditions
- [`child(string|array|int $selector = '', array $options = array()): Page|NullPage`](method-child.md) Return the page’s first single child that matches the given selector.
- [`parent(string|array $selector = ''): Page`](method-parent.md) Return this page’s parent Page, or–if given a selector–the closest matching parent.
- [`parents(string|array|bool $selector = ''): PageArray`](method-parents.md) Return this page’s parent pages, or the parent pages matching the given selector.
- [`numParents(string $selector = ''): int`](method-numparents.md) Return number of parents (depth relative to homepage) that this page has, optionally filtered by a selector
- [`parentsUntil(string|Page|array $selector = '', string|array $filter = ''): PageArray`](method-parentsuntil.md) Return all parents from current page till the one matched by $selector
- [`closest(string|array $selector): Page|NullPage`](method-closest.md) Find the closest parent page matching your selector
- [`rootParent(): Page`](method-___rootparent.md) (hookable) Get the lowest-level, non-homepage parent of this page
- [`siblings(string|array|bool $selector = '', bool $includeCurrent = true): PageArray`](method-siblings.md) Return this Page’s sibling pages, optionally filtered by a selector.
- [`numDescendants(bool|string|array $selector = null): int`](method-numdescendants.md) Return number of descendants (children, grandchildren, great-grandchildren, …), optionally with conditions
- [`next(string|array $selector = '', ?PageArray $siblings = null): Page|NullPage`](method-next.md) Return the next sibling page
- [`nextAll(string|array|bool $selector = '', bool|PageArray $getQty = false, bool $getPrev = false): PageArray|int`](method-nextall.md) Return all sibling pages after this one, optionally matching a selector
- [`nextUntil(string|Page|array $selector = '', string|array $filter = '', ?PageArray $siblings = null): PageArray`](method-nextuntil.md) Return all sibling pages after this one until matching the one specified
- [`prev(string|array $selector = '', ?PageArray $siblings = null): Page|NullPage`](method-prev.md) Return the previous sibling page
- [`prevAll(string|array|bool $selector = '', bool|PageArray $getQty = false): Page|NullPage|int`](method-prevall.md) Return all sibling pages before this one, optionally matching a selector
- [`prevUntil(string|Page|array $selector = '', string|array $filter = '', ?PageArray $siblings = null): PageArray`](method-prevuntil.md) Return all sibling pages before this one until matching the one specified
- [`references(string|bool $selector = '', Field|string|bool $field = ''): PageArray|array`](method-___references.md) (hookable) Return pages that have Page reference fields pointing to this one (references)
- [`links(string|bool $selector = '', string|Field $field = ''): PageArray`](method-___links.md) (hookable) Return pages linking to this one (in Textarea/HTML fields)
- [`getLanguages(): PageArray|null`](method-getlanguages.md) Get languages active for this page and viewable by current user
- [`save(Field|string $field = null, array $options = array()): bool`](method-save.md) Save the entire page to the database, or just a field from it
- [`saveFields(array|string $fields, array $options = array()): array`](method-savefields.md) Save only the given named fields for this page
- [`setAndSave(array|string $key, string|int|bool|object $value = null, array $options = array()): bool`](method-setandsave.md) Quickly set field value(s) and save to database
- [`delete(bool $recursive = false): bool|int`](method-delete.md) Delete this page from the database
- [`trash(): bool`](method-trash.md) Move this page to the trash
- [`count(): int`](method-count.md) Returns number of children page has, affected by output formatting mode.
- [`getIterator(): \ArrayObject`](method-getiterator.md) Enables iteration of the page's properties and fields with PHP’s foreach()
- [`isChanged(string $what = ''): bool`](method-ischanged.md) Has the Page changed since it was loaded?
- [`resetTrackChanges(bool $trackChanges = true): $this`](method-resettrackchanges.md) Clears out any tracked changes and turns change tracking ON or OFF
- [`path(): string`](method-path.md) Returns the Page’s path from the ProcessWire installation root.
- [`url(array|int|string|bool|Language|null $options = null): string`](method-url.md) Returns the URL to the page (optionally with additional $options)
- [`urls(array $options = array()): array`](method-urls.md) Return all URLs that this page can be accessed from (excluding URL segments and pagination)
- [`httpUrl(array $options = array()): string`](method-httpurl.md) Returns the URL to the page, including scheme and hostname
- [`editUrl(array|bool|string $options = array()): string`](method-editurl.md) Return the URL necessary to edit this page
- [`sortfield(): string`](method-sortfield.md) Return the field name by which children are sorted
- [`index($selector = ''): int`](method-index.md) Return the index/position of this page relative to siblings.
- [`render(array|string $options = [], array $options2 = null): string|mixed`](method-___render.md) (hookable) Render output of this Page or a Field
- [`renderPage(array $options = []): string|mixed`](method-___renderpage.md) (hookable) Render page output
- [`renderField(string $fieldName, string $file = '', mixed|null $value = null): mixed|string`](method-___renderfield.md) (hookable) Render given field using site/templates/fields/ markup file
- [`renderValue(mixed $value, string $file = ''): mixed|string`](method-___rendervalue.md) (hookable) Render given value using /site/templates/fields/ markup file
- [`getInputfields(string|array $fieldName = ''): null|InputfieldWrapper`](method-getinputfields.md) Return all Inputfield objects necessary to edit this page
- [`getInputfields(string|array $fieldName = ''): null|InputfieldWrapper`](method-___getinputfields.md) (hookable) Hookable version of getInputfields() method.
- [`getInputfield(string $fieldName): Inputfield|InputfieldWrapper|null`](method-getinputfield.md) Get a single Inputfield for the given field name
- [`edit(string|bool|null $key = null, string|bool|null $markup = null, bool|null $modal = null): string|bool|mixed`](method-___edit.md) (hookable) Get front-end editable output for field (requires PageFrontEdit module to be installed)
- [`setStatus($value): self`](method-setstatus.md) Set the status setting, with some built-in protections
- [`hasStatus(int|string $status): bool`](method-hasstatus.md) Does this page have the given status?
- [`addStatus(int|string $statusFlag): $this`](method-addstatus.md) Add the specified status to this page
- [`removeStatus(int|string $statusFlag): $this`](method-removestatus.md) Remove the specified status from this page
- [`matches(string|Selectors|array $s): bool`](method-matches.md) Given a selector, return whether or not this Page matches using runtime/memory comparison
- [`matchesDatabase(string|Selectors|array $s): bool`](method-matchesdatabase.md) Given a selector, return whether or not this Page matches by querying the database
- [`is(int|string|Selectors $status): bool`](method-is.md) Does this page have the specified status number or template name?
- [`isHidden(): bool`](method-ishidden.md) Does this page have a 'hidden' status?
- [`isUnpublished(): bool`](method-isunpublished.md) Does this page have a 'unpublished' status?
- [`isLocked(): bool`](method-islocked.md) Does this page have a 'locked' status?
- [`isTrash(): bool`](method-istrash.md) Is this Page in the trash?
- [`isPublic(): bool`](method-ispublic.md) Is this page public and viewable by all?
- [`isPublic(): bool`](method-___ispublic.md) (hookable) Hookable implementation for the above isPublic function
- [`status(bool|int $value = false, int|null $status = null): int|array|Page`](method-status.md) Get or set current status
- [`processFieldDataQueue()`](method-processfielddataqueue.md) Process and instantiate any data in the fieldDataQueue
- [`of(bool $outputFormatting = null): bool`](method-of.md) Get or set the current output formatting state of the page
- [`filesManager(): PagefilesManager`](method-filesmanager.md) Return instance of PagefilesManager specific to this Page
- [`secureFiles(): bool|null`](method-securefiles.md) Does this Page use secure Pagefiles?
- [`hasFilesPath(): bool`](method-hasfilespath.md) Does the page have a files path for storing files?
- [`hasFiles(): bool`](method-hasfiles.md) Does the page have a files path and one or more files present in it?
- [`hasFile(string $file, array $options = array()): bool|string`](method-hasfile.md) Does Page have given filename in its files directory?
- [`filesPath(): string`](method-filespath.md) Returns the path for files, creating it if it does not yet exist
- [`filesUrl(): string`](method-filesurl.md) Returns the URL for files, creating it if it does not yet exist
- [`getAccessParent(string $type = 'view'): Page|NullPage`](method-getaccessparent.md) Returns the page from which role/access settings are inherited from
- [`getAccessTemplate(string $type = 'view'): Template|null`](method-getaccesstemplate.md) Returns the template from which role/access settings are inherited from
- [`getAccessRoles(string $type = 'view'): PageArray`](method-getaccessroles.md) Return Roles (PageArray) that have access to this page
- [`hasAccessRole(string|int|Role $role, string $type = 'view'): bool`](method-hasaccessrole.md) Returns whether this page has the given access role
- [`isEqual(string $key, mixed $value1, mixed $value2): bool`](method-isequal.md) Is $value1 equal to $value2?
- [`getHelperInstance(string $className): object|PageComparison|PageAccess|PageTraversal|PageValues`](method-gethelperinstance.md) Return a Page helper class instance that’s common among all Page (and derived) objects in this ProcessWire instance
- [`comparison(): PageComparison`](method-comparison.md)
- [`access(): PageAccess`](method-access.md)
- [`traversal(): PageTraversal`](method-traversal.md)
- [`values(): PageValues`](method-values.md)
- [`meta(string|bool $key = '', null|mixed $value = null): WireDataDB|string|array|int|float`](method-meta.md) Get or set page’s persistent meta data
- [`__toString(): string`](method-__tostring.md) Returns the Page ID in a string
- [`loaded()`](method-___loaded.md) (hookable) Called when this page has been loaded and is now ready and use
- [`editReady(InputfieldWrapper $form)`](method-___editready.md) (hookable) Called when this page has been loaded into the Page editor (ProcessPageEdit)
- [`saveReady(array $changes, string|false $name = false)`](method-___saveready.md) (hookable) Called right before this Page is saved
- [`saved(array $changes, string|false $name = false)`](method-___saved.md) (hookable) Called right after this Page is saved
- [`addReady()`](method-___addready.md) (hookable) Called when this new Page about to be added and saved to the database
- [`added()`](method-___added.md) (hookable) Called after this new Page has been added
- [`moveReady(Page $oldParent, Page $newParent)`](method-___moveready.md) (hookable) Called when this Page is about to be moved to another parent
- [`moved(Page $oldParent, Page $newParent)`](method-___moved.md) (hookable) Called after this Page has been moved to another parent
- [`deleteReady()`](method-___deleteready.md) (hookable) Called right before this page is deleted (and before any of its data is touched)
- [`deleted()`](method-___deleted.md) (hookable) Called after this page and its data has been deleted
- [`cloneReady(Page $copy)`](method-___cloneready.md) (hookable) Called right before this page is cloned
- [`cloned(Page $copy)`](method-___cloned.md) (hookable) Called right after this page has been cloned
- [`renameReady(string $oldName, string $newName)`](method-___renameready.md) (hookable) Called right before this page is renamed (i.e. has its name property changed)
- [`renamed(string $oldName, string $newName)`](method-___renamed.md) (hookable) Called right after this page has been renamed (i.e. had its name property changed)
- [`addStatusReady(string $name, int $value)`](method-___addstatusready.md) (hookable) Called when new status flag about to be added to page but not yet saved
- [`addedStatus(string $name, int $value)`](method-___addedstatus.md) (hookable) Called when a new status flag has been added (and saved)
- [`removeStatusReady(string $name, int $value)`](method-___removestatusready.md) (hookable) Called when status flag is about to removed from page but not yet saved
- [`removedStatus(string $name, int $value)`](method-___removedstatus.md) (hookable) Called when a status flag has been removed from this page (and saved)

Constants:
- [`statusLocked`](const-statuslocked.md)
- [`statusHidden`](const-statushidden.md)
- [`statusUnpublished`](const-statusunpublished.md)

Methods added by PagePermissions.module:
----------------------------------------

- [`viewable($field = '', $checkTemplateFile = true): bool`](method-viewable.md) Returns true if the page (and optionally field) is viewable by the current user, false if not.
- [`editable($field = '', $checkPageEditable = true): bool`](method-editable.md) Returns true if the page (and optionally field) is editable by the current user, false if not.
- [`publishable(): bool`](method-publishable.md) Returns true if the page is publishable by the current user, false if not.
- [`listable(): bool`](method-listable.md) Returns true if the page is listable by the current user, false if not.
- [`deleteable(): bool`](method-deleteable.md) Returns true if the page is deleteable by the current user, false if not.
- [`deletable(): bool`](method-deletable.md) Alias of deleteable().
- [`trashable($orDeleteable = false): bool`](method-trashable.md) Returns true if the page is trashable by the current user, false if not.
- [`restorable(): bool`](method-restorable.md) Returns true if page is in the trash and is capable of being restored to its original location. @since 3.0.107
- [`addable($pageToAdd = null): bool`](method-addable.md) Returns true if the current user can add children to the page, false if not. Optionally specify the page to be added for additional access checking.
- [`moveable($newParent = null): bool`](method-moveable.md) Returns true if the current user can move this page. Optionally specify the new parent to check if the page is moveable to that parent.
- [`sortable(): bool`](method-sortable.md) Returns true if the current user can change the sort order of the current page (within the same parent).
- [`cloneable($recursive = null): bool`](method-cloneable.md) Can current user clone this page? Specify false for $recursive argument to ignore whether children are cloneable. @since 3.0.239
- [`$viewable: bool`](method-viewable.md)
- [`$editable: bool`](method-editable.md)
- [`$publishable: bool`](method-publishable.md)
- [`$deleteable: bool`](method-deleteable.md)
- [`$deletable: bool`](method-deletable.md)
- [`$trashable: bool`](method-trashable.md)
- [`$addable: bool`](method-addable.md)
- [`$moveable: bool`](method-moveable.md)
- [`$sortable: bool`](method-sortable.md)
- [`$listable: bool`](method-listable.md)
- [`$cloneable: bool`](method-cloneable.md) @since 3.0.239

Methods added by PagePathHistory.module (installed by default)
--------------------------------------------------------------

- [`addUrl($url, $language = null): bool`](method-addurl.md) Add a new URL that redirects to this page and save immediately (returns false if already taken).
- [`removeUrl($url): bool`](method-removeurl.md) Remove a URL that redirects to this page and save immediately.
Note: you can use the $page->urls() method to get URLs added by PagePathHistory.

Methods added by LanguageSupport.module (not installed by default)
-----------------------------------------------------------------

- [`setLanguageValue($language, $field, $value): Page`](method-setlanguagevalue.md) Set value for field in language (requires LanguageSupport module). $language may be ID, language name or Language object. Field should be field name (string).
- [`setLanguageValues($field, array $values): Page`](method-setlanguagevalues.md) Set value for field in one or more languages (requires LanguageSupport module). $field should be field/property name (string), $values should be array of values indexed by language name. @since 3.0.236
- [`getLanguageValue($language, $field): mixed`](method-getlanguagevalue.md) Get value for field in language (requires LanguageSupport module). $language may be ID, language name or Language object. Field should be field name (string).
- [`getLanguageValues($field, array $langs = []): array`](method-getlanguagevalues.md) Get values for field or one or more languages (requires LanguageSupport module). $field should be field/property name (string), $langs should be array of language names, or omit for all languages. Returns array of values indexed by language name. @since 3.0.236

Methods added by LanguageSupportPageNames.module (not installed by default)
---------------------------------------------------------------------------

- [`localName($language = null, $useDefaultWhenEmpty = false): string`](method-localname.md) Return the page name in the current user’s language, or specify $language argument (Language object, name, or ID), or TRUE to use default page name when blank (instead of 2nd argument).
- [`localPath($language = null): string`](method-localpath.md) Return the page path in the current user's language, or specify $language argument (Language object, name, or ID).
- [`localUrl($language = null): string`](method-localurl.md) Return the page URL in the current user's language, or specify $language argument (Language object, name, or ID).
- [`localHttpUrl($language = null): string`](method-localhttpurl.md) Return the page URL (including scheme and hostname) in the current user's language, or specify $language argument (Language object, name, or ID).
- [`setLanguageStatus($language, $status = null): Page`](method-setlanguagestatus.md) Set active status for language(s), can be called as `$page->setLanguageStatus('es', true);` or `$page->setLanguageStatus([ 'es' => true, 'br' => false ]);` to set multiple. @since 3.0.236
- [`getLanguageStatus($language = []): array|bool`](method-getlanguagestatus.md) Get active status for language(s). If given a $language (Language or name of language) it returns a boolean. If given multiple language names (array), or argument omitted, it returns array like `[ 'default' => true, 'fr' => false ];`. @since 3.0.236
- [`setLanguageName($language, $name = null): Page`](method-setlanguagename.md) Set page name for language with `$page->setLanguageName('es', 'hola');` or set multiple with `$page->setLanguageName([ 'default' => 'hello', 'es' => 'hola' ]);` @since 3.0.236
- [`getLanguageName($language = []): array|string`](method-getlanguagename.md) Get page name for language(s). If given a Language object, it returns a string. If given array of language names, or argument omitted, it returns an array like `[ 'default' => 'hello', 'es' => 'hola' ];`. @since 3.0.236

Methods added by PageFrontEdit.module (not always installed by default)
-----------------------------------------------------------------------

- [`edit($key = null, $markup = null, $modal = null): string|bool|mixed`](method-___edit.md) Get front-end editable field output or get/set status.

Methods added by ProDrafts.module (if installed)
------------------------------------------------

- [`draft($key = null, $value = null): ProDraft|int|string|Page|array`](method-draft.md) Helper method for drafts (added by ProDrafts).

Hookable methods
----------------

- [`getUnknown($key): mixed`](method-___getunknown.md) Last stop to find a property that we haven't been able to locate. Hook this method to provide a handler.
- [`loaded(): void`](method-___loaded.md) Called when page is loaded into memory and is ready to use.
- [`render($options = [], $options2 = null): string|mixed`](method-___render.md) Render page or field.
- [`renderPage(array $options = []): string|mixed`](method-___renderpage.md) Render page.
- [`renderField($fieldName, $file = ''): string|mixed`](method-___renderfield.md) Render field markup, optionally with file relative to templates/fields/.
- [`references($selector = '', $field = ''): PageArray`](method-___references.md) Return pages that are pointing to this one by way of Page reference fields.
- [`links($selector = '', $field = ''): PageArray`](method-___links.md) Return pages that link to this one contextually in Textarea/HTML fields.
- [`if($key, $yes, $no = ''): string|mixed`](method-___if.md) If value is available for $key return or call $yes condition (with optional $no condition)

Hookable action methods called before or after a page is saved (3.0.253+)
-------------------------------------------------------------------------

- [`editReady(InputfieldWrapper $form): void`](method-___editready.md)
- [`saveReady(array $changes, $name = false): void`](method-___saveready.md)
- [`saved(array $changes, $name = false): void`](method-___saved.md)
- [`addReady(): void`](method-___addready.md)
- [`added(): void`](method-___added.md)
- [`moveReady(Page $oldParent, Page $newParent): void`](method-___moveready.md)
- [`moved(Page $oldParent, Page $newParent): void`](method-___moved.md)
- [`deleteReady(array $options): void`](method-___deleteready.md)
- [`deleted(array $options): void`](method-___deleted.md)
- [`cloneReady(Page $copy): void`](method-___cloneready.md)
- [`cloned(Page $copy): void`](method-___cloned.md)
- [`renameReady(string $oldName, string $newName): void`](method-___renameready.md)
- [`renamed(string $oldName, string $newName): void`](method-___renamed.md)
- [`addStatusReady($name, $value): void`](method-___addstatusready.md)
- [`addedStatus(string $name, int $value): void`](method-___addedstatus.md)
- [`removeStatusReady($name, $value): void`](method-___removestatusready.md)
- [`removedStatus(string $name, int $value): void`](method-___removedstatus.md)


Alias/alternate methods
-----------------------

- [`descendants($selector = '', array $options = array()): PageArray`](method-descendants.md) Find descendant pages, alias of `Page::find()`, see that method for details. @since 3.0.116
- [`descendant($selector = '', array $options = array()): Page|NullPage`](method-descendant.md) Find one descendant page, alias of `Page::findOne()`, see that method for details. @since 3.0.116
