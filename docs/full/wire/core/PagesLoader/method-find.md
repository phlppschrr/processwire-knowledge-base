# $pagesLoader->find($selector, $options = array()): PageArray|array

Source: `wire/core/PagesLoader.php`

Given a Selector string, return the Page objects that match in a PageArray.

Non-visible pages are excluded unless an `include=hidden|unpublished|all` mode is specified in the selector string,
or in the `$options` array. If 'all' mode is specified, then non-accessible pages (via access control) can also be included.

## Arguments

- `$selector` `string|int|array|Selectors` Specify selector (standard usage), but can also accept page ID or array of page IDs.
- `$options` (optional) `array|string` Optional one or more options that can modify certain behaviors. May be assoc array or key=value string. - `findOne` (bool): Apply optimizations for finding a single page. - `findAll` (bool): Find all pages with no exclusions (same as include=all option). - `findIDs` (bool|int): Makes method return raw array rather than PageArray, specify one of the following: • `true` (bool): return array of [ [id, templates_id, parent_id] ] for each page. • `1` (int): Return just array of just page IDs, [id, id, id] • `2` (int): Return all pages table columns in associative array for each page (3.0.153+). • `3` (int): Same as 2 + dates are unix timestamps + has 'pageArray' key w/blank PageArray for pagination info (3.0.172+). • `4` (int): Same as 3 + return PageArray instead if one is available in cache (3.0.172+). - `getTotal` (bool): Whether to set returning PageArray's "total" property (default: true except when findOne=true) - `cache` (bool): Allow caching of selectors and pages loaded (default=true). Also sets loadOptions[cache]. - `allowCustom` (bool): Whether to allow use of "_custom=new selector" in selectors (default=false). - `lazy` (bool): Makes find() return Page objects that don't have any data populated to them (other than id and template). - `loadPages` (bool): Whether to populate the returned PageArray with found pages (default: true). The only reason why you'd want to change this to false would be if you only needed the count details from the PageArray: getTotal(), getStart(), getLimit, etc. This is intended as an optimization for Pages::count(). Does not apply if $selectorString argument is an array. - `caller` (string): Name of calling function, for debugging purposes, i.e. pages.count - `include` (string): Inclusion mode of 'hidden', 'unpublished' or 'all'. Default=none. Typically you would specify this directly in the selector string, so the option is mainly useful if your first argument is not a string. - `stopBeforeID` (int): Stop loading pages once page matching this ID is found (default=0). - `startAfterID` (int): Start loading pages once page matching this ID is found (default=0). - `loadOptions` (array): Assoc array of options to pass to getById() load options. (does not apply when 'findIds' > 3). - `joinFields` (array): Names of fields to autojoin, or empty array to join none; overrides field autojoin settings (default=null) 3.0.172+

## Return value

PageArray|array
