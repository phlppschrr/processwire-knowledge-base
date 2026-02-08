# PageTraversal

Source: `wire/core/PageTraversal.php`

ProcessWire Page Traversal

Provides implementation for Page traversal functions.
Based upon the jQuery traversal functions.

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com

## numChildren()

Return number of children, optionally with conditions

Use this over $page->numChildren property when you want to specify a selector or when you want the result to
include only visible children. See the options for the $selector argument.

@param Page $page

@param bool|string|int|array $selector
	When not specified, result includes all children without conditions, same as $page->numChildren property.
	When a string or array, a selector is assumed and quantity will be counted based on selector.
	When boolean true, number includes only visible children (excludes unpublished, hidden, no-access, etc.)
	When boolean false, number includes all children without conditions, including unpublished, hidden, no-access, etc.
	When integer 1 number includes viewable children (as opposed to visible, viewable includes hidden pages + it also includes unpublished pages if user has page-edit permission).

@param array $options
 - `descendants` (bool): Use descendants rather than direct children

@return int Number of children

## numDescendants()

Return number of descendants, optionally with conditions

Use this over $page->numDescendants property when you want to specify a selector or when you want the result to
include only visible descendants. See the options for the $selector argument.

@param Page $page

@param bool|string|int|array $selector
	When not specified, result includes all descendants without conditions, same as $page->numDescendants property.
	When a string or array, a selector is assumed and quantity will be counted based on selector.
	When boolean true, number includes only visible descendants (excludes unpublished, hidden, no-access, etc.)
	When boolean false, number includes all descendants without conditions, including unpublished, hidden, no-access, etc.
	When integer 1 number includes viewable descendants (as opposed to visible, viewable includes hidden pages + it also includes unpublished pages if user has page-edit permission).

@return int Number of descendants

## children()

Return this page's children pages, optionally filtered by a selector

@param Page $page

@param string|array $selector Selector to use, or blank to return all children

@param array $options

@return PageArray

## child()

Return the page's first single child that matches the given selector.

Same as children() but returns a Page object or NullPage (with id=0) rather than a PageArray

@param Page $page

@param string|array $selector Selector to use, or blank to return the first child.

@param array $options

@return Page|NullPage

## parents()

Return this page's parent pages, or the parent pages matching the given selector.

@param Page $page

@param string|array|bool $selector Optional selector string to filter parents by or boolean true for reverse order

@return PageArray

## numParents()

Return number of parents (depth relative to homepage) that this page has, optionally filtered by a selector

For example, homepage has 0 parents and root level pages have 1 parent (which is the homepage), and the
number increases the deeper the page is in the pages structure.

@param Page $page

@param string $selector Optional selector to filter by (default='')

@return int Number of parents

## parentsUntil()

Return all parent from current till the one matched by $selector

@param Page $page

@param string|Page|array $selector May either be a selector or Page to stop at. Results will not include this.

@param string|array $filter Optional selector to filter matched pages by

@return PageArray

## rootParent()

Get the lowest-level, non-homepage parent of this page

rootParents typically comprise the first level of navigation on a site.

@param Page $page

@return Page

## siblings()

Return this Page's sibling pages, optionally filtered by a selector.

Note that the siblings include the current page. To exclude the current page, specify "id!=$page".

@param Page $page

@param string $selector Optional selector to filter siblings by.

@return PageArray

## _getIncludeMode()

Get include mode specified in selector or blank if none

@param string|array|Selectors $selector

@return string

## _nextFinderOptions()

Builds the PageFinder options for the _next() method

@param Page $page

@param string|array|Selectors $selector

@param array $options

@return array

## _next()

Provides the core logic for next, prev, nextAll, prevAll, nextUntil, prevUntil

@param Page $page

@param string|array|Selectors $selector Optional selector. When specified, will find nearest sibling(s) that match.

@param array $options Options to modify behavior
 - `prev` (bool): When true, previous siblings will be returned rather than next siblings.
 - `all` (bool): If true, returns all nextAll or prevAll rather than just single sibling (default=false).
 - `until` (string): If specified, returns siblings until another is found matching the given selector (default=false).
 - `qty` (bool): If true, makes it return just the quantity that would match (default=false).

@return Page|NullPage|PageArray|int Returns one of the following:
 - `PageArray` if the "all" or "until" option is specified.
 - `Page|NullPage` in other cases.

## index()

Return the index/position of the given page relative to its siblings

If given a hidden or unpublished page, that page would not usually be part of the group of siblings.
As a result, such pages will return what the value would be if they were visible (as of 3.0.121). This
may overlap with the index of other pages, since indexes are relative to visible pages, unless you
specify an include mode (see next paragraph).

If you want this method to include hidden/unpublished pages as part of the index numbers, then
specify boolean true for the $selector argument (which implies "include=all") OR specify a
selector of "include=hidden", "include=unpublished" or "include=all".

@param Page $page

@param string|array|bool|Selectors $selector Selector to apply or boolean true for "include=all" (since 3.0.121).
 - Boolean true to include hidden and unpublished pages as part of the index numbers (same as "include=all").
 - An "include=hidden", "include=unpublished" or "include=all" selector to include them in the index numbers.
 - A string selector or selector array to filter the criteria for the returned index number.

@return int Returns index number (zero-based)

## next()

Return the next sibling page

@param Page $page

@param string|array|Selectors $selector Optional selector. When specified, will find nearest next sibling that matches.

@return Page|NullPage Returns the next sibling page, or a NullPage if none found.

## prev()

Return the previous sibling page

@param Page $page

@param string|array|Selectors $selector Optional selector. When specified, will find nearest previous sibling that matches.

@return Page|NullPage Returns the previous sibling page, or a NullPage if none found.

## nextAll()

Return all sibling pages after this one, optionally matching a selector

@param Page $page

@param string|array|Selectors $selector Optional selector. When specified, will filter the found siblings.

@param array $options Options to pass to the _next() method

@return PageArray Returns all matching pages after this one.

## prevAll()

Return all sibling pages prior to this one, optionally matching a selector

@param Page $page

@param string|array|Selectors $selector Optional selector. When specified, will filter the found siblings.

@param array $options Options to pass to the _next() method

@return PageArray Returns all matching pages after this one.

## nextUntil()

Return all sibling pages after this one until matching the one specified

@param Page $page

@param string|Page|array|Selectors $selector May either be a selector or Page to stop at. Results will not include this.

@param string|array $filter Optional selector to filter matched pages by

@param array $options Options to pass to the _next() method

@return PageArray

## prevUntil()

Return all sibling pages prior to this one until matching the one specified

@param Page $page

@param string|Page|array $selector May either be a selector or Page to stop at. Results will not include this.

@param string|array $filter Optional selector to filter matched pages by

@param array $options Options to pass to the _next() method

@return PageArray

## urlOptions()

Returns the URL to the page with $options

You can specify an `$options` argument to this method with any of the following:

- `pageNum` (int|string|bool): Specify pagination number, "+" for next pagination, "-" for previous pagination, or true for current.
- `urlSegmentStr` (string|bool): Specify a URL segment string to append, or true (3.0.155+) for current.
- `urlSegments` (array|bool): Specify regular array of URL segments to append (may be used instead of urlSegmentStr).
   Specify boolean true for current URL segments (3.0.155+).
   Specify associative array (in 3.0.155+) to make both keys and values part of the URL segment string.
- `data` (array): Array of key=value variables to form a query string.
- `http` (bool): Specify true to make URL include scheme and hostname (default=false).
- `scheme` (string): Like the http option, makes URL include scheme and hostname, but you specify scheme with this, i.e. 'https' (3.0.178+)
- `host` (string): Hostname to force use of, i.e. 'world.com' or 'hello.world.com'. The 'http' option is implied when host specified. (3.0.178+)
- `language` (Language): Specify Language object to return URL in that Language.

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

@param Page $page

@param array|int|string|bool|Language $options Optionally specify options to modify default behavior (see method description).

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

@param Page $page

@param array $options Options to modify default behavior:
 - `http` (bool): Make URLs include current scheme and hostname (default=false).
 - `past` (bool): Include past/historical URLs? (default=true)
 - `languages` (bool): Include other language URLs when supported/available? (default=true).
 - `language` (Language|int|string): Include only URLs for this language (default=null).
    Note: the `languages` option must be true if using the `language` option.

@return array

## editUrl()

Return the URL necessary to edit page

- We recommend checking that the page is editable before outputting the editUrl().
- If user opens URL in their browser and is not logged in, they must login to account with edit permission.
- This method can also be accessed by property at `$page->editUrl` (without parenthesis).

~~~~~~
if($page->editable()) {
  echo "<a href='$page->editUrl'>Edit this page</a>";
}
~~~~~~

@param Page $page

@param array|bool|string $options Specify true for http option, specify name of field to find (3.0.151+), or use $options array:
 - `http` (bool): True to force scheme and hostname in URL (default=auto detect).
 - `language` (Language|bool): Optionally specify Language to start editor in, or boolean true to force current user language.
 - `find` (string): Name of field to find in the editor (3.0.151+)
 - `vars` (array): Additional variables to include in query string (3.0.239+)

@return string URL for editing this page

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

@param Page $page

@param array $options For details on usage see `Page::url()` options argument.

@return string Returns full URL to page, for example: `https://processwire.com/about/`

@see Page::url(), Page::localHttpUrl()

## references()

Return pages that are referencing the given one by way of Page references

@param Page $page

@param string|bool $selector Optional selector to filter results by or boolean true as shortcut for `include=all`.

@param Field|string $field Limit to follower pages using this field,
  - or specify boolean TRUE to make it return array of PageArrays indexed by field name.

@param bool $getCount Specify true to return counts rather than PageArray(s)

@return PageArray|array|int

@throws WireException Highly unlikely

## hasReferences()

Return number of VISIBLE pages that are following (referencing) the given one by way of Page references

Note that this excludes hidden, unpublished and otherwise non-accessible pages (access control).
If you do not want to exclude these, use the numFollowers() function instead, OR specify "include=all" for
the $selector argument.

@param Page $page

@param string $selector Filter count by this selector

@param string|Field|bool $field Limit count to given Field or specify boolean true to return array of counts.

@return int|array Returns count, or array of counts (if $field==true)

## numReferences()

Return number of ANY pages that are following (referencing) the given one by way of Page references

@param Page $page

@param string $selector Filter count by this selector

@param string|Field|bool $field Limit count to given Field or specify boolean true to return array of counts.

@return int|array Returns count, or array of counts (if $field==true)

## referencing()

Return pages that this page is referencing by way of Page reference fields

@param Page $page

@param bool|Field|string|int $field Limit results to requested field, or specify boolean true to return array indexed by field names.

@param bool $getCount Specify true to return count(s) rather than pages.

@return PageArray|int|array

## numReferencing()

Return number of pages this one is following (referencing) by way of Page references

@param Page $page

@param bool $field Optionally limit to field, or specify boolean true to return array of counts per field.

@return int|array

## links()

Find other pages linking to the given one by way contextual links is textarea/html fields

@param Page $page

@param string $selector

@param bool|string|Field $field

@param array $options
 - `getIDs` (bool): Return array of page IDs rather than Page instances. (default=false)
 - `getCount` (bool): Return a total count (int) of found pages rather than Page instances. (default=false)
 - `confirm` (bool): Confirm that the links are present by looking at the actual page field data. (default=true)
    You can specify false for this option to make it perform faster, but with a potentially less accurate result.

@return PageArray|array|int

@throws WireException

## numLinks()

Return total found number of pages linking to this one with no exclusions

@param Page $page

@param bool $field

@return int

## hasLinks()

Return total number of pages visible to current user linking to this one

@param Page $page

@param bool $field

@return array|int|PageArray

## nextSibling()

***************************************************************************************************************
LEGACY METHODS

Following are legacy methods to support backwards compatibility with previous PW versions that used
a $siblings argument for next/prev related methods.

## nextSibling()

Return the next sibling page, within a group of provided siblings (that includes the current page)

This method is the old version of the next() method and is only used if a $siblings argument is provided
to the Page::next() call.  It is much slower than the next() method.

If given a PageArray of siblings (containing the current) it will return the next sibling relative to the provided PageArray.

Be careful with this function when the page has a lot of siblings. It has to load them all, so this function is best
avoided at large scale, unless you provide your own already-reduced siblings list (like from pagination)

When using a selector, note that this method operates only on visible children. If you want something like "include=all"
or "include=hidden", they will not work in the selector. Instead, you should provide the siblings already retrieved with
one of those modifiers, and provide those siblings as the second argument to this function.

@param Page $page

@param string|array $selector Optional selector. When specified, will find nearest next sibling that matches.

@param PageArray|null $siblings Optional siblings to use instead of the default. May also be specified as first argument when no selector needed.

@return Page|NullPage Returns the next sibling page, or a NullPage if none found.

## prevSibling()

Return the previous sibling page within a provided group of siblings that contains the current page

This method is the old version of the prev() method and is only used if a $siblings argument is provided
to the Page::prev() call. It is much slower than the prev() method.

If given a PageArray of siblings (containing the current) it will return the previous sibling relative to the provided PageArray.

Be careful with this function when the page has a lot of siblings. It has to load them all, so this function is best
avoided at large scale, unless you provide your own already-reduced siblings list (like from pagination)

When using a selector, note that this method operates only on visible children. If you want something like "include=all"
or "include=hidden", they will not work in the selector. Instead, you should provide the siblings already retrieved with
one of those modifiers, and provide those siblings as the second argument to this function.

@param Page $page

@param string|array $selector Optional selector. When specified, will find nearest previous sibling that matches.

@param PageArray|null $siblings Optional siblings to use instead of the default. May also be specified as first argument when no selector needed.

@return Page|NullPage Returns the previous sibling page, or a NullPage if none found.

## nextAllSiblings()

Return all sibling pages after this one, optionally matching a selector

@param Page $page

@param string|array $selector Optional selector. When specified, will filter the found siblings.

@param PageArray|null $siblings Optional siblings to use instead of the default.

@return PageArray Returns all matching pages after this one.

## prevAllSiblings()

Return all sibling pages before this one, optionally matching a selector

@param Page $page

@param string|array $selector Optional selector. When specified, will filter the found siblings.

@param PageArray|null $siblings Optional siblings to use instead of the default.

@return PageArray

## nextUntilSiblings()

Return all sibling pages after this one until matching the one specified

@param Page $page

@param string|Page|array $selector May either be a selector or Page to stop at. Results will not include this.

@param string|array $filter Optional selector to filter matched pages by

@param PageArray|null $siblings Optional PageArray of siblings to use instead of all from the page.

@return PageArray

## prevUntilSiblings()

Return all sibling pages before this one until matching the one specified

@param Page $page

@param string|Page|array $selector May either be a selector or Page to stop at. Results will not include this.

@param string|array $filter Optional selector string to filter matched pages by

@param PageArray|null $siblings Optional PageArray of siblings to use instead of all from the page.

@return PageArray
