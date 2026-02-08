# PagesLoader

Source: `wire/core/PagesLoader.php`

ProcessWire Pages Loader

Pages Loader
$pages->loader
Implements page finding/loading methods for the $pages API variable.
Please always use `$pages->method()` rather than `$pages->loader->method()` in cases where there is overlap.

ProcessWire 3.x, Copyright 2025 by Ryan Cramer
https://processwire.com

## __construct()

Construct

@param Pages $pages

## setOutputFormatting()

Set whether loaded pages have their outputFormatting turned on or off

By default, it is turned on.


@param bool $outputFormatting

## getOutputFormatting()

Get whether loaded pages have their outputFormatting turned on or off


@return bool

## setAutojoin()

Enable or disable use of autojoin for all queries

Default should always be true, and you may use this to turn it off temporarily, but
you should remember to turn it back on


@param bool $autojoin

## getAutojoin()

Get whether autojoin is enabled for page loading queries


@return bool

## normalizeSelectorString()

Normalize a selector string

This is to reduce the number of unique selectors that produce the same result.
It is helpful with caching results, so that we don't cache the same results multiple
times because they used slightly different selectors.

@param string $selector

@param bool $convertIDs Normalize to integer ID or array of integer IDs when possible (default=true)

@return array|int|string

## normalizeSelector()

Normalize a selector

This is to reduce the number of unique selectors that produce the same result.
It is helpful with caching results, so that we don't cache the same results multiple
times because they used slightly different selectors.

@param string|int|array $selector

@param bool $convertIDs Convert ID-only selectors to integers or arrays of integers?

@return array|int|string

## isIdArray()

Is this an array of IDs? Also sanitizes to all integers when true

@param array $a

@return bool

## findShortcut()

Helper for find() method to attempt to shortcut the find when possible

@param string|array|Selectors $selector

@param array $options

@param array $loadOptions

@return bool|Page|PageArray Returns boolean false when no shortcut available

## find()

Given a Selector string, return the Page objects that match in a PageArray.

Non-visible pages are excluded unless an `include=hidden|unpublished|all` mode is specified in the selector string,
or in the `$options` array. If 'all' mode is specified, then non-accessible pages (via access control) can also be included.


@param string|int|array|Selectors $selector Specify selector (standard usage), but can also accept page ID or array of page IDs.

@param array|string $options Optional one or more options that can modify certain behaviors. May be assoc array or key=value string.
	- `findOne` (bool): Apply optimizations for finding a single page.
 - `findAll` (bool): Find all pages with no exclusions (same as include=all option).
 - `findIDs` (bool|int): Makes method return raw array rather than PageArray, specify one of the following:
     • `true` (bool): return array of [ [id, templates_id, parent_id] ] for each page.
     • `1` (int): Return just array of just page IDs, [id, id, id]
     • `2` (int): Return all pages table columns in associative array for each page (3.0.153+).
     • `3` (int): Same as 2 + dates are unix timestamps + has 'pageArray' key w/blank PageArray for pagination info (3.0.172+).
     • `4` (int): Same as 3 + return PageArray instead if one is available in cache (3.0.172+).
	- `getTotal` (bool): Whether to set returning PageArray's "total" property (default: true except when findOne=true)
 - `cache` (bool): Allow caching of selectors and pages loaded (default=true). Also sets loadOptions[cache].
 - `allowCustom` (bool): Whether to allow use of "_custom=new selector" in selectors (default=false).
 - `lazy` (bool): Makes find() return Page objects that don't have any data populated to them (other than id and template).
	- `loadPages` (bool): Whether to populate the returned PageArray with found pages (default: true).
	   The only reason why you'd want to change this to false would be if you only needed the count details from
	   the PageArray: getTotal(), getStart(), getLimit, etc. This is intended as an optimization for Pages::count().
	   Does not apply if $selectorString argument is an array.
 - `caller` (string): Name of calling function, for debugging purposes, i.e. pages.count
	- `include` (string): Inclusion mode of 'hidden', 'unpublished' or 'all'. Default=none. Typically you would specify this
	   directly in the selector string, so the option is mainly useful if your first argument is not a string.
 - `stopBeforeID` (int): Stop loading pages once page matching this ID is found (default=0).
 - `startAfterID` (int): Start loading pages once page matching this ID is found (default=0).
	- `loadOptions` (array): Assoc array of options to pass to getById() load options. (does not apply when 'findIds' > 3).
 - `joinFields` (array): Names of fields to autojoin, or empty array to join none; overrides field autojoin settings (default=null) 3.0.172+

@return PageArray|array

## findMin()

Minimal find for reduced or delayed overload in some circumstances

This combines the page finding and page loading operation into a single operation
and single query, unlike a regular find() which finds matching page IDs in one
query and then loads them in a separate query. As a result this method does not
need to call the getByIds() method to load pages, as it is able to load them itself.

This strategy may eventually replace the “find() + getByIds()” strategy, but for the
moment is only used when the `$pages->find()` method specifies `field=name` in
the selector. In that selector, `name` can be any field name, or group of them, i.e.
`title|date|summary`, or a non-existing field like `none` to specify that no fields
should be autojoin (for fastest performance).

Note that while this might reduce overhead in some cases, it can also increase the
overall request time if you omit fields that are actually used on the resulting pages.
For instance, if the `title` field is an autojoin field (as it is by default), and
we do a `$pages->find('template=blog-post, field=none');` and then render a list of
blog post titles, then we have just increased overhead because PW would have to
perform a separate query to load each blog-post page’s title. On the other hand, if
we render a list of blog post titles with date and summary, and the date and summary
fields are not configured as autojoin fields, then we can specify all those that we
use in our rendered list to greatly improve performance, like this:
`$pages->find('template=blog-post, field=title|date|summary');`.

While this method combines what find() and getById() do in one query, there does not
appear to be any overhead benefit when the two strategies are dealing with identical
conditions, like the same autojoin fields.


@param string|array|Selectors $selector

@param array $options
 - `cache` (bool): Allow pulling from and saving results to cache? (default=true)
 - `joinFields` (array): Names of fields to also join into the page load

@return PageArray

@throws WireException

@since 3.0.172

## findOne()

Like find() but returns only the first match as a Page object (not PageArray)

This is functionally similar to the get() method except that its default behavior is to
filter for access control and hidden/unpublished/etc. states, in the same way that the
find() method does. You can add an `include=` to your selector with value `hidden`,
`unpublished` or `all` to change this behavior, just like with find().

Unlike the find() method, this method performs a secondary runtime access check by calling
`$page->viewable()` with the found $page, and returns a `NullPage` if the page is not
viewable with that call. In 3.0.142+, an `include=` mode of `all` or `unpublished` will
override this, where appropriate.

This method also accepts an `$options` array, whereas `Pages::get()` does not.


@param string|int|array|Selectors $selector

@param array|string $options See $options for `Pages::find`

@return Page|NullPage

## findCache()

Find pages and cache the result for specified period of time

Use this when you want to cache a slow or complex page finding operation so that it doesn’t
have to be repated for every web request. Note that this only caches the find operation
and not the loading of the found pages.

~~~~~
$items = $pages->findCache("title%=foo"); // 60 seconds (default)
$items = $pages->findCache("title%=foo", 3600); // 1 hour
$items = $pages->findCache("title%=foo", "+1 HOUR");  // same as above
~~~~~


@param string|array|Selectors $selector

@param int|string|bool|null $expire When the cache should expire, one of the following:
 - Max age integer (in seconds).
 - Any string accepted by PHP’s `strtotime()` that specifies when the cache should be expired.
 - Any `WireCache::expire…` constant or anything accepted by the `WireCache::get()` $expire argument.

@param array $options Options to pass to `$pages->getByIDs()`, or:
 - `findIDs` (bool): Return just the page IDs rather then the actual pages? (default=false)

@return PageArray|array

@since 3.0.218

## get()

Returns the first page matching the given selector with no exclusions


@param string|int|array|Selectors $selector

@param array $options See Pages::find method for options

@return Page|NullPage Always returns a Page object, but will return NullPage (with id=0) when no match found

## has()

Is there any page that matches the given $selector in the system? (with no exclusions)

- This can be used as an “exists” or “getID” type of method.
- Returns ID of first matching page if any exist, or 0 if none exist (returns array if `$verbose` is true).
- Like with the `get()` method, no pages are excluded, so an `include=all` is not necessary in selector.
- If you need to quickly check if something exists, this method is preferable to using a count() or get().

When `$verbose` option is used, an array is returned instead. Verbose return array includes all columns
from the matching row in the pages table.


@param string|int|array|Selectors $selector

@param bool $verbose Return verbose array with all pages columns rather than just page id? (default=false)

@param array $options Additional options to pass in find() $options argument (not currently applicable)

@return array|int

@since 3.0.153

## getById()

Given an array or CSV string of Page IDs, return a PageArray

Optionally specify an $options array rather than a template for argument 2. When present, the 'template' and 'parent_id' arguments may be provided
in the given `$options` array. These options may be specified:

LOAD OPTIONS (argument 2 array):

- `cache` (bool): Place loaded pages in memory cache? (default=true)
- `getFromCache` (bool): Allow use of previously cached pages in memory (rather than re-loading it from DB)? (default=true)
- `template` (Template): See $template argument for details. (default=null)
- `parent_id` (int): See $parent_id argument for details (default=null)
- `getNumChildren` (bool): Specify false to disable retrieval and population of 'numChildren' Page property. (default=true)
- `getOne` (bool): Specify true to return just one Page object, rather than a PageArray. (default=false)
- `autojoin` (bool): Allow use of autojoin option? (default=true)
- `joinFields` (array): Autojoin the field names specified in this array, regardless of field settings, requires `autojoin=true`. (default=empty)
- `joinSortfield` (bool): Whether the 'sortfield' property will be joined to the page. (default=true)
- `findTemplates` (bool): Determine which templates will be used (when no template specified) for more specific autojoins. (default=true)
- `pageClass` (string): Class to instantiate Page objects with. Leave blank to determine from template. (default=auto-detect)
- `pageArrayClass` (string): PageArray-derived class to store pages in (when 'getOne' is false). (default=PageArray)
- `pageArray` (PageArray): Optional predefined PageArray to populate to (default=null)
- `page` (Page): Existing Page object to populate (also requires the getOne option to be true). (default=null)
- `caller` (string): Name of calling function, for debugging purposes (default=blank).

Use the `$options` array for potential speed optimizations:
- Specify a 'template' with your call, when possible, so that this method doesn't have to determine it separately.
- Specify false for 'getNumChildren' for potential speed optimization when you know for certain pages will not have children.
- Specify false for 'autojoin' for potential speed optimization in certain scenarios (can also be a bottleneck, so be sure to test).
- Specify false for 'joinSortfield' for potential speed optimization when you know the Page will not have children or won't need to know the order.
- Specify false for 'findTemplates' so this method doesn't have to look them up. Potential speed optimization if you have few autojoin fields globally.
- Note that if you specify false for 'findTemplates' the pageClass is assumed to be 'Page' unless you specify something different for the 'pageClass' option.


@param array|WireArray|string|int $_ids Array of page IDs, comma or pipe-separated string of IDs, or single page ID (string or int)
 or in 3.0.156+ array of associative arrays where each in format: [ 'id' => 123, 'templates_id' => 456 ]

@param Template|array|string|int|null $template Specify a template to make the load faster, because it won't have to attempt to join all possible fields...
 just those used by the template. Optionally specify an $options array instead, see the method notes above.

@param int|null $parent_id Specify a parent to make the load faster, as it reduces the possibility for full table scans.
	This argument is ignored when an options array is supplied for the $template.

@return PageArray|Page|NullPage Returns Page only if the 'getOne' option is specified, otherwise always returns a PageArray.

@throws WireException

## findByName()

Find page(s) by name

This method is optimized just for finding pages by name and it does
not perform any filtering or access checking.


@param string $name Match this page name

@param array $options
 - `parent' (int|Page): Match this parent ID (default=0)
 - `parentName` (string): Match this parent name (default='')
 - `getArray` (bool): Get PHP info array rather than Page|NullPage|PageArray? (default=false)
 - `getOne` (bool|int): Get just one match of Page or NullPage? (default=false)
    When true, if multiple pages match then NullPage will be returned. To instead return
    the first match, specify int `1` instead of boolean true.

@return array|NullPage|Page|PageArray

## getPath()

Given an ID return a path to a page, without loading the actual page

Please note
===========
1) Always returns path in default language, unless a language argument/option is specified.
2) Path may be different from 'url' as it doesn't include $config->urls->root at the beginning.
3) In most cases, it's preferable to use $page->path() rather than this method. This method is
   here just for cases where a path is needed without loading the page.
4) It's possible for there to be Page::path() hooks, and this method completely bypasses them,
   which is another reason not to use it unless you know such hooks aren't applicable to you.


@param int|Page $id ID of the page you want the path to

@param null|array|Language|int|string $options Specify $options array or Language object, id or name. Allowed options:
 - language (int|string|anguage): To retrieve in non-default language, specify language object, ID or name (default=null)
 - useCache (bool): Allow pulling paths from already loaded pages? (default=true)
 - usePagePaths (bool): Allow pulling paths from PagePaths module, if installed? (default=true)

@return string Path to page or blank on error/not-found

## getByPath()

Get a page by its path, similar to $pages->get('/path/to/page/') but with more options


Please note
===========
1) There are no exclusions for page status or access. If needed, you should validate access
   on any page returned from this method.
2) In a multi-language environment, you must specify the $useLanguages option to be true, if you
   want a result for a $path that is (or might be) a multi-language path. Otherwise, multi-language
   paths will make this method return a NullPage (or 0 if getID option is true).
3) Partial paths may also match, so long as the partial path is completely unique in the site.
   If you don't want that behavior, double check the path of the returned page.
4) See also the newer/more capable `$pages->pathFinder()` methods `get('/path/')` and `getPage('/path/')`.

@param string $path

@param array|bool $options array of options (below), or specify boolean for $useLanguages option only.
 - `getID` (bool): Specify true to just return the page ID (default=false)
 - `useLanguages` (bool): Specify true to allow retrieval by language-specific paths (default=false)
 - `useHistory` (bool): Allow use of previous paths used by the page, if PagePathHistory module is installed (default=false)
 - `allowUrl` (bool): Allow getting page by path OR url? Specify false to find only by path. This option only applies if
    the site happens to run from a subdirectory. (default=true) 3.0.184+
 - `allowPartial` (bool): Allow partial paths to match? (default=true) 3.0.184+
 - `allowUrlSegments` (bool): Allow paths with URL segments to match? When true and page match cannot be found, the closest
    parent page that allows URL segments will be returned. Found URL segments are populated to a `_urlSegments` array
    property on the returned page object. This also cancels the allowPartial setting. (default=false) 3.0.184+

@return Page|int

@see PagesPathFinder::get(), PagesPathFinder::getPage()

## getFresh()

Get a fresh, non-cached copy of a Page from the database

This method is the same as `$pages->get()` except that it skips over all memory caches when loading a Page.
Meaning, if the Page is already in memory, it doesn’t use the one in memory and instead reloads from the DB.
Nor does it place the Page it loads in any memory cache. Use this method to load a fresh copy of a page
that you might need to compare to an existing loaded copy, or to load a copy that won’t be seen or touched
by anything in ProcessWire other than your own code.

~~~~~
$p1 = $pages->get(1234);
$p2 = $pages->get($p1->path);
$p1 === $p2; // true: same Page instance

$p3 = $pages->getFresh($p1);
$p1 === $p3; // false: same Page but different instance
~~~~~


@param Page|string|array|Selectors|int $selectorOrPage Specify Page to get copy of, selector or ID

@param array $options Options to modify behavior

@return Page|NullPage

@since 3.0.172

## getNumChildren()

Load total number of children from DB for given page


@param int|Page $page Page or Page ID

@return int

@throws WireException

@since 3.0.172

## count()

Count and return how many pages will match the given selector string


@param string|array|Selectors $selector Specify selector, or omit to retrieve a site-wide count.

@param array|string $options See $options in Pages::find

@return int

## preloadFields()

Preload/Prefetch fields for page together as a group (experimental)

This is an optimization that enables you to load the values for multiple fields into
a page at once, and often in a single query. This is similar to the `joinFields` option
when loading a page, or the `autojoin` option configured with a field, except that it
can be used after a page is already loaded. It provides a performance improvement
relative lazy-loading of fields individually as they are accessed.

Preload works only with Fieldtypes that do not override the core’s loading methods.
Preload also does not work with FieldtypeMulti types at present, except for the Page
Fieldtype when configured to load a single page. Though it can be enabled for testing
purposes using the `useFieldtypeMulti` $options argument.

NOTE: This function is currently experimental, recommended for testing only.


@param Page $page Page to preload fields for

@param array $fieldNames Names of fields to preload

@param array $options
 - `debug` (bool): Specify true to include additional debug info in return value (default=false).
 - `useFieldtypeMulti` (bool): Enable FieldtypeMulti for testing purposes (default=false).
 - `loadPageRefs` (bool): Optimization to early load pages in page reference fields? (default=true)

@return array Array containing what was loaded and skipped

@since 3.0.243

## preloadAllFields()

Preload all supported fields for given page (experimental)

NOTE: This function is currently experimental, recommended for testing only.


@param Page $page Page to preload fields for

@param array $options
 - `debug` (bool): Specify true to return array of debug info (default=false).
 - `skipFieldNames` (array): Optional names of fields to skip over (default=[]).
 - See the `PagesLoader::preloadFields()` method for additional options.

@return array Array of details

@since 3.0.243

## skipPreloadField()

Skip preloading of this field or fieldtype?

Returns populated string with reason if yes, or blank string if no.

@param Page $page

@param Field $field

@param array $options

@return string

## filterListable()

Remove pages from already-loaded PageArray aren't visible or accessible

@param PageArray $items

@param string $includeMode Optional inclusion mode:
	- 'hidden': Allow pages with 'hidden' status'
	- 'unpublished': Allow pages with 'unpublished' or 'hidden' status
	- 'all': Allow all pages (not much point in calling this method)

@param array $options loadOptions

@return PageArray

## getNativeColumns()

Returns an array of all columns native to the pages table


@return array of column names, also indexed by column name

## getNativeColumnValue()

Get value of of a native column in pages table for given page ID


@param int|Page $id Page ID

@param string $column

@return int|string|bool Returns int/string value on success or boolean false if no matching row

@since 3.0.156

@throws \PDOException|WireException

## isNativeColumn()

Is the given column name native to the pages table?


@param $columnName

@return bool

## debug()

Get or set debug state


@param bool|null $debug

@return bool

## getTotalPagesLoaded()

Return the total quantity of pages loaded by getById()


@return int

## getLastPageFinder()

Get last used instance of PageFinder (for debugging purposes)


@return PageFinder|null

@since 3.0.146

## isLoading()

Are we currently loading pages?


@return bool

@since 3.0.195
