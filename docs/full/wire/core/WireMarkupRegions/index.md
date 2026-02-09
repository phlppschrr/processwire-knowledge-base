# WireMarkupRegions

Source: `wire/core/WireMarkupRegions.php`

Inherits: `Wire`

ProcessWire Markup Regions

Supports finding and manipulating of markup regions in an HTML document.

Methods:
- [`find(string $selector, string $markup, array $options = array()): array`](method-find.md)
- [`findMulti(string $selector, string $markup, array $options = array()): array`](method-findmulti.md)
- [`hasClass(string $class, array $classes): bool|string`](method-hasclass.md)
- [`parseFindSelector(string $find): array`](method-parsefindselector.md)
- [`getTagRegion(string $region, array $tagInfo, array $options): array|string`](method-gettagregion.md)
- [`getTagInfo(string $tag): array`](method-gettaginfo.md)
- [`stripRegions(string $tag, string $markup, bool $getRegions = false): string|array`](method-stripregions.md)
- [`stripOptional(string $markup, bool $debug = false): string`](method-stripoptional.md)
- [`mergeTags(string $htmlTag, array|string $mergeTag): string`](method-mergetags.md)
- [`renderAttributes(array $attrs, bool $encode = true, string $quote = '"'): string`](method-renderattributes.md)
- [`hasAttribute(string $name, string|bool $value, string &$html): bool`](method-hasattribute.md)
- [`update(string $selector, string $content, string $markup, array $options = array()): string`](method-update.md)
- [`replace(string $selector, string $replace, string $markup, array $options = array()): string`](method-replace.md)
- [`append(string $selector, string $content, string $markup, array $options = array()): string`](method-append.md)
- [`prepend(string $selector, string $content, string $markup, array $options = array()): string`](method-prepend.md)
- [`before(string $selector, string $content, string $markup, array $options = array()): string`](method-before.md)
- [`after(string $selector, string $content, string $markup, array $options = array()): string`](method-after.md)
- [`remove(string $selector, string $markup, array $options = array()): string`](method-remove.md)
- [`initHtml(string &$html)`](method-inithtml.md)
- [`populate(string &$htmlDocument, string|array $htmlRegions, array $options = array()): int`](method-populate.md)
- [`populateSingles(string &$htmlDocument, array|string &$htmlRegions)`](method-populatesingles.md)
- [`populateFileRegions(string &$htmlDocument, array|string &$htmlRegions, array $options, bool $debug)`](method-populatefileregions.md)
- [`removeRegionTags(string &$html): bool`](method-removeregiontags.md)
- [`hasRegions(string &$html): bool`](method-hasregions.md)
- [`hasRegionActions(string &$html): bool`](method-hasregionactions.md)
- [`fileRegions(): WireMarkupFileRegions`](method-fileregions.md)

Constants:
- [`debug`](const-debug.md)
- [`debugLandmark`](const-debuglandmark.md)
