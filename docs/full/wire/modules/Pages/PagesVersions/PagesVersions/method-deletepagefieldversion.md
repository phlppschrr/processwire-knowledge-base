# PagesVersions::deletePageFieldVersion()

Source: `wire/modules/Pages/PagesVersions/PagesVersions.module.php`

Delete a page field version

This should not be called independently of deletePageVersion() as this
method does not delete any files connected to the version.

@param Page $page

@param Field $field

@param int $version

@return bool
