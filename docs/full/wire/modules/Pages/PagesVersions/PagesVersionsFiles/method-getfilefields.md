# $pagesVersionsFiles->getFileFields(Page $page, array $options = []): Field[]

Source: `wire/modules/Pages/PagesVersions/PagesVersionsFiles.php`

Get all fields that can support files

## Arguments

- `$page` `Page`
- `$options` (optional) `array` - `populated` (bool): Only return populated file fields with 1+ files in them? (default=false) - `names` (array): Limit check to these field names or omit for all. (default=[])

## Return value

Field[] Returned fields array is indexed by field name
