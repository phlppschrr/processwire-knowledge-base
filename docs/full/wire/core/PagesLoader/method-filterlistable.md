# PagesLoader::filterListable()

Source: `wire/core/PagesLoader.php`

Remove pages from already-loaded PageArray aren't visible or accessible

@param PageArray $items

@param string $includeMode Optional inclusion mode:
	- 'hidden': Allow pages with 'hidden' status'
	- 'unpublished': Allow pages with 'unpublished' or 'hidden' status
	- 'all': Allow all pages (not much point in calling this method)

@param array $options loadOptions

@return PageArray
