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
- [`__construct(?Template $tpl = null)`](method-__construct.md)
- [`__destruct()`](method-__destruct.md)
- [`__clone()`](method-__clone.md)
- [`set(string $key, mixed $value): Page|WireData`](method-set.md)
- [`setQuietly(string $key, mixed $value): $this`](method-setquietly.md)
- [`get(string $key): mixed`](method-get.md)
- [`getMultiple(array|string $keys, bool $assoc = false): array`](method-getmultiple.md)
- [`getField(string|int|Field $field): Field|null`](method-getfield.md)
- [`getFields(): FieldsArray`](method-getfields.md)
- [`hasField(int|string|Field|array $field): bool|string`](method-hasfield.md)
- [`getFieldSubfieldValue($key): mixed|null`](method-getfieldsubfieldvalue.md)
- [`preload(array $fieldNames = array(), array $options = array()): array`](method-preload.md)
- [`getUnknown(string $key): null|mixed`](method-___getunknown.md) (hookable)
- [`getFieldFirstValue(string $multiKey, bool $getKey = false): null|mixed`](method-getfieldfirstvalue.md)
- [`getFieldValue(string $key, string $selector = ''): null|mixed`](method-getfieldvalue.md)
- [`formatFieldValue(Field $field, mixed $value): mixed`](method-formatfieldvalue.md)
- [`if(string|bool|int $key, string|callable|mixed $yes = '', string|callable|mixed $no = ''): mixed|string|bool`](method-___if.md) (hookable)
- [`getMarkup(string $key): string`](method-___getmarkup.md) (hookable)
- [`getText(string $key, bool $oneLine = false, bool|null $entities = null): string`](method-gettext.md)
- [`setUnformatted(string $key, mixed $value): self`](method-setunformatted.md)
- [`getUnformatted(string $key): mixed`](method-getunformatted.md)
- [`getFormatted(string $key): mixed`](method-getformatted.md)
- [`__get(string $key): mixed`](method-__get.md)
- [`__set(string $key, mixed $value)`](method-__set.md)
- [`callUnknown(string $method, array $arguments): null|mixed`](method-___callunknown.md) (hookable)
- [`setName(string $value, Language|string|int|null $language = null): $this`](method-setname.md)
- [`template(null|Template|string|int $template = null): Template|null`](method-template.md)
- [`setUser(User|int|string $user, string $userType): $this`](method-setuser.md)
- [`getUser(string $userType): User|NullPage`](method-getuser.md)
- [`find(string|array $selector = '', array $options = array()): PageArray`](method-find.md)
- [`findOne(string|array $selector = '', array $options = array()): Page|NullPage`](method-findone.md)
- [`children(string $selector = '', array $options = array()): PageArray|array`](method-children.md)
- [`numChildren(bool|string|array $selector = null): int`](method-numchildren.md)
- [`hasChildren(bool|string|array $selector = true): int`](method-haschildren.md)
- [`child(string|array|int $selector = '', array $options = array()): Page|NullPage`](method-child.md)
- [`parent(string|array $selector = ''): Page`](method-parent.md)
- [`parents(string|array|bool $selector = ''): PageArray`](method-parents.md)
- [`numParents(string $selector = ''): int`](method-numparents.md)
- [`parentsUntil(string|Page|array $selector = '', string|array $filter = ''): PageArray`](method-parentsuntil.md)
- [`closest(string|array $selector): Page|NullPage`](method-closest.md)
- [`rootParent(): Page`](method-___rootparent.md) (hookable)
- [`siblings(string|array|bool $selector = '', bool $includeCurrent = true): PageArray`](method-siblings.md)
- [`numDescendants(bool|string|array $selector = null): int`](method-numdescendants.md)
- [`next(string|array $selector = '', ?PageArray $siblings = null): Page|NullPage`](method-next.md)
- [`nextAll(string|array|bool $selector = '', bool|PageArray $getQty = false, bool $getPrev = false): PageArray|int`](method-nextall.md)
- [`nextUntil(string|Page|array $selector = '', string|array $filter = '', ?PageArray $siblings = null): PageArray`](method-nextuntil.md)
- [`prev(string|array $selector = '', ?PageArray $siblings = null): Page|NullPage`](method-prev.md)
- [`prevAll(string|array|bool $selector = '', bool|PageArray $getQty = false): Page|NullPage|int`](method-prevall.md)
- [`prevUntil(string|Page|array $selector = '', string|array $filter = '', ?PageArray $siblings = null): PageArray`](method-prevuntil.md)
- [`references(string|bool $selector = '', Field|string|bool $field = ''): PageArray|array`](method-___references.md) (hookable)
- [`links(string|bool $selector = '', string|Field $field = ''): PageArray`](method-___links.md) (hookable)
- [`getLanguages(): PageArray|null`](method-getlanguages.md)
- [`save(Field|string $field = null, array $options = array()): bool`](method-save.md)
- [`saveFields(array|string $fields, array $options = array()): array`](method-savefields.md)
- [`setAndSave(array|string $key, string|int|bool|object $value = null, array $options = array()): bool`](method-setandsave.md)
- [`delete(bool $recursive = false): bool|int`](method-delete.md)
- [`trash(): bool`](method-trash.md)
- [`count(): int`](method-count.md)
- [`getIterator(): \ArrayObject`](method-getiterator.md)
- [`isChanged(string $what = ''): bool`](method-ischanged.md)
- [`resetTrackChanges(bool $trackChanges = true): $this`](method-resettrackchanges.md)
- [`path(): string`](method-path.md)
- [`url(array|int|string|bool|Language|null $options = null): string`](method-url.md)
- [`urls(array $options = array()): array`](method-urls.md)
- [`httpUrl(array $options = array()): string`](method-httpurl.md)
- [`editUrl(array|bool|string $options = array()): string`](method-editurl.md)
- [`sortfield(): string`](method-sortfield.md)
- [`index($selector = ''): int`](method-index.md)
- [`render(array|string $options = [], array $options2 = null): string|mixed`](method-___render.md) (hookable)
- [`renderPage(array $options = []): string|mixed`](method-___renderpage.md) (hookable)
- [`renderField(string $fieldName, string $file = '', mixed|null $value = null): mixed|string`](method-___renderfield.md) (hookable)
- [`renderValue(mixed $value, string $file = ''): mixed|string`](method-___rendervalue.md) (hookable)
- [`getInputfields(string|array $fieldName = ''): null|InputfieldWrapper`](method-getinputfields.md)
- [`getInputfields(string|array $fieldName = ''): null|InputfieldWrapper`](method-___getinputfields.md) (hookable)
- [`getInputfield(string $fieldName): Inputfield|InputfieldWrapper|null`](method-getinputfield.md)
- [`edit(string|bool|null $key = null, string|bool|null $markup = null, bool|null $modal = null): string|bool|mixed`](method-___edit.md) (hookable)
- [`setStatus($value): self`](method-setstatus.md)
- [`hasStatus(int|string $status): bool`](method-hasstatus.md)
- [`addStatus(int|string $statusFlag): $this`](method-addstatus.md)
- [`removeStatus(int|string $statusFlag): $this`](method-removestatus.md)
- [`matches(string|Selectors|array $s): bool`](method-matches.md)
- [`matchesDatabase(string|Selectors|array $s): bool`](method-matchesdatabase.md)
- [`is(int|string|Selectors $status): bool`](method-is.md)
- [`isHidden(): bool`](method-ishidden.md)
- [`isUnpublished(): bool`](method-isunpublished.md)
- [`isLocked(): bool`](method-islocked.md)
- [`isTrash(): bool`](method-istrash.md)
- [`isPublic(): bool`](method-ispublic.md)
- [`isPublic(): bool`](method-___ispublic.md) (hookable)
- [`status(bool|int $value = false, int|null $status = null): int|array|Page`](method-status.md)
- [`processFieldDataQueue()`](method-processfielddataqueue.md)
- [`of(bool $outputFormatting = null): bool`](method-of.md)
- [`filesManager(): PagefilesManager`](method-filesmanager.md)
- [`secureFiles(): bool|null`](method-securefiles.md)
- [`hasFilesPath(): bool`](method-hasfilespath.md)
- [`hasFiles(): bool`](method-hasfiles.md)
- [`hasFile(string $file, array $options = array()): bool|string`](method-hasfile.md)
- [`filesPath(): string`](method-filespath.md)
- [`filesUrl(): string`](method-filesurl.md)
- [`getAccessParent(string $type = 'view'): Page|NullPage`](method-getaccessparent.md)
- [`getAccessTemplate(string $type = 'view'): Template|null`](method-getaccesstemplate.md)
- [`getAccessRoles(string $type = 'view'): PageArray`](method-getaccessroles.md)
- [`hasAccessRole(string|int|Role $role, string $type = 'view'): bool`](method-hasaccessrole.md)
- [`isEqual(string $key, mixed $value1, mixed $value2): bool`](method-isequal.md)
- [`getHelperInstance(string $className): object|PageComparison|PageAccess|PageTraversal|PageValues`](method-gethelperinstance.md)
- [`comparison(): PageComparison`](method-comparison.md)
- [`access(): PageAccess`](method-access.md)
- [`traversal(): PageTraversal`](method-traversal.md)
- [`values(): PageValues`](method-values.md)
- [`meta(string|bool $key = '', null|mixed $value = null): WireDataDB|string|array|int|float`](method-meta.md)
- [`__toString(): string`](method-__tostring.md)
- [`loaded()`](method-___loaded.md) (hookable)
- [`editReady(InputfieldWrapper $form)`](method-___editready.md) (hookable)
- [`saveReady(array $changes, string|false $name = false)`](method-___saveready.md) (hookable)
- [`saved(array $changes, string|false $name = false)`](method-___saved.md) (hookable)
- [`addReady()`](method-___addready.md) (hookable)
- [`added()`](method-___added.md) (hookable)
- [`moveReady(Page $oldParent, Page $newParent)`](method-___moveready.md) (hookable)
- [`moved(Page $oldParent, Page $newParent)`](method-___moved.md) (hookable)
- [`deleteReady()`](method-___deleteready.md) (hookable)
- [`deleted()`](method-___deleted.md) (hookable)
- [`cloneReady(Page $copy)`](method-___cloneready.md) (hookable)
- [`cloned(Page $copy)`](method-___cloned.md) (hookable)
- [`renameReady(string $oldName, string $newName)`](method-___renameready.md) (hookable)
- [`renamed(string $oldName, string $newName)`](method-___renamed.md) (hookable)
- [`addStatusReady(string $name, int $value)`](method-___addstatusready.md) (hookable)
- [`addedStatus(string $name, int $value)`](method-___addedstatus.md) (hookable)
- [`removeStatusReady(string $name, int $value)`](method-___removestatusready.md) (hookable)
- [`removedStatus(string $name, int $value)`](method-___removedstatus.md) (hookable)

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
