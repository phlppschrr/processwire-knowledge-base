# $pagesLoaderCache->cacheGroup(Page $page, $groupName)

Source: `wire/core/PagesLoaderCache.php`

Cache given page into a named group that it can be uncached with

## Usage

~~~~~
// basic usage
$result = $pagesLoaderCache->cacheGroup($page, $groupName);

// usage with all arguments
$result = $pagesLoaderCache->cacheGroup(Page $page, $groupName);
~~~~~

## Arguments

- `$page` `Page`
- `$groupName` `string`

## Since

3.0.198
