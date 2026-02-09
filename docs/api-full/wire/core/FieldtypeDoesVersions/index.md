# FieldtypeDoesVersions

Source: `wire/core/Interfaces.php`

## Summary

Indicates Fieldtype has version support and manages its own versions

Common methods:
- [`getPageFieldVersion()`](method-getpagefieldversion.md)
- [`savePageFieldVersion()`](method-savepagefieldversion.md)
- [`restorePageFieldVersion()`](method-restorepagefieldversion.md)
- [`deletePageFieldVersion()`](method-deletepagefieldversion.md)

## Methods
- [`getPageFieldVersion(Page $page, Field $field, int $version): mixed`](method-getpagefieldversion.md) Get the value for given page, field and version
- [`savePageFieldVersion(Page $page, Field $field, int $version): bool`](method-savepagefieldversion.md) Save version of given page field
- [`restorePageFieldVersion(Page $page, Field $field, int $version): bool`](method-restorepagefieldversion.md) Restore version of given page field to live page
- [`deletePageFieldVersion(Page $page, Field $field, int $version): bool`](method-deletepagefieldversion.md) Delete version
