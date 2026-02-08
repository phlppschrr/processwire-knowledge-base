# $pagesLoader->filterListable(PageArray $items, $includeMode = '', array $options = array()): PageArray

Source: `wire/core/PagesLoader.php`

Remove pages from already-loaded PageArray aren't visible or accessible

## Arguments

- PageArray $items
- string $includeMode Optional inclusion mode: - 'hidden': Allow pages with 'hidden' status' - 'unpublished': Allow pages with 'unpublished' or 'hidden' status - 'all': Allow all pages (not much point in calling this method)
- array $options loadOptions

## Return value

PageArray
