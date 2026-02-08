# PagesVersionsFiles::getFileFields()

Source: `wire/modules/Pages/PagesVersions/PagesVersionsFiles.php`

Get all fields that can support files

@param Page $page

@param array $options
 - `populated` (bool): Only return populated file fields with 1+ files in them? (default=false)
 - `names` (array): Limit check to these field names or omit for all. (default=[])

@return Field[] Returned fields array is indexed by field name
