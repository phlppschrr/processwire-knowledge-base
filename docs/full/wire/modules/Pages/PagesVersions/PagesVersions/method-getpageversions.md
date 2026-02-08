# PagesVersions::getPageVersions()

Source: `wire/modules/Pages/PagesVersions/PagesVersions.module.php`

Get all versions for given page

~~~~~
$page = $pages->get(1234);
$versions = $pagesVersions->getPageVersions($page);
foreach($versions as $p) {
  echo $p->get('_version')->version; // i.e. 2, 3, 4, etc.
}
~~~~~


@param Page $page

@param array $options
 - `getInfo` (bool): Specify true to instead get PageVersionInfo objects (default=false)
 - `sort` (string): Sort by property, one of: 'created', '-created', 'version', '-version' (default='-created')
 - `version` (array): Limit to this version number, for internal use (default=0)

@return PageVersionInfo[]|Page[]
 - Returns Array of `Page` objects or array of `PageVersionInfo` objects if `getInfo` requested.
 - When returning pages, version info is in `$page->_version` value of each page,
   which is a `PageVersionInfo` object.

@throws WireException
