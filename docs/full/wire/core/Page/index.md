# Page

Source: `wire/core/Page.php`

ProcessWire Page

Page is the class used by all instantiated pages and it provides functionality for:

1. Providing get/set access to the Page's properties
2. Accessing the related hierarchy of pages (i.e. parents, children, sibling pages)

ProcessWire 3.x, Copyright 2025 by Ryan Cramer
https://processwire.com

Class used by all Page objects in ProcessWire.
$page
The `$page` API variable represents the current page being viewed. However, the documentation
here also applies to all Page objects that you may work with in the API. We use `$page` as the most common example
throughout the documentation, but you can substitute that with any variable name representing a Page.

@link http://processwire.com/api/ref/page/ Offical $page Documentation

@link http://processwire.com/api/selectors/ Official Selectors Documentation




Methods added by PagePermissions.module:
----------------------------------------

@method bool viewable($field = '', $checkTemplateFile = true) Returns true if the page (and optionally field) is viewable by the current user, false if not.

@method bool editable($field = '', $checkPageEditable = true) Returns true if the page (and optionally field) is editable by the current user, false if not.

@method bool publishable() Returns true if the page is publishable by the current user, false if not.

@method bool listable() Returns true if the page is listable by the current user, false if not.

@method bool deleteable() Returns true if the page is deleteable by the current user, false if not.

@method bool deletable() Alias of deleteable().

@method bool trashable($orDeleteable = false) Returns true if the page is trashable by the current user, false if not.

@method bool restorable() Returns true if page is in the trash and is capable of being restored to its original location. @since 3.0.107

@method bool addable($pageToAdd = null) Returns true if the current user can add children to the page, false if not. Optionally specify the page to be added for additional access checking.

@method bool moveable($newParent = null) Returns true if the current user can move this page. Optionally specify the new parent to check if the page is moveable to that parent.

@method bool sortable() Returns true if the current user can change the sort order of the current page (within the same parent).

@method bool cloneable($recursive = null) Can current user clone this page? Specify false for $recursive argument to ignore whether children are cloneable. @since 3.0.239

@property bool $viewable

@property bool $editable

@property bool $publishable

@property bool $deleteable

@property bool $deletable

@property bool $trashable

@property bool $addable

@property bool $moveable

@property bool $sortable

@property bool $listable

@property bool $cloneable @since 3.0.239

Methods added by PagePathHistory.module (installed by default)
--------------------------------------------------------------

@method bool addUrl($url, $language = null) Add a new URL that redirects to this page and save immediately (returns false if already taken).

@method bool removeUrl($url) Remove a URL that redirects to this page and save immediately.
Note: you can use the $page->urls() method to get URLs added by PagePathHistory.

Methods added by LanguageSupport.module (not installed by default)
-----------------------------------------------------------------

@method Page setLanguageValue($language, $field, $value) Set value for field in language (requires LanguageSupport module). $language may be ID, language name or Language object. Field should be field name (string).

@method Page setLanguageValues($field, array $values) Set value for field in one or more languages (requires LanguageSupport module). $field should be field/property name (string), $values should be array of values indexed by language name. @since 3.0.236

@method mixed getLanguageValue($language, $field) Get value for field in language (requires LanguageSupport module). $language may be ID, language name or Language object. Field should be field name (string).

@method array getLanguageValues($field, array $langs = []) Get values for field or one or more languages (requires LanguageSupport module). $field should be field/property name (string), $langs should be array of language names, or omit for all languages. Returns array of values indexed by language name. @since 3.0.236

Methods added by LanguageSupportPageNames.module (not installed by default)
---------------------------------------------------------------------------

@method string localName($language = null, $useDefaultWhenEmpty = false) Return the page name in the current user’s language, or specify $language argument (Language object, name, or ID), or TRUE to use default page name when blank (instead of 2nd argument).

@method string localPath($language = null) Return the page path in the current user's language, or specify $language argument (Language object, name, or ID).

@method string localUrl($language = null) Return the page URL in the current user's language, or specify $language argument (Language object, name, or ID).

@method string localHttpUrl($language = null) Return the page URL (including scheme and hostname) in the current user's language, or specify $language argument (Language object, name, or ID).

@method Page setLanguageStatus($language, $status = null) Set active status for language(s), can be called as `$page->setLanguageStatus('es', true);` or `$page->setLanguageStatus([ 'es' => true, 'br' => false ]);` to set multiple. @since 3.0.236

@method array|bool getLanguageStatus($language = []) Get active status for language(s). If given a $language (Language or name of language) it returns a boolean. If given multiple language names (array), or argument omitted, it returns array like `[ 'default' => true, 'fr' => false ];`. @since 3.0.236

@method Page setLanguageName($language, $name = null) Set page name for language with `$page->setLanguageName('es', 'hola');` or set multiple with `$page->setLanguageName([ 'default' => 'hello', 'es' => 'hola' ]);` @since 3.0.236

@method array|string getLanguageName($language = []) Get page name for language(s). If given a Language object, it returns a string. If given array of language names, or argument omitted, it returns an array like `[ 'default' => 'hello', 'es' => 'hola' ];`. @since 3.0.236

Methods added by PageFrontEdit.module (not always installed by default)
-----------------------------------------------------------------------

@method string|bool|mixed edit($key = null, $markup = null, $modal = null) Get front-end editable field output or get/set status.

Methods added by ProDrafts.module (if installed)
------------------------------------------------

@method ProDraft|int|string|Page|array draft($key = null, $value = null) Helper method for drafts (added by ProDrafts).

Hookable methods
----------------

@method mixed getUnknown($key) Last stop to find a property that we haven't been able to locate. Hook this method to provide a handler.

@method void loaded() Called when page is loaded into memory and is ready to use.

@method string|mixed render($options = [], $options2 = null) Render page or field.

@method string|mixed renderPage(array $options = []) Render page.

@method string|mixed renderField($fieldName, $file = '') Render field markup, optionally with file relative to templates/fields/.

@method PageArray references($selector = '', $field = '') Return pages that are pointing to this one by way of Page reference fields.

@method PageArray links($selector = '', $field = '') Return pages that link to this one contextually in Textarea/HTML fields.

@method string|mixed if($key, $yes, $no = '') If value is available for $key return or call $yes condition (with optional $no condition)

Hookable action methods called before or after a page is saved (3.0.253+)
-------------------------------------------------------------------------

@method void editReady(InputfieldWrapper $form)

@method void saveReady(array $changes, $name = false)

@method void saved(array $changes, $name = false)

@method void addReady()

@method void added()

@method void moveReady(Page $oldParent, Page $newParent)

@method void moved(Page $oldParent, Page $newParent)

@method void deleteReady(array $options)

@method void deleted(array $options)

@method void cloneReady(Page $copy)

@method void cloned(Page $copy)

@method void renameReady(string $oldName, string $newName)

@method void renamed(string $oldName, string $newName)

@method void addStatusReady($name, $value)

@method void addedStatus(string $name, int $value)

@method void removeStatusReady($name, $value)

@method void removedStatus(string $name, int $value)


Alias/alternate methods
-----------------------

@method PageArray descendants($selector = '', array $options = array()) Find descendant pages, alias of `Page::find()`, see that method for details. @since 3.0.116

@method Page|NullPage descendant($selector = '', array $options = array()) Find one descendant page, alias of `Page::findOne()`, see that method for details. @since 3.0.116

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

Methods:
Method: [__construct()](method-__construct.md)
Method: [__destruct()](method-__destruct.md)
Method: [__clone()](method-__clone.md)
Method: [set()](method-set.md)
Method: [setQuietly()](method-setquietly.md)
Method: [get()](method-get.md)
Method: [getMultiple()](method-getmultiple.md)
Method: [getField()](method-getfield.md)
Method: [getFields()](method-getfields.md)
Method: [hasField()](method-hasfield.md)
Method: [getFieldSubfieldValue()](method-getfieldsubfieldvalue.md)
Method: [preload()](method-preload.md)
Method: [getUnknown()](method-___getunknown.md) (hookable)
Method: [getFieldFirstValue()](method-getfieldfirstvalue.md)
Method: [getFieldValue()](method-getfieldvalue.md)
Method: [formatFieldValue()](method-formatfieldvalue.md)
Method: [if()](method-___if.md) (hookable)
Method: [getMarkup()](method-___getmarkup.md) (hookable)
Method: [getText()](method-gettext.md)
Method: [setUnformatted()](method-setunformatted.md)
Method: [getUnformatted()](method-getunformatted.md)
Method: [getFormatted()](method-getformatted.md)
Method: [__get()](method-__get.md)
Method: [__set()](method-__set.md)
Method: [callUnknown()](method-___callunknown.md) (hookable)
Method: [setName()](method-setname.md)
Method: [template()](method-template.md)
Method: [setUser()](method-setuser.md)
Method: [getUser()](method-getuser.md)
Method: [find()](method-find.md)
Method: [findOne()](method-findone.md)
Method: [children()](method-children.md)
Method: [numChildren()](method-numchildren.md)
Method: [hasChildren()](method-haschildren.md)
Method: [child()](method-child.md)
Method: [parent()](method-parent.md)
Method: [parents()](method-parents.md)
Method: [numParents()](method-numparents.md)
Method: [parentsUntil()](method-parentsuntil.md)
Method: [closest()](method-closest.md)
Method: [rootParent()](method-___rootparent.md) (hookable)
Method: [siblings()](method-siblings.md)
Method: [numDescendants()](method-numdescendants.md)
Method: [next()](method-next.md)
Method: [nextAll()](method-nextall.md)
Method: [nextUntil()](method-nextuntil.md)
Method: [prev()](method-prev.md)
Method: [prevAll()](method-prevall.md)
Method: [prevUntil()](method-prevuntil.md)
Method: [references()](method-___references.md) (hookable)
Method: [links()](method-___links.md) (hookable)
Method: [getLanguages()](method-getlanguages.md)
Method: [save()](method-save.md)
Method: [saveFields()](method-savefields.md)
Method: [setAndSave()](method-setandsave.md)
Method: [delete()](method-delete.md)
Method: [trash()](method-trash.md)
Method: [count()](method-count.md)
Method: [getIterator()](method-getiterator.md)
Method: [isChanged()](method-ischanged.md)
Method: [resetTrackChanges()](method-resettrackchanges.md)
Method: [path()](method-path.md)
Method: [url()](method-url.md)
Method: [urls()](method-urls.md)
Method: [httpUrl()](method-httpurl.md)
Method: [editUrl()](method-editurl.md)
Method: [sortfield()](method-sortfield.md)
Method: [index()](method-index.md)
Method: [render()](method-___render.md) (hookable)
Method: [renderPage()](method-___renderpage.md) (hookable)
Method: [renderField()](method-___renderfield.md) (hookable)
Method: [renderValue()](method-___rendervalue.md) (hookable)
Method: [getInputfields()](method-getinputfields.md)
Method: [getInputfields()](method-___getinputfields.md) (hookable)
Method: [getInputfield()](method-getinputfield.md)
Method: [edit()](method-___edit.md) (hookable)
Method: [setStatus()](method-setstatus.md)
Method: [hasStatus()](method-hasstatus.md)
Method: [addStatus()](method-addstatus.md)
Method: [removeStatus()](method-removestatus.md)
Method: [matches()](method-matches.md)
Method: [matchesDatabase()](method-matchesdatabase.md)
Method: [is()](method-is.md)
Method: [isHidden()](method-ishidden.md)
Method: [isUnpublished()](method-isunpublished.md)
Method: [isLocked()](method-islocked.md)
Method: [isTrash()](method-istrash.md)
Method: [isPublic()](method-ispublic.md)
Method: [isPublic()](method-___ispublic.md) (hookable)
Method: [status()](method-status.md)
Method: [processFieldDataQueue()](method-processfielddataqueue.md)
Method: [of()](method-of.md)
Method: [filesManager()](method-filesmanager.md)
Method: [secureFiles()](method-securefiles.md)
Method: [hasFilesPath()](method-hasfilespath.md)
Method: [hasFiles()](method-hasfiles.md)
Method: [hasFile()](method-hasfile.md)
Method: [filesPath()](method-filespath.md)
Method: [filesUrl()](method-filesurl.md)
Method: [getAccessParent()](method-getaccessparent.md)
Method: [getAccessTemplate()](method-getaccesstemplate.md)
Method: [getAccessRoles()](method-getaccessroles.md)
Method: [hasAccessRole()](method-hasaccessrole.md)
Method: [isEqual()](method-isequal.md)
Method: [getHelperInstance()](method-gethelperinstance.md)
Method: [comparison()](method-comparison.md)
Method: [access()](method-access.md)
Method: [traversal()](method-traversal.md)
Method: [values()](method-values.md)
Method: [meta()](method-meta.md)
Method: [__toString()](method-__tostring.md)
Method: [loaded()](method-___loaded.md) (hookable)
Method: [editReady()](method-___editready.md) (hookable)
Method: [saveReady()](method-___saveready.md) (hookable)
Method: [saved()](method-___saved.md) (hookable)
Method: [addReady()](method-___addready.md) (hookable)
Method: [added()](method-___added.md) (hookable)
Method: [moveReady()](method-___moveready.md) (hookable)
Method: [moved()](method-___moved.md) (hookable)
Method: [deleteReady()](method-___deleteready.md) (hookable)
Method: [deleted()](method-___deleted.md) (hookable)
Method: [cloneReady()](method-___cloneready.md) (hookable)
Method: [cloned()](method-___cloned.md) (hookable)
Method: [renameReady()](method-___renameready.md) (hookable)
Method: [renamed()](method-___renamed.md) (hookable)
Method: [addStatusReady()](method-___addstatusready.md) (hookable)
Method: [addedStatus()](method-___addedstatus.md) (hookable)
Method: [removeStatusReady()](method-___removestatusready.md) (hookable)
Method: [removedStatus()](method-___removedstatus.md) (hookable)

Constants:
Const: [statusLocked](const-statuslocked.md)
Const: [statusHidden](const-statushidden.md)
Const: [statusUnpublished](const-statusunpublished.md)
