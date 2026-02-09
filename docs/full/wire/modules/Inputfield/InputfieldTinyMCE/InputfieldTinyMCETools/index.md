# InputfieldTinyMCETools

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCETools.php`

Inherits: `InputfieldTinyMCEClass`


Groups:
Group: [other](group-other.md)

InputfieldTinyMCETools

Helper tools for InputfieldTinyMCE module.

Methods:
- [`sanitizeNames(string|array $value): string`](method-sanitizenames.md) Sanitize toolbar or plugin names
- [`getImageField(): Field|null`](method-getimagefield.md) Get field that images can be uploaded to or null if none found
- [`purifyValue(string $value): string`](method-purifyvalue.md) Clean up a value that will be sent to/from the editor
- [`purifyValueToggles(string $value): string`](method-purifyvaluetoggles.md) Apply markup cleaning toggles
- [`purifier(): MarkupHTMLPurifier`](method-purifier.md)
- [`linkConfig(string $key = ''): array|string`](method-linkconfig.md) Get config for ProcessPageEditLink module
- [`jsonDecode(string $json, string $propertyName): array`](method-jsondecode.md) Decode JSON
- [`jsonDecodeFile(string $file, string $propertyName): array`](method-jsondecodefile.md) Decode JSON file
- [`jsonEncode(array $a, string $propertyName, bool $pretty = true): string`](method-jsonencode.md) Encode array to JSON
- [`getPasteFiltersForJS(): string`](method-getpastefiltersforjs.md) Prepare pasteFilters string for JS
- [`__get($name): string`](method-__get.md) Get content.css file contents for inline editor output
- [`__get(string $name): array|mixed|string|null`](method-__get.md)
