# $pages->getById($_ids, $template = null, $parent_id = null): PageArray|Page

Source: `wire/core/Pages.php`

Given an array or CSV string of Page IDs, return a PageArray (internal API)

Note that this method is primarily for internal use and most of the options available are specific to the needs
of core methods that utilize them. All pages loaded by ProcessWire pass through this method.

Optionally specify an `$options` array rather than a template for argument 2. When present, the `template` and `parent_id`
arguments may be provided in the given $options array. These options may be specified:

**LOAD OPTIONS (argument 2 array):**

- `cache` (bool): Place loaded pages in memory cache? (default=true)
- `getFromCache` (bool): Allow use of previously cached pages in memory (rather than re-loading it from DB)? (default=true)
- `template` (Template): Instance of Template, see the $template argument for details.
- `parent_id` (int): Parent ID, see $parent_id argument for details.
- `getNumChildren` (bool): Specify false to disable retrieval and population of 'numChildren' Page property. (default=true)
- `getOne` (bool): Specify true to return just one Page object, rather than a PageArray. (default=false)
- `autojoin` (bool): Allow use of autojoin option? (default=true)
- `joinFields` (array): Autojoin the field names specified in this array, regardless of field settings (requires autojoin=true). (default=empty)
- `joinSortfield` (bool): Whether the 'sortfield' property will be joined to the page. (default=true)
- `findTemplates` (bool): Determine which templates will be used (when no template specified) for more specific autojoins. (default=true)
- `pageClass` (string): Class to instantiate Page objects with. Leave blank to determine from template. (default=auto-detect)
- `pageArrayClass` (string): PageArray-derived class to store pages in (when 'getOne' is false). (default=PageArray)
- `pageArray` (PageArray): Populate this existing PageArray rather than creating a new one. (default=null)
- `page` (Page): Existing Page object to populate (also requires the getOne option to be true). (default=null)

**Use the `$options` array for potential speed optimizations:**

- Specify a `template` with your call, when possible, so that this method doesn't have to determine it separately.
- Specify false for `getNumChildren` for potential speed optimization when you know for certain pages will not have children.
- Specify false for `autojoin` for potential speed optimization in certain scenarios (can also be a bottleneck, so be sure to test).
- Specify false for `joinSortfield` for potential speed optimization when you know the Page will not have children or won't need to know the order.
- Specify false for `findTemplates` so this method doesn't have to look them up. Potential speed optimization if you have few autojoin fields globally.
- Note that if you specify false for `findTemplates` the pageClass is assumed to be 'Page' unless you specify something different for the 'pageClass' option.

## Example

~~~~~
// Retrieve pages by IDs in CSV string
$items = $pages->getById("1111,2222,3333");

// Retrieve pages by IDs in PHP array
$items = $pages->getById([1111,2222,3333]);

// Specify that retrieved pages are using template 'skyscraper' as an optimization
$items = $pages->getById([1111,2222,3333], $templates->get('skyscraper'));

// Retrieve pages with $options array
$items = $pages->getById([1111,2222,3333], [
  'template' => $templates->get('skyscraper'),
  'parent_id' => 1024
]);
~~~~~

## Usage

~~~~~
// basic usage
$items = $pages->getById($_ids);

// usage with all arguments
$items = $pages->getById($_ids, $template = null, $parent_id = null);
~~~~~

## Arguments

- `$_ids` `array|WireArray|string|int` Array of Page IDs, CSV string of Page IDs, or single page ID.
- `$template` (optional) `Template|array|null` Specify a template to make the load faster, because it won't have to attempt to join all possible fields... just those used by the template. Optionally specify an $options array instead, see the method notes above.
- `$parent_id` (optional) `int|null` Specify a parent to make the load faster, as it reduces the possibility for full table scans. This argument is ignored when an options array is supplied for the $template.

## Return value

- `PageArray|Page` Returns Page only if the 'getOne' option is specified, otherwise always returns a PageArray.

## Exceptions

- `WireException`
