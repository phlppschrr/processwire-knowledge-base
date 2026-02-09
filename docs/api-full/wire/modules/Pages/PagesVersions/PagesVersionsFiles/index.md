# PagesVersionsFiles

Source: `wire/modules/Pages/PagesVersions/PagesVersionsFiles.php`

Inherits: `Wire`

## Summary

File management for PagesVersions

Common methods:
- [`copyPageVersionFiles()`](method-copypageversionfiles.md)
- [`deletePageVersionFiles()`](method-deletepageversionfiles.md)
- [`restorePageVersionFiles()`](method-restorepageversionfiles.md)
- [`copyPageFieldVersionFiles()`](method-copypagefieldversionfiles.md)
- [`deletePageFieldVersionFiles()`](method-deletepagefieldversionfiles.md)

## Methods
- [`__construct(PagesVersions $pagesVersions)`](method-__construct.md) Construct
- [`copyPageVersionFiles(Page $page, int $version): bool|int`](method-copypageversionfiles.md) Copy files for given `$page` into version directory
- [`deletePageVersionFiles(Page $page, int $version): bool`](method-deletepageversionfiles.md) Delete files for given version
- [`restorePageVersionFiles(Page $page, int $version): int`](method-restorepageversionfiles.md) Restore files from version into live `$page`
- [`copyPageFieldVersionFiles(Page $page, Field $field, int $version): int`](method-copypagefieldversionfiles.md) Copy files for given `$page` and field into version directory
- [`deletePageFieldVersionFiles(Page $page, Field $field, int $version): int`](method-deletepagefieldversionfiles.md) Delete files for given page and field version
- [`restorePageFieldVersionFiles(Page $page, Field $field, int $version): int`](method-restorepagefieldversionfiles.md) Restore files for given field from version into live `$page`
- [`getFileFields(Page $page, array $options = []): Field[]`](method-getfilefields.md) Get all fields that can support files
- [`fieldSupportsFiles(Field|string|int $field): bool`](method-fieldsupportsfiles.md) Does given field support files?
- [`useFilesByField(Page $page, array $names = []): bool`](method-usefilesbyfield.md) Copy/restore files individually by field for given page?
- [`pageVersion(Page $page, int $version): NullPage|Page`](method-pageversion.md) Ensure that given page is given version, and return version page if it isn't already
