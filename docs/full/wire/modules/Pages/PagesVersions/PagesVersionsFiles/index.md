# PagesVersionsFiles

Source: `wire/modules/Pages/PagesVersions/PagesVersionsFiles.php`

Inherits: `Wire`

File management for PagesVersions

Methods:
- [`__construct(PagesVersions $pagesVersions)`](method-__construct.md)
- [`copyPageVersionFiles(Page $page, $version)`](method-copypageversionfiles.md)
- [`copyPageVersionFiles(Page $page, int $version): bool|int`](method-copypageversionfiles.md)
- [`deletePageVersionFiles(Page $page, int $version): bool`](method-deletepageversionfiles.md)
- [`restorePageVersionFiles(Page $page, int $version): int`](method-restorepageversionfiles.md)
- [`copyPageFieldVersionFiles(Page $page, Field $field, $version)`](method-copypagefieldversionfiles.md)
- [`copyPageFieldVersionFiles(Page $page, Field $field, int $version): int`](method-copypagefieldversionfiles.md)
- [`deletePageFieldVersionFiles(Page $page, Field $field, int $version): int`](method-deletepagefieldversionfiles.md)
- [`restorePageFieldVersionFiles(Page $page, Field $field, int $version): int`](method-restorepagefieldversionfiles.md)
- [`getFileFields(Page $page, array $options = []): Field[]`](method-getfilefields.md)
- [`fieldSupportsFiles(Field|string|int $field): bool`](method-fieldsupportsfiles.md)
- [`useFilesByField(Page $page, array $names = []): bool`](method-usefilesbyfield.md)
- [`pageVersion(Page $page, int $version): NullPage|Page`](method-pageversion.md)
- [`hookPagefilesManagerPath(HookEvent $event)`](method-hookpagefilesmanagerpath.md)
