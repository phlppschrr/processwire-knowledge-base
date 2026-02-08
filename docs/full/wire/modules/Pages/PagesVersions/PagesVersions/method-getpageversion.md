# PagesVersions::getPageVersion()

Source: `wire/modules/Pages/PagesVersions/PagesVersions.module.php`

Get requested page version in a copy of given page

~~~~~
$page = $pages->get(1234);
$pageV2 = $pagesVersions->getPageVersion($page, 2);
~~~~~


@param Page $page Page that version is for

@param int $version Version number to get

@param array $options
 - `names` (array): Optionally load only these field/property names from version.

@return Page|NullPage
 - Returned page is a clone/copy of the given page updated for version data.
 - Returns a `NullPage` if requested version is not found or not allowed.
