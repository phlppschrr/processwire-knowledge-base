# PagesVersions::savePageVersion()

Source: `wire/modules/Pages/PagesVersions/PagesVersions.module.php`

Save a page version


@param Page $page

@param int|PageVersionInfo $version Version number or PageVersionInfo
 - If given version number is greater than 0 and version doesn't exist, it will be added.
 - If 0 or omitted and given page is already a version, its version will be updated.
 - If 0 or omitted and given page is not a version, this method behaves the same as
   the `addPageVersion()` method and returns the added version number.

@param array $options
 - `description` (string): Optional text description for version (default='')
 - `update` (bool): Update version if it already exists (default=true)

@return int|array Returns version number saved or added or 0 on fail

@throws WireException|\PDOException
