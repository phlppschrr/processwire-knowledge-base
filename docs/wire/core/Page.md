# Page

Source: `wire/core/Page.php`

ProcessWire Page

Page is the class used by all instantiated pages and it provides functionality for:

1. Providing get/set access to the Page's properties
2. Accessing the related hierarchy of pages (i.e. parents, children, sibling pages)

ProcessWire 3.x, Copyright 2025 by Ryan Cramer
https://processwire.com

Class used by all Page objects in ProcessWire.
Multi-language methods require these core modules: `LanguageSupport`, `LanguageSupportFields`, `LanguageSupportPageNames`.
Most system properties directly correspond to columns in the `pages` database table.
Provides access to the previously set runtime value of some Page properties.
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

## common

@property PageArray $parents All the parent pages down to the root (homepage). Returns a PageArray.

## traversal

@property Page|string|int $parent The parent Page object or a NullPage if there is no parent. For assignment, you may also use the parent path (string) or id (integer).

@property Page $rootParent The parent page closest to the homepage (typically used for identifying a section)

@property int $numChildren The number of children (subpages) this page has, with no exclusions (fast).

@property int $hasChildren The number of visible children this page has. Excludes unpublished, no-access, hidden, etc.

@property int $numDescendants Number of descendants (quantity of children, and their children, and so on). @since 3.0.116

@property int $numParents Number of parent pages (i.e. depth) @since 3.0.117

@property PageArray $children All the children of this page. Returns a PageArray. See also $page->children($selector).

@property Page|NullPage $child The first child of this page. Returns a Page. See also $page->child($selector).

@property PageArray $siblings All the sibling pages of this page. Returns a PageArray. See also $page->siblings($selector).

@property Page $next This page's next sibling page, or NullPage if it is the last sibling. See also $page->next($pageArray).

@property Page $prev This page's previous sibling page, or NullPage if it is the first sibling. See also $page->prev($pageArray).

@property int $index Index of this page relative to its siblings, regardless of sort (starting from 0).

@property PageArray $references Return pages that are referencing the given one by way of Page references.

@property int $numReferences Total number of pages referencing this page with Page reference fields.

@property int $hasReferences Number of visible pages (to current user) referencing this page with page reference fields.

@property PageArray $referencing Return pages that this page is referencing by way of Page reference fields.

@property int $numReferencing Total number of other pages this page is pointing to (referencing) with Page fields.

@property PageArray $links Return pages that link to this one contextually in Textarea/HTML fields.

@property int $numLinks Total number of pages manually linking to this page in Textarea/HTML fields.

@property int $hasLinks Number of visible pages (to current user) linking to this page in Textarea/HTML fields.

## date-time

@property int $created Unix timestamp of when the page was created.

@property string $createdStr Date/time when the page was created (formatted date/time string).

@property int $modified Unix timestamp of when the page was last modified.

@property string $modifiedStr Date/time when the page was last modified (formatted date/time string).

@property int $published Unix timestamp of when the page was published.

@property string $publishedStr Date/time when the page was published (formatted date/time string).

## status

@property int|null $statusPrevious Previous status, if status was changed. Null if not.

@property string statusStr Returns space-separated string of status names active on this page.

## system

@property int $id The numbered ID of the current page

@property string $name The name assigned to the page, as it appears in the URL

@property int $parent_id The numbered ID of the parent page or 0 if homepage or not assigned.

@property int $templates_id The numbered ID of the template usedby this page.

@property int $created_users_id ID of created user.

@property int $modified_users_id ID of last modified user.

@property int $sort Sort order of this page relative to siblings (applicable when manual sorting is used).

@property int|null $sortPrevious Previous sort order, if changed (3.0.235+)

@property string $sortfield Field that a page is sorted by relative to its siblings (default="sort", which means drag/drop manual)

@property int $status Page status flags.

## files

@property PagefilesManager $filesManager The object instance that manages files for this page.

@property string $filesPath Get the disk path to store files for this page, creating it if it does not exist.

@property string $filesUrl Get the URL to store files for this page, creating it if it does not exist.

@property bool $hasFiles Does this page have one or more files in its files path?

## other

@property string $title The page’s title (headline) text

@property string $path The page’s URL path from the homepage (i.e. /about/staff/ryan/)

@property string $url The page’s URL path from the server's document root

@property string $httpUrl Same as $page->url, except includes scheme (http or https) and hostname.

@property Template|string $template The Template object this page is using. The template name (string) may also be used for assignment.

@property Fieldgroup $fields All the Fields assigned to this page (via its template). Returns a Fieldgroup.

@property bool $outputFormatting Whether output formatting is enabled or not. Same as calling $page->of() with no arguments.

@property Fieldgroup $fieldgroup Fieldgroup used by page template. Shorter alias for $page->template->fieldgroup (same as $page->fields)

@property PageRender $render May be used for field markup rendering like $page->render->title.

## previous

@property string|null $namePrevious Previous name, if changed. Null or blank string if not.

@property Page|null $parentPrevious Previous parent, if parent was changed. Null if not.

@property Template|null $templatePrevious Previous template, if template was changed. Null if not.

## urls

@property array $urls All URLs the page is accessible from, whether current, former and multi-language.

@property string $editUrl URL that this page can be edited at.

## users

@property User|NullPage $createdUser The user that created this page. Returns a User or a NullPage.

@property User|NullPage $modifiedUser The user that last modified this page. Returns a User or a NullPage.

## statusLocked

Indicates page is locked for changes (name: "locked")

## statusHidden

Page is hidden and excluded from page finding methods unless overridden by selector (name: "hidden").

## statusUnpublished

Page is unpublished (not publicly visible) and excluded from page finding methods unless overridden (name: "unpublished").

## __construct()

Create a new page in memory.

@param Template|null $tpl Template object this page should use.

## __destruct()

Destruct this page instance

## __clone()

Clone this page instance

## set()

Set the value of a page property

You can set properties to a page using either `$page->set('property', $value);` or `$page->property = $value;`.

~~~~~
// Set the page title using set() method
$page->set('title', 'About Us');

// Set the page title directly (equivalent to the above)
$page->title = 'About Us';
~~~~~


@param string $key Name of property to set

@param mixed $value Value to set

@return Page|WireData Reference to this Page

@see __set

@throws WireException

## setQuietly()

Quietly set the value of a page property.

Set a value to a page without tracking changes and without exceptions.
Otherwise same as set().


@param string $key

@param mixed $value

@return $this

## get()

Get the value of a Page property (see details for several options)

This method can accept a simple property name, and also much more:

- You can retrieve a value using either `$page->get('property');` or `$page->property`.
- Get the first populated property by specifying multiple properties separated by a pipe, i.e. `headline|title`.
- Get multiple properties in a string by specifying a string `{property}` tags, i.e. `{title}: {summary}`.
- Specify a selector string to get the first matching child page, i.e. `created>=today`.
- This method can also retrieve sub-properties of object properties, i.e. `parent.title`.
- To get a guaranteed iterable value, append `[]` to the key, i.e. `$page->get('name[]')`. 3.0.205+

~~~~~
// retrieve the title using get…
$title = $page->get('title');

// …or retrieve using direct access
$title = $page->title;

// retrieve headline if populated, otherwise title
$headline = $page->get('headline|title');

// retrieve title, created date, and summary, formatted in a string
$str = $page->get('{createdStr}: {title} - {summary}');

// example of getting a sub-property: title of parent page
$title = $page->get('parent.title');

// all following features are supported in 3.0.205+

// get value guaranteed to be iterable (array, WireArray, or derived)
$images = $page->get('image[]');
$categories = $page->get('category[]');

// get item by position/index, returns 1 item whether field is single or multi value
$file = $page->get('files[0]'); // get first file  (or null if files is empty)
$file = $page->get('files.first); // same as above
$file = $page->get('files.last'); // get last file
$file = $page->get('files[1]'); // get 2nd file (or null if there isn't one)

// get titles from Page reference field categories in an array
$titles = $page->get('categories.title');  // array of titles
$title = $page->get('categories[0].title'); // string of just first title

// you can also use a selector in [brackets] for a filtered value
// example: get categories with titles matching text 'design'
$categories = $page->get('categories[title%=design]'); // PageArray
$category = $page->get('categories[title%=design][0]'); // Page or null
$titles = $page->get('categories[title%=design].title'); // array of strings
$title = $page->get('categories[title%=design].title[0]'); // string or null
~~~~~

@param string $key Name of property, format string or selector, per the details above.

@return mixed Value of found property, or NULL if not found.

@see __get()

## getMultiple()

Get multiple Page property/field values in an array

This method works exactly the same as the `get()` method except that it accepts an
array (or CSV string) of properties/fields to get, and likewise returns an array
of those property/field values. By default it returns a regular (non-indexed) PHP
array in the same order given. To instead get an associative array indexed by the
property/field names given, specify `true` for the `$assoc` argument.

~~~~~
// returns regular array i.e. [ 'foo val', 'bar val' ]
$a = $page->getMultiple([ 'foo', 'bar' ]);
list($foo, $bar) = $a;

// returns associative array i.e. [ 'foo' => 'foo val', 'bar' => 'bar val' ]
$a = $page->getMultiple([ 'foo', 'bar' ], true);
$foo = $a['foo'];
$bar = $a['bar'];

// CSV string can also be used instead of array
$a = $page->getMultiple('foo,bar');
~~~~~

@param array|string $keys Array or CSV string of properties to get.

@param bool $assoc Get associative array indexed by given properties? (default=false)

@return array

@since 3.0.201

## getField()

Get a Field object in context or NULL if not valid for this page

Field in context is only returned when output formatting is on.


@param string|int|Field $field

@return Field|null

@todo determine if we can always retrieve in context regardless of output formatting.

## getFields()

Returns a FieldsArray of all Field objects in the context of this Page

Unlike $page->fieldgroup (or its alias $page->fields), the fields returned from
this method are in the context of this page/template. Meaning returned Field
objects may have some properties that are different from the Field outside of
the context of this page.


@return FieldsArray of Field objects

## hasField()

Returns whether or not given $field name, ID or object is valid for this Page

Note that this only indicates validity, not whether the field is populated.


@param int|string|Field|array $field Field name, object or ID to check.
 - In 3.0.126+ this may also be an array or pipe "|" separated string of field names to check.

@return bool|string True if valid, false if not.
 - In 3.0.126+ returns first matching field name if given an array of field names or pipe separated string of field names.

## getFieldSubfieldValue()

If given a field.subfield string, returns the associated value

This is like the getDot() method, but with additional protection during output formatting.

@param $key

@return mixed|null

@deprecated Method no longer needed

## preload()

Preload multiple fields together as a group (experimental)

This is an optimization that enables you to load the values for multiple fields into
a page at once, and often in a single query. For fields where it is supported, and
for cases where you have a lot of fields to load at once, it can be up to 50% faster
than the default of lazy-loading fields.

To use, call `$page->preload([ 'field1', 'field2', 'etc.' ])` before accessing
`$page->field1`, `$page->field2`, etc.

The more fields you give this method, the more performance improvement it can offer.
As a result, don't bother if with only a few fields, as it's less likely to make
a difference at small scale. You will also see a more measurable benefit if preloading
fields for lots of pages at once.

Preload works with some Fieldtypes and not others. For details on what it is doing,
specify `true` for the `debug` option which will make it return array of what it
loaded and what it didn't. Have a look at this array with TracyDebugger or output
a print_r() call on it, and the result is self explanatory.

NOTE: This function is currently experimental, recommended for testing only.

~~~~~
// Example usage
$page->preload([ 'headline', 'body', 'sidebar', 'intro', 'summary' ]);
echo "
  <h1 id='headline'>$page->headline</h1>";
  <div id='intro'>$page->intro</div>
  <div id='body'>$page->body</div>
  <aside id='sidebar' pw-append>$page->sidebar</aside>
  <meta id='meta-description'>$page->summary</meta>
";
~~~~~

@param array $fieldNames Names of fields to preload or omit (or blank array)
  to preload all supported fields.

@param array $options Options to modify default behavior:
- `debug` (bool): Specify true to return additional info in returned array (default=false).
- See the `PagesLoader::preloadFields()` method for additional options.

@return array Array of details

@since 3.0.243

## ___getUnknown()

Hookable method called when a request to a field was made that didn't match anything

Hooks that want to inject something here should hook after and modify the $event->return.


@param string $key Name of property.

@return null|mixed Returns null if property not known, or a value if it is.

## getFieldFirstValue()

Given a Multi Key, determine if there are multiple keys requested and return the first non-empty value

A Multi Key is a string with multiple field names split by pipes, i.e. headline|title

Example: browser_title|headline|title - Return the value of the first field that is non-empty

@param string $multiKey

@param bool $getKey Specify true to get the first matching key (name) rather than value

@return null|mixed Returns null if no values match, or if there aren't multiple keys split by "|" chars

@deprecated Use $page->values()->getFieldFirstValue() instead

## getFieldValue()

Get the value for a non-native page field, and call upon Fieldtype to join it if not autojoined

@param string $key Name of field to get

@param string $selector Optional selector to filter load by...
  ...or, if not in selector format, it becomes an __invoke() argument for object values .

@return null|mixed

## formatFieldValue()

Return a value consistent with the page’s output formatting state

This is primarily for use as a helper to the getFieldValue() method.

@param Field $field

@param mixed $value

@return mixed

## ___if()

If value is available for $key return or call $yes condition (with optional $no condition)

This merges the capabilities of an if() statement, get() and getMarkup() methods in one,
plus some useful PW type-specific logic, providing a useful output shortcut. It many situations
it enables you to accomplish on one-line of code what might have otherwise taken multiple lines
of code. Use this when looking for a useful shortcut and this one fits your need, otherwise
use a regular PHP if() statement.

This function is primarily intended for conditionally outputting some formatted string value or
markup, however its use is not limited to that, as you can specify whatever you’d like for the
$yes and $no conditions. The examples section best describes potential usages of this method,
so I recommend looking at those before reading all the details of this method.

Note that the logic is a little bit smarter for PW than a regular PHP if() statement in these ways:

- If value resolves to any kind of *empty* `WireArray` (like a `PageArray`) the NO condition is used.
  If the WireArray is populated with at least one item then the YES condition is used. So this if()
  method (unlike PHP if) requires that not only is the value present, but it is also populated.

- If value resolves to a `NullPage` the NO condition is used.

The `$key` argument may be any of the following:

- A field name, in which case we will use the value of that field on this page. If the value is
  empty the NO condition will be used, otherwise the YES condition will be used. You can use any
  format for the field name that the `Page::get()` method accepts, so subfields and OR field
  statements are also okay, i.e. `categories.count`, `field1|field2|field3', etc.

- A selector string that must match this page in order to return the YES condition. If it does not
  match then the NO condition will be used.

- A boolean, integer, digit string or PHP array. If considered empty by PHP it will return the NO
  condition, otherwise it will return the YES condition.

The `$yes` and `$no` arguments (the conditional actions) may be any of the following:

- Any string value that you’d like (HTML markup is fine too).

- A field name that is present on this page, or optionally the word “value” to refer to the field
  specified in the `$key` argument. Either way, makes this method return the actual field value as it
  exists on the page, rather than a string/markup version of it. Note that if this word (“value”) is
  used for the argument then of course the `$key` argument must be a field name (not a selector string).

- Any callable inline function that returns the value you want this function to return.

- A string containing one or more `{field}` placeholders, where you replace “field” with a field name.
  These are in turn populated by the `Page::getMarkup()` method. You can also use `{field.subfield}`
  and `{field1|field2|field3}` type placeholder strings.

- A string containing `{val}` or `{value}` where they will be replaced with the markup value of the
  field name given in the $key argument.

- If you omit the `$no` argument an empty string is assumed.

- If you omit both the `$yes` and `$no` arguments, then boolean is assumed (true for yes, false for no),
  which makes this method likewise return a boolean. The only real reason to do this would be to take
  advantage of the method’s slightly different behavior than regular PHP if() statements (i.e. treating
  empty WireArray or NullPage objects as false conditions).

~~~~~
// if summary is populated, output it in an paragraph
echo $page->if("summary", "<p class='summary'>{summary}</p>");

// same as above, but shows you can specify {value} to assume field in $key arg
echo $page->if("summary", "<p class='summary'>{value}</p>");

// if price is populated, format for output, otherwise ask them to call for price
echo $page->if("price", function($val) { return '$' . number_format($val); }, "Please call");

// you can also use selector strings
echo $page->if("inventory>10", "In stock", "Limited availability");

// output an <img> tag for the first image on the page, or blank if none
echo $page->if("images", function($val) { return "<img src='{$val->first->url}'>"; });
~~~~~

@param string|bool|int $key Name of field to check, selector string to evaluate, or boolean/int to evalute

@param string|callable|mixed $yes If value for $key is present, return or call this

@param string|callable|mixed $no If value for $key is empty, return or call this

@return mixed|string|bool

@since 3.0.126

## ___getMarkup()

Return the markup value for a given field name or {tag} string

1. If given a field name (or `name.subname` or `name1|name2|name3`) it will return the
   markup value as defined by the fieldtype.
2. If given a string with field names referenced in `{tags}`, it will populate those
   tags and return the populated string.


@param string $key Field name or markup string with field {name} tags in it

@return string

@see Page::getText()

## getText()

Same as getMarkup() except returned value is plain text

If no `$entities` argument is provided, returned value is entity encoded when output formatting
is on, and not entity encoded when output formatting is off.


@param string $key Field name or string with field {name} tags in it.

@param bool $oneLine Specify true if returned value must be on single line.

@param bool|null $entities True to entity encode, false to not. Null for auto, which follows page's outputFormatting state.

@return string

@see Page::getMarkup()

## setUnformatted()

Set the unformatted value of a field, regardless of current output formatting state

Use this when setting an unformatted value to a page that has (or might have) output formatting enabled.
This will save you the steps of checking the output formatting state, turning it off, setting the value,
and turning it back on again (if it was on). Note that the output formatting distinction matters for some
field types and not others, just depending on the case—this method is safe to use either way.

Make sure you do not use this to set an already formatted value to a Page (like some text that has been
entity encoded). This method skips over some of the checks that might otherwise flag the page as corrupted.

~~~~~
// good usage
$page->setUnformatted('title', 'This & That');

// bad usage
$page->setUnformatted('title', 'This &amp; That');
~~~~~


@param string $key

@param mixed $value

@return self

@since 3.0.169

@throws WireException if given an object value that indicates it is already formatted.

@see Page::getUnformatted(), Page::of(), Page::setOutputFormatting(), Page::outputFormatting()

## getUnformatted()

Get the unformatted value of a field, regardless of current output formatting state

When a page’s output formatting state is off, `$page->get('property')` or `$page->property` will
produce the same result as this method call.

~~~~~
// Get the 'body' field without any text formatters applied
$body = $page->getUnformatted('body');
~~~~~


@param string $key Field or property name to retrieve

@return mixed

@see Page::getFormatted(), Page::of(), Page::setOutputFormatting(), Page::outputFormatting()

## getFormatted()

Get the formatted value of a field, regardless of output formatting state

When a page's output formatting state is on, `$page->get('property')` or `$page->property` will
produce the same result as this method call.

~~~~~
// Get the formatted 'body' field (text formatters applied)
$body = $page->getFormatted('body');
~~~~~


@param string $key Field or property name to retrieve

@return mixed

@see Page::getUnformatted(), Page::of()

## __get()

Direct access get method

@param string $key

@return mixed

@see get()

## __set()

Direct access set method

@param string $key

@param mixed $value

@see set()

## ___callUnknown()

If method call resulted in no handler, this hookable method is called.

If you want to override this method with a hook, see the example below.
~~~~~
$wire->addHookBefore('Wire::callUnknown', function(HookEvent $event) {
  // Get information about unknown method that was called
  $methodObject = $event->object;
  $methodName = $event->arguments(0); // string
  $methodArgs = $event->arguments(1); // array
  // The replace option replaces the method and blocks the exception
  $event->replace = true;
  // Now do something with the information you have, for example
  // you might want to populate a value to $event->return if
  // you want the unknown method to return a value.
});
~~~~~


@param string $method Requested method name

@param array $arguments Arguments provided

@return null|mixed Return value of method (if applicable)

@throws WireException

@see Wire::callUnknown()

## setName()

Set the page name, optionally for specific language

~~~~~
// Set page name (default language)
$page->setName('my-page-name');

// This is equivalent to the above
$page->name = 'my-page-name';

// Set page name for Spanish language
$page->setName('la-cerveza', 'es');
~~~~~


@param string $value Page name that you want to set

@param Language|string|int|null $language Set language for name (can also be language name or string in format "name1234")

@return $this

## template()

Get or set template

@param null|Template|string|int $template

@return Template|null

@since 3.0.181

## setUser()

Set either the createdUser or the modifiedUser

@param User|int|string $user User object or integer/string representation of User

@param string $userType Must be either 'created' or 'modified'

@return $this

@throws WireException

## getUser()

Get page’s created or modified user

@param string $userType One of 'created' or 'modified'

@return User|NullPage

## find()

Find descendant pages matching given selector

This is the same as `Pages::find()` except that the results are limited to descendents of this Page.

~~~~~
// Find all unpublished pages underneath the current page
$items = $page->find("status=unpublished");
~~~~~


@param string|array $selector Selector string or array

@param array $options Same as the $options array passed to $pages->find().

@return PageArray

@see Pages::find()

## findOne()

Find one descendant page matching given selector

This is the same as `Pages::findOne()` except that the match is always a descendant of page it is called on.

~~~~~
// Find the most recently modified descendant page
$item = $page->findOne("sort=-modified");
~~~~~


@param string|array $selector Selector string or array

@param array $options Optional options to modify default bheavior, see options for `Pages::find()`.

@return Page|NullPage Returns Page when found, or NullPage when nothing found.

@see Pages::findOne(), Page::child()

@since 3.0.116

## children()

Return this page’s children, optionally filtered by a selector

By default, hidden, unpublished and no-access pages are excluded unless `include=x` (where "x" is desired status) is specified.
If a selector isn't needed, children can also be accessed directly by property with `$page->children`.

~~~~~
// Render navigation for all child pages below this one
foreach($page->children() as $child) {
  echo "<li><a href='$child->url'>$child->title</a></li>";
}
~~~~~
~~~~~
// Retrieve just the 3 newest children
$newest = $page->children("limit=3, sort=-created");
~~~~~


@param string $selector Selector to use, or omit to return all children.

@param array $options Optional options to modify behavior, the same as those provided to Pages::find.

@return PageArray|array Returns PageArray for most cases. Returns regular PHP array if using the findIDs option.

@see Page::child(), Page::find(), Page::numChildren(), Page::hasChildren()

## numChildren()

Return number of all children, optionally with conditions

Use this over the `$page->numChildren` property when you want to specify a selector, or when you want the result to
include only visible children. See the options for the $selector argument.

When you want to retrieve all children with no exclusions or conditions, use the `$page->numChildren` property instead.

~~~~~
// Find how many children were modified in the last week
$qty = $page->numChildren("modified>='-1 WEEK'");
~~~~~


@param bool|string|array $selector
- When not specified, result includes all children without conditions, same as $page->numChildren property.
- When a string or array, a selector is assumed and quantity will be counted based on selector.
- When boolean true, number includes only visible children (excludes unpublished, hidden, no-access, etc.)
- When boolean false, number includes all children without conditions, including unpublished, hidden, no-access, etc.
- When integer 1 number includes “viewable” children (as opposed to “visible” children, viewable children includes
  hidden pages and also includes unpublished pages if user has page-edit permission).

@return int Number of children

@see Page::hasChildren(), Page::children(), Page::child()

## hasChildren()

Return the number of visible children, optionally with conditions

This method is similar to `$page->numChildren()` except that the default behavior is to exclude non-visible children.

This method may be more convenient for front-end navigation use than the `$page->numChildren()` method because
it only includes the count of visible children. By visible, we mean children that are not hidden, unpublished,
or non-accessible due to access control.

~~~~~
// Determine if we should show navigation to children
if($page->hasChildren()) {
  // Yes, we should show navigation to children
}
~~~~~


@param bool|string|array $selector
- When not specified, result is quantity of visible children (excludes unpublished, hidden, no-access, etc.)
- When a string or array, a selector is assumed and quantity will be counted based on selector.
- When boolean true, number includes only visible children (this is the default behavior, so no need to specify this value).
- When boolean false, number includes all children without conditions, including unpublished, hidden, no-access, etc.

@return int Number of children

## child()

Return the page’s first single child that matches the given selector.

Same as `$page->children()` but returns a single Page object or NullPage (with id=0) rather than a PageArray.
Meaning, this method will only ever return one Page.

~~~~~
// Get the newest created child page
$newestChild = $page->child("sort=-created");
~~~~~


@param string|array|int $selector Selector to use, or blank to return the first child.

@param array $options Optional options per Pages::find

@return Page|NullPage

@see Page::children()

## parent()

Return this page’s parent Page, or–if given a selector–the closest matching parent.

Omit all arguments if you just want to retrieve the parent of this page, which would be the same as the
`$page->parent` property. To retrieve the closest parent matching your selector, specify either a selector
string or array.

~~~~~
// Retrieve the parent
$parent = $page->parent();

// Retrieve the closest parent using template "products"
$parent = $page->parent("template=products");
~~~~~


@param string|array $selector Optional selector. When used, it returns the closest parent matching the selector.

@return Page Returns a Page or a NullPage when there is no parent or the selector string did not match any parents.

## parents()

Return this page’s parent pages, or the parent pages matching the given selector.

This method returns all parents of this page, in order. If a selector is specified, they
will be filtered by the selector. By default, parents are returned in breadcrumb order.
In 3.0.158+ if you specify boolean true for selector argument, then it will return parents
in reverse order (closest to furthest).

~~~~~
// Render breadcrumbs
foreach($page->parents() as $parent) {
  echo "<li><a href='$parent->url'>$parent->title</a></li>";
}
~~~~~
~~~~~
// Return all parents, excluding the homepage
$parents = $page->parents("template!=home");
~~~~~
~~~~~
// Return parents in reverse order (closest to furthest, 3.0.158+)
$parents = $page->parents(true);
~~~~~


@param string|array|bool $selector Optional selector string to filter parents by or boolean true for reverse order

@return PageArray All parent pages, or those matching the given selector.

## numParents()

Return number of parents (depth relative to homepage) that this page has, optionally filtered by a selector

For example, homepage has 0 parents and root level pages have 1 parent (which is the homepage), and the
number increases the deeper the page is in the pages structure.

@param string $selector Optional selector to filter by (default='')

@return int Number of parents

## parentsUntil()

Return all parents from current page till the one matched by $selector

This duplicates the jQuery parentsUntil() function in ProcessWire.


@param string|Page|array $selector May either be a selector sor Page to stop at. Results will not include this.

@param string|array $filter Optional selector to filter matched pages by

@return PageArray

## closest()

Find the closest parent page matching your selector

This is like `$page->parent()` but includes the current Page in the possible pages that can be matched,
and the $selector argument is required.


@param string|array $selector Selector string to match.

@return Page|NullPage $selector Returns the current Page or closest parent matching the selector. Returns NullPage when no match.

## ___rootParent()

Get the lowest-level, non-homepage parent of this page

The rootParents typically comprise the first level of navigation on a site, and in many cases are considered
the "section" pages of the site.

~~~~~
// Determine if we are in the "products" section of the site
if($page->rootParent()->template == 'products') {
  // we are in the products section
} else {
  // we are in some other section of the site
}
~~~~~


@return Page

## siblings()

Return this Page’s sibling pages, optionally filtered by a selector.

To exclude the current page in list of siblings, specify boolean false for first or second argument.

~~~~~
// Get all sibling pages
$siblings = $page->siblings();

// Get all sibling pages, and exclude current page from the returned value
$siblings = $page->siblings(false);

// Get all siblings having the "product-featured" template, sorted by name
$featured = $page->siblings("template=product-featured, sort=name");

// Same as above, while excluding current page
$featured = $page->siblings("template=product-featured, sort=name", false);
~~~~~


@param string|array|bool $selector Optional selector to filter siblings by, or omit for all siblings.

@param bool $includeCurrent Specify false to exclude current page in the returned siblings (default=true).
  If no $selector argument is given, this argument may optionally be specified as the first argument.

@return PageArray

## numDescendants()

Return number of descendants (children, grandchildren, great-grandchildren, …), optionally with conditions

Use this over the `$page->numDescendants` property when you want to specify a selector or apply
some other filter to the result (see options for `$selector` argument). If you want to include only
visible descendants specify a selector (string or array) or boolean true for the `$selector` argument,
if you don’t need a selector.

If you want to find descendant pages (rather than count), use the `Page::find()` method.

~~~~~
// Find how many descendants were modified in the last week
$qty = $page->numDescendants("modified>='-1 WEEK'");
~~~~~


@param bool|string|array $selector
- When not specified, result includes all descendants without conditions, same as $page->numDescendants property.
- When a string or array, a selector is assumed and quantity will be counted based on selector.
- When boolean true, number includes only visible descendants (excludes unpublished, hidden, no-access, etc.)

@return int Number of descendants

@see Page::numChildren(), Page::find()

## next()

Return the next sibling page

By default, hidden, unpublished and non-viewable pages are excluded. If you want them included,
be sure to specify `include=` with hidden, unpublished or all, in your selector.

~~~~~
// Get the next sibling
$sibling = $page->next();

// Get the next newest sibling
$sibling = $page->next("created>$page->created");

// Get the next sibling, even if it isn't viewable
$sibling = $page->next("include=all");
~~~~~


@param string|array $selector Optional selector. When specified, will find nearest next sibling that matches.

@param PageArray $siblings Optional siblings to use instead of the default. Avoid using this argument
  as it forces this method to use the older/slower functions.

@return Page|NullPage Returns the next sibling page, or a NullPage if none found.

## nextAll()

Return all sibling pages after this one, optionally matching a selector


@param string|array|bool $selector Optional selector. When specified, will filter the found siblings.

@param bool|PageArray $getQty Return a count instead of PageArray? (boolean)
  - If no $selector argument is needed, this may be specified as the first argument.
  - Legacy support: You may specify a PageArray of siblings to use instead of the default (deprecated, avoid it).

@param bool $getPrev For internal use, makes this method implement the prevAll() behavior instead.

@return PageArray|int Returns all matching pages after this one, or integer if $count option specified.

## nextUntil()

Return all sibling pages after this one until matching the one specified


@param string|Page|array $selector May either be a selector or Page to stop at. Results will not include this.

@param string|array $filter Optional selector to filter matched pages by

@param PageArray $siblings Optional PageArray of siblings to use instead (avoid).

@return PageArray

## prev()

Return the previous sibling page

~~~~~
// Get the previous sibling
$sibling = $page->prev();

// Get the previous sibling having field "featured" with value of "1"
$sibling = $page->prev("featured=1");
~~~~~


@param string|array $selector Optional selector. When specified, will find nearest previous sibling that matches.

@param PageArray|null $siblings Optional siblings to use instead of the default.

@return Page|NullPage Returns the previous sibling page, or a NullPage if none found.

## prevAll()

Return all sibling pages before this one, optionally matching a selector


@param string|array|bool $selector Optional selector. When specified, will filter the found siblings.

@param bool|PageArray $getQty Return a count instead of PageArray? (boolean)
  - If no $selector argument is needed, this may be specified as the first argument.
  - Legacy support: You may specify a PageArray of siblings to use instead of the default (deprecated, avoid it).

@return Page|NullPage|int Returns all matching pages before this one, or integer if $getQty requested.

## prevUntil()

Return all sibling pages before this one until matching the one specified


@param string|Page|array $selector May either be a selector or Page to stop at. Results will not include this.

@param string|array $filter Optional selector to filter matched pages by

@param PageArray|null $siblings Optional PageArray of siblings to use instead of default.

@return PageArray

## ___references()

Return pages that have Page reference fields pointing to this one (references)

By default this excludes pages that are hidden, unpublished and pages excluded due to access control for the current user.
To prevent these exclusions specify an include mode in the selector, i.e. `include=all`, or you can use
boolean `true` as a shortcut to specify that you do not want any exclusions.


@param string|bool $selector Optional selector to filter results by, or boolean true as shortcut for `include=all`.

@param Field|string|bool $field Optionally limit to pages using specified field (name or Field object),
 - OR specify boolean TRUE to return array of PageArrays indexed by field names.
 - If $field argument not specified, it searches all applicable Page fields.

@return PageArray|array

@since 3.0.107

## ___links()

Return pages linking to this one (in Textarea/HTML fields)

Applies only to Textarea fields with “html” content-type and link abstraction enabled.


@param string|bool $selector Optional selector to filter by or boolean true for “include=all”. (default='')

@param string|Field $field Optionally limit results to specified field. (default=all applicable Textarea fields)

@return PageArray

@since 3.0.107

## getLanguages()

Get languages active for this page and viewable by current user


@return PageArray|null Returns PageArray of languages, or null if language support is not active.

## save()

Save the entire page to the database, or just a field from it

This is the same as calling `$pages->save($page);` or `$pages->saveField($page, $field)`, but calling directly
on the $page like this may be more convenient in many instances.

If you want to hook into the save operation, hook into one of the many Pages class hooks referenced in the 'See Also' section.

~~~~~
// Save the page
$page->save();

// Save just the 'title' field from the page
$page->save('title');
~~~~~


@param Field|string $field Optional field to save (name of field or Field object)

@param array $options See Pages::save() documentation for options. You may also specify $options as the first argument if no $field is needed.

@return bool Returns true on success false on fail

@throws WireException on database error

@see Pages::save(), Page::saveFields(), Pages::saveField(), Pages::saveReady(), Pages::saveFieldReady(), Pages::saved(), Pages::fieldSaved()

## saveFields()

Save only the given named fields for this page

@param array|string $fields Array of field name(s) or string (CSV or space separated)

@param array $options See Pages::save() documentation for options.

@return array Names of fields that were saved

@throws WireException on database error

@see Page::save()

@since 3.0.242

## setAndSave()

Quickly set field value(s) and save to database

You can specify a single field and value, or an array of fields and values.

This method does not need output formatting to be turned off first, so make sure that whatever
value(s) you set are not formatted values.

~~~~~
// Set and save the summary field
$page->setAndSave('summary', 'When nothing is done, nothing is left undone.');
~~~~~
~~~~~
// Set and save multiple fields
$page->setAndSave([
  'title' => 'It is Friday again',
  'subtitle' => 'Here is another new blog post',
  'body' => 'Hope you all have a great weekend!'
]);
~~~~~
~~~~~
// Update a 'last_login' field after every user login
$session->addHookAfter('loginSuccess', function($event) {
  $user = $event->arguments(0);
  $user->setAndSave('last_login', time());
});
~~~~~

[Blog post about setAndSave](https://processwire.com/blog/posts/processwire-2.6.9-core-updates-and-new-procache-version/)

@param array|string $key Field or property name to set, or array of one or more ['property' => $value].

@param string|int|bool|object $value Value to set, or omit if you provided an array in first argument.

@param array $options See Pages::save() for additional $options that may be specified.

@return bool Returns true on success, false on failure

@see Pages::save()

## delete()

Delete this page from the database

This is the same as calling `$pages->delete($page)`.

~~~~~
// Delete pages named "delete-me" that don't have children
$items = $pages->find("name=delete-me, numChildren=0");
foreach($items as $item) {
  $item->delete();
}
~~~~~
~~~~~
// Delete a page and recursively all of its children, grandchildren, etc.
$item = $pages->get('/some-page/');
$item->delete(true);
~~~~~


@param bool $recursive If set to true, then this will attempt to delete all children too.

@return bool|int True on success, false on failure, or int quantity of pages deleted when recursive option is true.

@throws WireException when attempting to delete a page with children and $recursive option is not specified.

@see Pages::delete()

## trash()

Move this page to the trash

This is the same as calling `$pages->trash($page)`.

~~~~~
// Trash a page
$item = $pages->get('/some-page/');
$item->trash();
~~~~~


@return bool True on success, false on failure

@throws WireException

## count()

Returns number of children page has, affected by output formatting mode.

- When output formatting is on, returns only number of visible children,
  making the return value the same as the `Page::hasChildren()` method.

- When output formatting is off, returns number of all children without exclusion,
  making the return value the same as the `Page::numChildren()` method.

~~~~~
// Get number of visible children, like $page->hasChildren()
$page->of(true); // enable output formatting
$numVisible = $page->count();

// Get number of all children, like $page->numChildren()
$page->of(false); // disable output formatting
$numTotal = $page->count();
~~~~~


@return int Quantity of children

@see Page::hasChildren(), Page::numChildren()

## getIterator()

Enables iteration of the page's properties and fields with PHP’s foreach()

This fulfills PHP's IteratorAggregate interface, enabling you to interate all of the page's properties and fields.

~~~~~
// List all properties and fields from the page
foreach($page as $name => $value) {
  echo "<h3>$name</h3>";
  echo "<p>$value</p>";
}
~~~~~


@return \ArrayObject

## isChanged()

Has the Page changed since it was loaded?

To check if only a specific property on the page has changed, specify the property/field name as the first argument.
This method assumes that change tracking is enabled for the Page (as it is by default).
Pages that are new (i.e. don't yet exist in the database) always return true.


~~~~~
// Check if page has any changes
if($page->isChanged()) {
  // There are changes to this page
  $changes = $page->getChanges();
}
~~~~~
~~~~~
// When page is about to be saved, update summary when body has changed
$this->addHookBefore('Pages::saveReady', function($event) {
  $page = $event->arguments('page');
  if($page->isChanged('body')) {
    // get first 300 chars from body
    $summary = substr($page->body, 0, 300);
    // truncate to position of last period
    $period = strrpos($summary, '.');
    if($period) $summary = substr($summary, 0, $period);
    // populate to the page, so that summary is also saved
    $page->summary = $summary;
  }
});
~~~~~

@param string $what If specified, only checks the given property for changes rather than the whole page.

@return bool

@see Wire::setTrackChanges(), Wire::getChanges(), Wire::trackChange()

## resetTrackChanges()

Clears out any tracked changes and turns change tracking ON or OFF

Use this method when you want to clear a list of tracked changes on the page. Note that any changes are still
present, but ProcessWire no longer knows they had been changed. Meaning, the changes won't be available to
the `$page->isChanged()` and `$page->getChanges()` methods, and the changes might be skipped over if/when
the page is saved.


@param bool $trackChanges True to turn change tracking ON, or false to turn OFF. Default of true is assumed.

@return $this

@see Page::isChanged(), Page::getChanges(), Page::trackChanges()

## path()

Returns the Page’s path from the ProcessWire installation root.

The path is always indicated from the ProcessWire installation root. Meaning, if the installation is
running from a subdirectory, then the path does not include that subdirectory, whereas the url does.
Note that path and url are identical if installation is not running from a subdirectory.


~~~~~
// Difference between path and url on site running from subdirectory /my-site/
echo $page->path(); // outputs: /about/contact/
echo $page->url();  // outputs: /my-site/about/contact/
~~~~~

@return string Returns the page path, for example: `/about/contact/`

@see Page::url(), Page::httpUrl()

## url()

Returns the URL to the page (optionally with additional $options)

- This method can also be accessed by property `$page->url` (without parenthesis).

- Like `$page->path()` but comes from server document root. Path and url are identical if
  installation is not running from a subdirectory.

- Use `$page->httpUrl()` if you need the URL to include scheme and hostname.

- **Need to hook this method?** While it's not directly hookable, it does use the `$page->path()`
  method, which *is* hookable. As a result, you can affect the output of the url() method by
  hooking the path() method instead.

## $options argument

You can specify an `$options` argument to this method with any of the following:

- `pageNum` (int|string|bool): Specify pagination number, "+" for next pagination, "-" for previous pagination,
   or boolean true (3.0.155+) for current.
- `urlSegmentStr` (string|bool): Specify a URL segment string to append, or true (3.0.155+) for current.
- `urlSegments` (array|bool): Specify array of URL segments to append (may be used instead of urlSegmentStr),
   or boolean true (3.0.155+) for current. Specify associative array to use keys and values in order (3.0.155+).
- `data` (array): Array of key=value variables to form a query string.
- `http` (bool): Specify true to make URL include scheme and hostname (default=false).
- `language` (Language): Specify Language object to return URL in that Language.
- `host` (string): Force hostname to use, i.e. 'world.com' or 'hello.world.com'. The 'http' option is implied. (3.0.178+)
- `scheme` (string): Like http option, makes URL have scheme+hostname, but you specify scheme here, i.e. 'https' (3.0.178+)
   Note that if you specify scheme of 'https' and $config->noHTTPS is true, the 'http' scheme will still be used.

You can also specify any of the following for `$options` as shortcuts:

- If you specify an `int` for options it is assumed to be the `pageNum` option.
- If you specify `+` or `-` for options it is assumed to be the `pageNum` “next/previous pagination” option.
- If you specify any other `string` for options it is assumed to be the `urlSegmentStr` option.
- If you specify a `boolean` (true) for options it is assumed to be the `http` option.

Please also note regarding `$options`:

- This method honors template slash settings for page, URL segments and page numbers.
- Any passed in URL segments are automatically sanitized with `Sanitizer::pageNameUTF8()`.
- If using the `pageNum` or URL segment options please also make sure these are enabled on the page’s template.
- The query string generated by any `data` variables is entity encoded when output formatting is on.
- The `language` option requires that the `LanguageSupportPageNames` module is installed.
- The prefix for page numbers honors `$config->pageNumUrlPrefix` and multi-language prefixes as well.

~~~~~
// Using $page->url to output navigation
foreach($page->children as $child) {
  echo "<li><a href='$child->url'>$child->title</a></li>";
}
~~~~~
~~~~~
// Difference between url() and path() on site running from subdirectory /my-site/
echo $page->url();  // outputs: /my-site/about/contact/
echo $page->path(); // outputs: /about/contact/
~~~~~
~~~~~
// Specify that you want a specific pagination (output: /example/page2)
echo $page->url(2);

// Get URL for next and previous pagination
echo $page->url('+'); // next
echo $page->url('-'); // prev

// Get a URL with scheme and hostname (output: http://domain.com/example/)
echo $page->url(true);

// Specify a URL segment string (output: /example/photos/1)
echo $page->url('photos/1');

// Use a URL segment array (output: /example/photos/1)
echo $page->url([
  'urlSegments' => [ 'photos', '1' ]
]);

// Get URL in a specific language
$fr = $languages->get('fr');
echo $page->url($fr);

// Include data/query vars (output: /example/?action=view&type=photos)
echo $page->url([
  'data' => [
    'action' => 'view',
    'type' => 'photos'
  ]
]);

// Specify multiple options (output: http://domain.com/example/foo/page3?bar=baz)
echo $page->url([
  'http' => true,
  'pageNum' => 3,
  'urlSegmentStr' => 'foo',
  'data' => [ 'bar' => 'baz' ]
]);
~~~~~


@param array|int|string|bool|Language|null $options Optionally specify options to modify default behavior (see method description).

@return string Returns page URL, for example: `/my-site/about/contact/`

@see Page::path(), Page::httpUrl(), Page::editUrl(), Page::localUrl()

## urls()

Return all URLs that this page can be accessed from (excluding URL segments and pagination)

This includes the current page URL, any other language URLs (for which page is active), and
any past (historical) URLs the page was previously available at (which will redirect to it).

- Returned URLs do not include additional URL segments or pagination numbers.
- Returned URLs are indexed by language name, i.e. “default”, “fr”, “es”, etc.
- If multi-language URLs not installed, then index is just “default”.
- Past URLs are indexed by language; then ISO-8601 date, i.e. “default;2016-08-11T07:44:43-04:00”,
  where the date represents the last date that URL was considered current.
- If PagePathHistory core module is not installed then past/historical URLs are excluded.
- You can disable past/historical or multi-language URLs by using the $options argument.


@param array $options Options to modify default behavior:
 - `http` (bool): Make URLs include current scheme and hostname (default=false).
 - `past` (bool): Include past/historical URLs? (default=true)
 - `languages` (bool): Include other language URLs when supported/available? (default=true).
 - `language` (Language|int|string): Include only URLs for this language (default=null).
    Note: the `languages` option must be true if using the `language` option.

@return array

@since 3.0.107

@see Page::addUrl(), page::removeUrl()

## httpUrl()

Returns the URL to the page, including scheme and hostname

- This method is just like the `$page->url()` method except that it also includes scheme and hostname.

- This method can also be accessed at the property `$page->httpUrl` (without parenthesis).

- It is desirable to use this method when some page templates require https while others don't.
  This ensures local links will always point to pages with the proper scheme. For other cases, it may
  be preferable to use `$page->url()` since it produces shorter output.

~~~~~
// Generating a link to this page using httpUrl
echo "<a href='$page->httpUrl'>$page->title</a>";
~~~~~


@param array $options For details on usage see `Page::url()` options argument.

@return string Returns full URL to page, for example: `https://processwire.com/about/`

@see Page::url(), Page::localHttpUrl()

## editUrl()

Return the URL necessary to edit this page

- We recommend checking that the page is editable before outputting the editUrl().
- If user opens URL in their browser and is not logged in, they must login to account with edit permission.
- This method can also be accessed by property at `$page->editUrl` (without parenthesis).

~~~~~~
if($page->editable()) {
  echo "<a href='$page->editUrl'>Edit this page</a>";
}
~~~~~~


@param array|bool|string $options Specify true for http option, specify name of field to find (3.0.151+), or use $options array:
 - `http` (bool): True to force scheme and hostname in URL (default=auto detect).
 - `language` (Language|bool): Optionally specify Language to start editor in, or boolean true to force current user language.
 - `find` (string): Name of field to find in the editor (3.0.151+)
 - `vars` (array): Additional variables to include in query string (3.0.239+)

@return string URL for editing this page

## sortfield()

Return the field name by which children are sorted

- If sort is descending, then field name is prepended with a "-".
- Returns the value "sort" if pages are unsorted or sorted manually.
- Note the return value from this method may be different from the `Page::sortfield` (lowercase) property,
  as this method considers the sort field specified with the template as well.


@return string

## index()

Return the index/position of this page relative to siblings.

If given a hidden or unpublished page, that page would not usually be part of the group of siblings.
As a result, such pages will return what the value would be if they were visible (as of 3.0.121). This
may overlap with the index of other pages, since indexes are relative to visible pages, unless you
specify an include mode (see next paragraph).

If you want this method to include hidden/unpublished pages as part of the index numbers, then
specify boolean true for the $selector argument (which implies "include=all") OR specify a
selector of "include=hidden", "include=unpublished" or "include=all".

~~~~~
$i = $page->index();
$n = $page->parent->numChildren();
echo "This page is $i out of $n total pages";
~~~~~


@param bool|string|array Specify one of the following (since 3.0.121):
 - Boolean true to include hidden and unpublished pages as part of the index numbers (same as "include=all").
 - An "include=hidden", "include=unpublished" or "include=all" selector to include them in the index numbers.
 - A string selector or selector array to filter the criteria for the returned index number.

@return int Returns index number (zero-based)

@since 3.0.24

## ___render()

Render output of this Page or a Field

You may optionally specify 1-2 arguments to the method. The first argument may be any of the following:

1. An `$options` array with predefined options or custom variables (see arguments definition).
2. A filename to use for render (in /site/templates/). When used, you can optionally specify an `$options` array as the 2nd argument.
3. A field name to render. An optional 2nd argument can be a filename (in /site/templates/fields/) to use to render the field,
   though we'd recommend just using the `renderField()` method instead.

If using the `$options` array argument (whether 1st or 2nd argument), you may use it to specify your own variables to pass along to the
template file, and those values will be available in a variable named `$options` within the scope of the template file
(see examples below).

~~~~~
// regular page render call
$out = $page->render();

// render using given file (in /site/templates/)
$out = $page->render('basic-page.php');

// render while passing in custom variables
$out = $page->render([
  'firstName' => 'Ryan',
  'lastName' => 'Cramer'
]);

// in your template file, you can access the passed-in variables like this:
echo "<p>Full name: $options[firstName] $options[lastName]</p>";
~~~~~

Note: If the page’s template has caching enabled, then this method will return a cached page render (when available)
or save a new cache. Caches are only saved on guest users.

For simpler and more specific methods, we recommend using, hooking or overriding `renderPage()` or `renderField()` instead.


@param array|string $options String of filename to use for render, field name to render, or array of options:
 - `foo_bar` (mixed): Specify any of your own variable names and values to send to the template file (foo_bar is just an example, use your own).
	- `filename` (string): Filename to render, typically relative to /site/templates/. But absolute paths must resolve somewhere in PW’s install. (default='')
	- `prependFile` (string): Filename to prepend to output, must be in /site/templates/ (default=$config->prependTemplateFile)
	- `prependFiles` (array): Array of additional filenames to prepend to output, must be relative to /site/templates/.
	- `appendFile` (string): Filename to append to output, must be in /site/templates/.
	- `appendFiles` (array): Array of additional filenames to append to output, must be relative to /site/templates/.
	- `pageStack` (array): An array of pages, when recursively rendering. Used internally. You can examine it but not change it.
	- `allowCache` (bool): Allow cache to be used when template settings ask for it? (default=true)
	- `forceBuildCache` (bool): If true, the cache will be re-created for this page, regardless of whether it’s expired or not. (default=false)
 -  Note that the prepend and append options above have default values in `$config` or with the Template.

@param array $options2 If a filename or field name was used for $options then you may optionally specify options array here instead.

@return string|mixed

@throws WireException

@see Page::renderPage(), Page::renderField(), Page::renderValue()

## ___renderPage()

Render page output

This method is essentially the same as the `render()` method except that the `render()` method
is a gateway to this method or the `renderField()` method, and this one is not. More specifically:

- This method has only one purpose, which is rendering page output.
- This method has only has one argument, which is always an array.
- This method is available only in ProcessWire 3.0.253+.

This method is preferable to `render()` when it comes hooks or overriding in custom page classes,
as you don't need to figure out anything about the arguments.

~~~~~
// regular page render call
echo $page->renderPage();

// render while passing in custom variables
echo $page->renderPage([
  'firstName' => 'Ryan',
  'lastName' => 'Cramer'
]);

// in your template file, you can access the passed-in variables like this:
echo "<p>Full name: $options[firstName] $options[lastName]</p>";

// hoooking this method
$wire->addHookAfter('Page::renderPage', function(HookEvent $event) {
  $event->return = str_replace("</body>", "<p>Hello</p></body>", $event->return);
});
~~~~~


@param array $options Custom variables to pass to template file, and/or options as described below:
 - `foo_bar` (mixed): Specify any of your own variable names and values to send to the template file (foo_bar is just an example, use your own).
	- `filename` (string): Filename to render, typically relative to /site/templates/. Absolute paths must resolve somewhere in PW’s install. (default='')
	- `prependFile` (string): Filename to prepend to output, must be in /site/templates/.
	- `prependFiles` (array): Array of additional filenames to prepend to output, must be relative to /site/templates/.
	- `appendFile` (string): Filename to append to output, must be in /site/templates/.
	- `appendFiles` (array): Array of additional filenames to append to output, must be relative to /site/templates/.
	- `allowCache` (bool): Allow cache to be used when template settings ask for it? (default=true)
	- `forceBuildCache` (bool): If true, the cache will be re-created for this page. (default=false)
 -  Note that the prepend and append options above have default values in `$config` or with the Template.

@return string|mixed Renders the rendered output

@throws WireException

@since 3.0.253

## ___renderField()

Render given field using site/templates/fields/ markup file

Shorter aliases of this method include:

- `$page->render('fieldName', $file);`
- `$page->render->fieldName;`
- `$page->_fieldName_;`

This method expects that there is a file in `/site/templates/fields/` to render the field with
one of the following:

- `/site/templates/fields/fieldName.php`
- `/site/templates/fields/fieldName.templateName.php`
- `/site/templates/fields/fieldName/$file.php`
- `/site/templates/fields/$file.php`
- `/site/templates/fields/$file/fieldName.php`
- `/site/templates/fields/$file.fieldName.php`

Note that the examples above showing $file require that the `$file` argument is specified
in the `renderField()` method call.

~~~~~
// Render output for the 'images' field (assumes you have implemented an output file)
echo $page->renderField('images');
~~~~~


@param string $fieldName May be any custom field name or native page property.

@param string $file Optionally specify file (in site/templates/fields/) to render with (may optionally omit .php extension).

@param mixed|null $value Optionally specify value to render, otherwise it will be pulled from this page.

@return mixed|string Returns the rendered value of the field

@see Page::renderValue()

## ___renderValue()

Render given value using /site/templates/fields/ markup file

See the documentation for the `Page::renderField()` method for information about the `$file` argument.

~~~~~
// Render a value using site/templates/fields/my-images.php custom output template
$images = $page->images;
echo $page->renderValue($images, 'my-images');
~~~~~


@param mixed $value Value to render

@param string $file Optionally specify file (in site/templates/fields/) to render with (may omit .php extension)

@return mixed|string Returns rendered value

## getInputfields()

Return all Inputfield objects necessary to edit this page

This method returns an InputfieldWrapper object that contains all the custom Inputfield objects
required to edit this page. You may also specify a `$fieldName` argument to limit what is contained
in the returned InputfieldWrapper.

Please note this method deals only with custom fields, not system fields name 'name' or 'status', etc.,
as those are exclusive to the ProcessPageEdit page editor.


@param string|array $fieldName Optional field to limit to, typically the name of a fieldset or tab.
 - Or optionally specify array of $options (See `Fieldgroup::getPageInputfields()` for options).

@return null|InputfieldWrapper Returns an InputfieldWrapper array of Inputfield objects, or NULL on failure.

## ___getInputfields()

Hookable version of getInputfields() method.

See the getInputfields() method above for documentation details.

@param string|array $fieldName

@return null|InputfieldWrapper Returns an InputfieldWrapper array of Inputfield objects, or NULL on failure.

## getInputfield()

Get a single Inputfield for the given field name

- If requested field name refers to a single field, an Inputfield object is returned.
- If requested field name refers to a fieldset or tab, then an InputfieldWrapper representing will be returned.
- Returned Inputfield already has values populated to it.
- Please note this method deals only with custom fields, not system fields name 'name' or 'status', etc.,
  as those are exclusive to the ProcessPageEdit page editor.


@param string $fieldName

@return Inputfield|InputfieldWrapper|null Returns Inputfield, or null if given field name doesn't match field for this page.

## ___edit()

Get front-end editable output for field (requires PageFrontEdit module to be installed)

This method requires the core `PageFrontEdit` module to be installed. If it is not installed then
it returns expected output but it is not front-end editable. This method corresponds to front-end
editing Option B. See the [front-end editor docs](https://processwire.com/docs/front-end/) for more details.
If the user does not have permission to front-end edit then returned output will not be editable.

Use `$page->edit('field_name');` instead of `$page->get('field_name');` to automatically return an editable
field value when the user is allowed to edit, or a regular field value when not. When field is
editable, hovering the value shows a different icon. **The user must double-click the area to edit.**

The 2nd and 3rd arguments are typically used only if you need to override the default presentation of
the editor or provide some kind of action or button to trigger the editor. It might also be useful if
the content to edit is not visible by default. It is recommended that you specify boolean true for the
`$modal` argument when using the `$markup` argument, which makes it open the editor in a modal window,
less likely to interfere with your front-end layout.

~~~~~
// retrieve editable value if field_name is editable, or just value if not
$value = $page->edit('field_name');
~~~~~


@param string|bool|null $key Name of field, omit to get editor active status, or boolean true to enable editor.

@param string|bool|null $markup Markup user should click on to edit $fieldName (typically omitted).

@param bool|null $modal Specify true to force editable region to open a modal window (typically omitted).

@return string|bool|mixed

@see https://processwire.com/docs/front-end/

@since 3.0.0 This method is added by a hook in PageFrontEdit and only shown in this class for documentation purposes.

## setStatus()

Set the status setting, with some built-in protections

This method is also used when you set status directly, i.e. `$page->status = $value;`.

~~~~~
// set status to unpublished
$page->setStatus('unpublished');

// set status to hidden and unpublished
$page->setStatus('hidden, unpublished');

// set status to hidden + unpublished using Page constant bitmask
$page->setStatus(Page::statusHidden | Page::statusUnpublished);
~~~~~


@param int|array|string Status value, array of status names or values, or status name string.

@return self

@see Page::addStatus(), Page::removeStatus()

## hasStatus()

Does this page have the given status?

This method is the preferred way to check if a page has a particular status.
The status may be specified as one of the `Page::status` constants or a string representing
one of the constants, i.e. `hidden`, `unpublished`, `locked`, and so on.

~~~~~
// check if page has hidden status using status name
if($page->hasStatus('hidden')) { ... }

// check if page has hidden status using status constant
if($page->hasStatus(Page::statusHidden)) { ... }

// There are also method shortcuts, i.e.
if($page->isHidden()) { ... }
if($page->isUnpublished()) { ... }
if($page->isLocked()) { ... }
~~~~~


@param int|string $status Status flag constant or string representation (hidden, locked, unpublished, etc.)

@return bool Returns true if page has the given status, or false if it doesn't.

@see Page::addStatus(), Page::removeStatus(), Page::isHidden(), Page::isUnpublished(), Page::isLocked()

## addStatus()

Add the specified status to this page

This is the preferred way to add a new status to a page. There is also a corresponding `Page::removeStatus()` method.

~~~~~
// Add hidden status to the page using status name
$page->addStatus('hidden');

// Add hidden status to the page using status constant
$page->addStatus(Page::statusHidden);
~~~~~


@param int|string $statusFlag Status flag constant or string representation (hidden, locked, unpublished, etc.)

@return $this

@see Page::removeStatus(), Page::hasStatus()

## removeStatus()

Remove the specified status from this page

This is the preferred way to remove a status from a page. There is also a corresponding `Page::addStatus()` method.

~~~~~
// Remove hidden status from the page using status name
$page->removeStatus('hidden');

// Remove hidden status from the page using status constant
$page->removeStatus(Page::statusHidden);
~~~~~


@param int|string $statusFlag Status flag constant or string representation (hidden, locked, unpublished, etc.)

@return $this

@throws WireException If you attempt to remove `Page::statusSystem` or `Page::statusSystemID` statuses without first adding `Page::statusSystemOverride` status.

@see Page::addStatus(), Page::hasStatus()

## matches()

Given a selector, return whether or not this Page matches using runtime/memory comparison

~~~~~
if($page->matches("created>=" . strtotime("today"))) {
  echo "This page was created today";
}
~~~~~


@param string|Selectors|array $s Selector to compare against (string, Selectors object, or array).

@return bool Returns true if this page matches, or false if it doesn't.

## matchesDatabase()

Given a selector, return whether or not this Page matches by querying the database

~~~~~
if($page->matchesDatabase("created>=today")) {
  echo "This page was created today";
}
~~~~~


@param string|Selectors|array $s Selector to compare against (string, Selectors object, or array).

@return bool Returns true if this page matches, or false if it doesn't.

@since 3.0.225

## is()

Does this page have the specified status number or template name?

See status flag constants at top of Page class.
You may also use status names: hidden, locked, unpublished, system, systemID


@param int|string|Selectors $status Status number, status name, or Template name or selector string/object

@return bool

## isHidden()

Does this page have a 'hidden' status?


@return bool

## isUnpublished()

Does this page have a 'unpublished' status?


@return bool

## isLocked()

Does this page have a 'locked' status?


@return bool

## isTrash()

Is this Page in the trash?


@return bool

## isPublic()

Is this page public and viewable by all?

This is a state that persists regardless of user, so has nothing to do with the current user.
To be public, the page must be published and have guest view access.


@return bool True if public, false if not

## ___isPublic()

Hookable implementation for the above isPublic function

@return bool

## status()

Get or set current status

- When manipulating status, you may prefer to use the `$page->addStatus()` and `$page->removeStatus()` methods instead.

- Use this `status()` method when you want to set multiple statuses at once, or when you want to get status rather than set it.

- You can also get or set status directly, by manipulating the `$page->status` property.

~~~~~
// Get the current status as bitmask
$status = $page->status();

// Get an array of status names assigned to page
$statuses = $page->status(true);

// Set status by Page constant bitmask
$page->status(Page::statusHidden | Page::statusUnpublished);

// Set status by name
$page->status('unpublished');

// Set status by names
$page->status(['hidden', 'unpublished']);
~~~~~


@param bool|int $value Optionally specify one of the following:
 - `true` (boolean): To return an array of status names (indexed by status number).
 - `integer|string|array`: Status number(s) or status name(s) to set the current page status (same as $page->status = $value)

@param int|null $status If you specified `true` for first argument, optionally specify status value you want to use (if not the current).

@return int|array|Page If setting status, `$this` is returned. If getting status: current status or array of status names is returned.

@see Page::addStatus(), Page::removeStatus(), Page::hasStatus()

## processFieldDataQueue()

Process and instantiate any data in the fieldDataQueue

This happens after setIsLoaded(true) is called

## of()

Get or set the current output formatting state of the page

- Always returns the current output formatting state: true if ON, or false if OFF.

- To set the current output formatting state, provide a boolean true to turn it ON, or boolean false to turn it OFF.

- Pages used for front-end output should have output formatting turned ON.

- Pages that you are manipulating and saving should have output formatting turned OFF.

See this post about [output formatting](https://processwire.com/blog/posts/output-formatting/).

~~~~~
// Set output formatting state off, for page manipulation
$page->of(false);
$page->title = 'About Us';
$page->save();
~~~~~


@param bool $outputFormatting If specified, sets output formatting state ON or OFF. If not specified, nothing is changed.

@return bool Current output formatting state (before this function call, if it was changed)

@link https://processwire.com/blog/posts/output-formatting/

## filesManager()

Return instance of PagefilesManager specific to this Page


@return PagefilesManager

## secureFiles()

Does this Page use secure Pagefiles?

See also `$template->pagefileSecure` and `$config->pagefileSecure` which determine the return value.


@return bool|null Returns boolean true if yes, false if no, or null if not known

@since 3.0.166

## hasFilesPath()

Does the page have a files path for storing files?

This will only check if files path exists, it will not create the path if it’s not already present.


@return bool

@since 3.0.138 Earlier versions must use the more verbose PagefilesManager::hasPath($page)

@see hasFiles(), filesManager()

## hasFiles()

Does the page have a files path and one or more files present in it?

This will only check if files exist, it will not create the directory if it’s not already present.


@return bool

@since 3.0.138 Earlier versions must use the more verbose PagefilesManager::hasFiles($page)

@see hasFilesPath(), filesPath(), filesManager()

## hasFile()

Does Page have given filename in its files directory?

@param string $file File basename or verbose hash

@param array $options
 - `getPathname` (bool): Get full path + filename when would otherwise return boolean true? (default=false)
 - `getPagefile` (bool): Get Pagefile object when would otherwise return boolean true? (default=false)

@return bool|string

@since 3.0.166

## filesPath()

Returns the path for files, creating it if it does not yet exist


@return string

@since 3.0.138 You can also use the equivalent but more verbose `$page->filesManager()->path()` in any version

@see filesUrl(), hasFilesPath(), hasFiles(), filesManager()

## filesUrl()

Returns the URL for files, creating it if it does not yet exist


@return string

@see filesPath(), filesManager()

@since 3.0.138 You can use the equivalent but more verbose `$page->filesManager()->url()` in any version

## getAccessParent()

Returns the page from which role/access settings are inherited from


@param string $type Optionally specify one of 'view', 'edit', 'add', or 'create' (default='view')

@return Page|NullPage Returns NullPage if none found

## getAccessTemplate()

Returns the template from which role/access settings are inherited from


@param string $type Optionally specify one of 'view', 'edit', 'add', or 'create' (default='view')

@return Template|null Returns Template object or NULL if none

## getAccessRoles()

Return Roles (PageArray) that have access to this page

This is determined from the page's template. If the page's template has roles turned off,
then it will go down the tree till it finds usable roles to use and inherit from.


@param string $type May be 'view', 'edit', 'create' or 'add' (default='view')

@return PageArray of Role objects

## hasAccessRole()

Returns whether this page has the given access role

Given access role may be a role name, role ID or Role object.


@param string|int|Role $role

@param string $type May be 'view', 'edit', 'create' or 'add' (default is 'view')

@return bool

## isEqual()

Is $value1 equal to $value2?

@param string $key Name of the key that triggered the check (see WireData::set)

@param mixed $value1

@param mixed $value2

@return bool

## getHelperInstance()

Return a Page helper class instance that’s common among all Page (and derived) objects in this ProcessWire instance

@param string $className

@return object|PageComparison|PageAccess|PageTraversal|PageValues

## comparison()

@return PageComparison

## access()

@return PageAccess

## traversal()

@return PageTraversal

## values()

@return PageValues

## meta()

Get or set page’s persistent meta data

This meta data is managed in the DB. Setting a value immediately saves it in the DB, while
getting a value immediately loads it from the DB. As a result, this data is independent of the
usual Page load and save operations. This is primarily for internal core use, but may be
useful for other specific non-core purposes as well.

Note that this data is tied to the page where you call it. Meta data is completely free-form
and has no connection to ProcessWire fields.

Values for meta data must be basic PHP types, whether arrays, strings, numbers, etc. Please do
not use objects for meta values at this time.

~~~~~
// set and save a meta value
$page->meta()->set('colors', [ 'red', 'green', 'blue' ]);

// get a meta value
$colors = $page->meta()->get('colors');

// alternate shorter syntax for either of the above
$page->meta('colors', [ 'red', 'green', 'blue' ]); // set
$colors = $page->meta('colors'); // get

// delete a meta value
$page->meta()->remove('colors');

// get the WireDataDB instance that stores the meta values,
// it has all the same methods as WireData objects...
$meta = $page->meta();

// ...such as, get all values in an array:
$values = $meta->getArray();
~~~~~


@param string|bool $key Omit to get the WireData instance or specify property name to get or set.

@param null|mixed $value Value to set for given $key or omit if getting a value.

@return WireDataDB|string|array|int|float

@since 3.0.133

## __toString()

Returns the Page ID in a string

@return string

## ___loaded()

Called when this page has been loaded and is now ready and use

~~~~~
$wire->addHook('Page::loaded', function($e) {
  $e->message("Loaded page $e->object");
});
~~~~~

## ___editReady()

Called when this page has been loaded into the Page editor (ProcessPageEdit)

~~~~~
// hook example in /site/templates/admin.php
$wire->addHook('Page::editReady', function($e) {
  $form = $e->arguments(0);
  $f = $form->getByName('title');
  if($f) $f->notes = 'Hello World!';
});
~~~~~


@param InputfieldWrapper $form The page editing form

@todo Determine if this can also apply to the front-end editor.

@since 3.0.253

## ___saveReady()

Called right before this Page is saved

If the `$name` argument is populated then only that field/property will be saved.
But if `$name` is false, then the whole page will be saved, including any
changes in the `$changes` array, and any more you make when this method is called.
This is different from the `Pages::saveReady` hookable method, which is only called
when the entire page is saved.

~~~~~
$wire->addHook('Page:saveReady', function($e) {
  $page = $e->object;
  $name = $e->arguments(1);
  if($name) {
    $e->message("Ready to save field $name on page $page");
  } else {
    $e->message("Ready to save page $page");
  }
});
~~~~~


@param array $changes Names of changed field names and/or properties

@param string|false $name Indicates whether entire page was saved or just a field/property:
 - Populated with `string` field or property name if `$page->save($name)` was used rather than `$page->save();`
 - Populated with `false` if entire page is to be saved, i.e. `$page->save()`

@since 3.0.253

## ___saved()

Called right after this Page is saved

Note that if the `$name` argument is populated then only that field/property was saved.
This is different from the `Pages::saved` hookable method, which is only called
when the entire page is saved.

~~~~~
$wire->addHook('Page:saved', function($e) {
  $page = $e->object;
  $changes = $e->arguments(0);
  $name = $e->arguments(1);
  if($name) {
    $e->message("Saved field $name on page $page");
  } else {
    $e->message("Saved page $page: " . implode(', ', $changes));
  }
});
~~~~~


@param array $changes Names of changed field names and/or properties

@param string|false $name Indicates whether entire page was saved or just a field:
 - Populated with `string` field or property name if `$page->save($name)` was used rather than `$page->save();`
 - Populated with `false` if entire page was saved, i.e. `$page->save()`

@since 3.0.253

## ___addReady()

Called when this new Page about to be added and saved to the database

~~~~~
$wire->addHook('Page::addReady', function($e) {
  $page = $e->object;
  $e->message("Ready to add new $page->template page");
});
~~~~~


@since 3.0.253

## ___added()

Called after this new Page has been added

~~~~~
$wire->addHook('Page::added', function($e) {
  $page = $e->object;
  $e->message("Added new $page->template page: $page->path");
});
~~~~~


@since 3.0.253

## ___moveReady()

Called when this Page is about to be moved to another parent

~~~~~
$wire->addHook('Page::moveReady', function($e) {
  $page = $e->object;
  list($oldParent, $newParent) = $e->arguments;
  $e->log->message("Moving page $page from $oldParent->path into $newParent->path");
  if($newParent->isTrash()) $e->log->save("trash", "Trashing page $page");
});
~~~~~


@param Page $oldParent

@param Page $newParent

@since 3.0.253

## ___moved()

Called after this Page has been moved to another parent

~~~~~
$wire->addHook('Page::moved', function($e) {
  $page = $e->object;
  list($oldParent, $newParent) = $e->arguments;
  $e->log->message("Moved page $page from $oldParent->path into $newParent->path");
  if($newParent->isTrash()) $e->log->save("trash", "Trashed page $page");
});
~~~~~


@param Page $oldParent

@param Page $newParent

@since 3.0.253

## ___deleteReady()

Called right before this page is deleted (and before any of its data is touched)

~~~~~
$wire->addHook('Page::deleteReady', function($e) {
  $page = $e->object;
  $e->warning("Page $page WILL be deleted");
});
~~~~~


@since 3.0.253

## ___deleted()

Called after this page and its data has been deleted

~~~~~
$wire->addHook('Page::deleted', function($e) {
  $page = $e->object;
  $e->warning("Page $page has been deleted");
});
~~~~~


@since 3.0.253

## ___cloneReady()

Called right before this page is cloned

~~~~~
$wire->addHook('Page::cloneReady', function($e) {
 $page = $e->object;
 $e->log->message("Page $page is ready to be cloned");
});
~~~~~


@param Page $copy The copy of this page that it will be cloned to

@since 3.0.253

## ___cloned()

Called right after this page has been cloned

~~~~~
$wire->addHook('Page::cloned', function($e) {
  $page = $e->object;
  $copy = $e->arguments(1);
  $e->log->message("Page $page has been closed to page $copy");
});
~~~~~


@param Page $copy The new cloned copy of the page

@since 3.0.253

## ___renameReady()

Called right before this page is renamed (i.e. has its name property changed)

~~~~~
$wire->addHook('Page::renameReady', function($e) {
  $page = $e->object;
  list($oldName, $newName) = $e->arguments;
  $e->message("Page $page to be renamed: $oldName => $newName");
});
~~~~~


@param string $oldName The old name

@param string $newName The new name (read-only)

@since 3.0.253

## ___renamed()

Called right after this page has been renamed (i.e. had its name property changed)

~~~~~
$wire->addHook('Page::renamed', function($e) {
  $page = $e->object;
  list($oldName, $newName) = $e->arguments;
  $e->message("Page $page renamed: $oldName => $newName");
});
~~~~~


@param string $oldName The old name

@param string $newName The new name

@since 3.0.253

## ___addStatusReady()

Called when new status flag about to be added to page but not yet saved

~~~~~
$wire->addHook('Page::addStatusReady', function($e) {
  $page = $e->object;
  $name = $e->arguments(0);
  if($name === 'unpublished' && $page->id === 1) {
    $page->removeStatus($name);
    $e->error("We do not allow unpublish of homepage");
  }
});
~~~~~


@param string $name Name of the status flag to be added, i.e. unpublished, hidden, trash, locked

@param int $value Value of the status flag to be added, a `Page::status*` constant

@since 3.0.253

## ___addedStatus()

Called when a new status flag has been added (and saved)

~~~~~
$wire->addHook('Page::addedStatus', function($e) {
  $page = $e->object;
  $name = $e->arguments(0);
  $e->message("Added status $name to page $page");
  if($name === 'unpublished') $e->message("Unpublished page $page");
});
~~~~~


@param string $name Name of the status flag that was added, i.e. unpublished, hidden, trash, locked

@param int $value Value of the status flag that was added, a `Page::status*` constant

@since 3.0.253

## ___removeStatusReady()

Called when status flag is about to removed from page but not yet saved

~~~~~
$wire->addHook('Page::removeStatusReady', function($e) {
  $page = $e->object;
  $name = $e->arguments(0);
  if($name === 'hidden' && $page->template->name === 'sitemap') {
    $page->addStatus($name);
    $e->error("Sitemap must remain hidden");
  }
});
~~~~~


@param string $name Name of the status flag to be removed, i.e. unpublished, hidden, trash, locked

@param int $value Value of the status flag to be removed, a `Page::status*` constant

@since 3.0.253

## ___removedStatus()

Called when a status flag has been removed from this page (and saved)

~~~~~
$wire->addHook('Page::removedStatus', function($e) {
  $page = $e->object;
  $name = $e->arguments(0);
  $e->message("Removed status $name from page $page");
  if($name === 'unpublished') $e->message("Published page $page");
});
~~~~~


@param string $name Name of the status flag that was removed, i.e. unpublished, hidden, trash, locked

@param int $value Value of the status flag that was removed, a `Page::status*` constant

@since 3.0.253
