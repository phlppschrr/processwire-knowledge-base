# FieldtypeHasFiles

Source: `wire/core/Interfaces.php`

## Summary

Indicates Fieldtype manages files

Common methods:
- [`hasFiles()`](method-hasfiles.md)
- [`getFiles()`](method-getfiles.md)
- [`getFilesPath()`](method-getfilespath.md)

## Methods
- [`hasFiles(Page $page, Field $field): bool`](method-hasfiles.md) Whether or not given Page/Field has any files connected with it
- [`getFiles(Page $page, Field $field): array`](method-getfiles.md) Get array of full path/file for all files managed by given page and field
- [`getFilesPath(Page $page, Field $field): string`](method-getfilespath.md) Get path where files are (or would be) stored
