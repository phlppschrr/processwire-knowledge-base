# Templates

Source: `wire/core/Templates.php`

Inherits: `WireSaveableItems`


Groups:
Group: [other](group-other.md)

ProcessWire Templates

Manages and provides access to all the Template instances


Manages and provides access to all the Templates.

Methods:
- [`__construct(Fieldgroups $fieldgroups)`](method-__construct.md)
- [`add(string $name, array $properties = array()): Template`](method-add.md)
- [`get(string|int $key): Template|null|string`](method-get.md)
- [`save(Saveable $item): bool`](method-___save.md) (hookable)
- [`delete(Saveable $item): bool`](method-___delete.md) (hookable)
- [`clone(Saveable $item, string $name = ''): bool|Template`](method-___clone.md) (hookable)
- [`rename(Template $template, string $name)`](method-rename.md)
- [`getNumPages(Template $tpl): int`](method-getnumpages.md)
- [`encodeData(array $value): string`](method-encodedata.md)
- [`getExportData(Template $template): array`](method-___getexportdata.md) (hookable)
- [`setImportData(Template $template, array $data): array`](method-___setimportdata.md) (hookable)
- [`getParentPage(Template $template, bool $checkAccess = false, bool|int $getAll = false): Page|NullPage|null|PageArray`](method-getparentpage.md)
- [`getParentPages(Template $template, bool $checkAccess = false, int $maxStatus = 0): PageArray`](method-getparentpages.md)
- [`getPageClass(Template $template, bool $withNamespace = true): string`](method-getpageclass.md)
- [`getTags(bool $getTemplateNames = false): array`](method-___gettags.md) (hookable)
- [`fileModified(Template $template)`](method-___filemodified.md) (hookable)
