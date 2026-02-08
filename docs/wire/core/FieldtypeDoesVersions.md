# FieldtypeDoesVersions

Source: `wire/core/Interfaces.php`

Indicates Fieldtype has version support and manages its own versions

## getPageFieldVersion()

Get the value for given page, field and version

@param Page $page

@param Field $field

@param int $version

@return mixed

## savePageFieldVersion()

Save version of given page field

@param Page $page

@param Field $field

@param int $version

@return bool

## restorePageFieldVersion()

Restore version of given page field to live page

@param Page $page

@param Field $field

@param int $version

@return bool

## deletePageFieldVersion()

Delete version

@param Page $page

@param Field $field

@param int $version

@return bool
