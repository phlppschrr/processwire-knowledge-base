# FieldtypeHasFiles

Source: `wire/core/Interfaces.php`

Indicates Fieldtype manages files

## hasFiles()

Whether or not given Page/Field has any files connected with it

@param Page $page

@param Field $field

@return bool

## getFiles()

Get array of full path/file for all files managed by given page and field

@param Page $page

@param Field $field

@return array

## getFilesPath()

Get path where files are (or would be) stored

@param Page $page

@param Field $field

@return string
