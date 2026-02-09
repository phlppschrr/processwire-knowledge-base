# Templates

Source: `wire/core/Templates.php`

Inherits: `WireSaveableItems`

## Summary

ProcessWire Templates

Common methods:
- [`init()`](method-init.md)
- [`getAll()`](method-getall.md)
- [`getWireArray()`](method-getwirearray.md)
- [`makeItem()`](method-makeitem.md)
- [`loadAllLazyItems()`](method-loadalllazyitems.md)

Groups:
Group: [other](group-other.md)

Manages and provides access to all the Template instances


Manages and provides access to all the Templates.

## Methods
- [`__construct(Fieldgroups $fieldgroups)`](method-__construct.md) Construct the Templates
- [`add(string $name, array $properties = array()): Template`](method-add.md) Add and save new template (and fieldgroup) with given name and return it
- [`get(string|int $key): Template|null|string`](method-get.md) Get a template by name or ID
- [`save(Saveable $item): bool`](method-___save.md) (hookable) Save a Template
- [`delete(Saveable $item): bool`](method-___delete.md) (hookable) Delete a Template
- [`clone(Saveable $item, string $name = ''): bool|Template`](method-___clone.md) (hookable) Clone the given Template
- [`rename(Template $template, string $name)`](method-rename.md) Rename given template (and its fieldgroup, and file, when possible)
- [`getNumPages(Template $tpl): int`](method-getnumpages.md) Return the number of pages using the provided Template
- [`encodeData(array $value): string`](method-encodedata.md) Overridden from WireSaveableItems to retain specific keys
- [`getExportData(Template $template): array`](method-___getexportdata.md) (hookable) Export Template data for external use
- [`setImportData(Template $template, array $data): array`](method-___setimportdata.md) (hookable) Given an array of Template export data, import it to the given Template
- [`getParentPage(Template $template, bool $checkAccess = false, bool|int $getAll = false): Page|NullPage|null|PageArray`](method-getparentpage.md) Return the parent page that this template assumes new pages are added to
- [`getParentPages(Template $template, bool $checkAccess = false, int $maxStatus = 0): PageArray`](method-getparentpages.md) Return all possible parent pages for the given template, if predefined
- [`getPageClass(Template $template, bool $withNamespace = true): string`](method-getpageclass.md) Get class name to use for pages using given Template
- [`getTags(bool $getTemplateNames = false): array`](method-___gettags.md) (hookable) Get all tags used by templates
- [`fileModified(Template $template)`](method-___filemodified.md) (hookable) Hook called when a Template detects that its file has changed
