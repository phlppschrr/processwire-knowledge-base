# WireMarkupRegions

Source: `wire/core/WireMarkupRegions.php`

Inherits: `Wire`

ProcessWire Markup Regions

Supports finding and manipulating of markup regions in an HTML document.

Methods:
- [`find(string $selector, string $markup, array $options = array()): array`](method-find.md) Locate and return all regions of markup having the given attribute
- [`findMulti(string $selector, string $markup, array $options = array()): array`](method-findmulti.md) Multi-selector version of find(), where $selector contains CSV
- [`hasClass(string $class, array $classes): bool|string`](method-hasclass.md) Does the given class exist in given $classes array?
- [`parseFindSelector(string $find): array`](method-parsefindselector.md) Given a $find selector return array with tests and other meta info
- [`getTagRegion(string $region, array $tagInfo, array $options): array|string`](method-gettagregion.md) Given all markup after a tag, return just the portion that is the tag body/region
- [`getTagInfo(string $tag): array`](method-gettaginfo.md) Given HTML tag like “<div id='foo' class='bar baz'>” return associative array of info about it
- [`stripRegions(string $tag, string $markup, bool $getRegions = false): string|array`](method-stripregions.md) Strip the given region non-nested tags from the document
- [`stripOptional(string $markup, bool $debug = false): string`](method-stripoptional.md) Strip optional tags/comments from given markup
- [`mergeTags(string $htmlTag, array|string $mergeTag): string`](method-mergetags.md) Merge attributes from one HTML tag to another
- [`renderAttributes(array $attrs, bool $encode = true, string $quote = '"'): string`](method-renderattributes.md) Given an associative array of “key=value” attributes, render an HTML attribute string of them
- [`hasAttribute(string $name, string|bool $value, string &$html): bool`](method-hasattribute.md) Does the given attribute name and value appear somewhere in the given html?
- [`update(string $selector, string $content, string $markup, array $options = array()): string`](method-update.md) Update the region(s) that match the given $selector with the given $content (markup/text)
- [`replace(string $selector, string $replace, string $markup, array $options = array()): string`](method-replace.md) Replace the region(s) that match the given $selector with the given $replace markup
- [`append(string $selector, string $content, string $markup, array $options = array()): string`](method-append.md) Append the region(s) that match the given $selector with the given $content markup
- [`prepend(string $selector, string $content, string $markup, array $options = array()): string`](method-prepend.md) Prepend the region(s) that match the given $selector with the given $content markup
- [`before(string $selector, string $content, string $markup, array $options = array()): string`](method-before.md) Insert region(s) that match the given $selector before the given $content markup
- [`after(string $selector, string $content, string $markup, array $options = array()): string`](method-after.md) Insert the region(s) that match the given $selector after the given $content markup
- [`remove(string $selector, string $markup, array $options = array()): string`](method-remove.md) Remove the region(s) that match the given $selector
- [`initHtml(string &$html)`](method-inithtml.md) Initialize given HTML for markup regions
- [`populate(string &$htmlDocument, string|array $htmlRegions, array $options = array()): int`](method-populate.md) Identify and populate markup regions in given HTML
- [`populateSingles(string &$htmlDocument, array|string &$htmlRegions)`](method-populatesingles.md) Populate single-use tags as unnamed markup regions
- [`populateFileRegions(string &$htmlDocument, array|string &$htmlRegions, array $options, bool $debug)`](method-populatefileregions.md) Populate file regions
- [`removeRegionTags(string &$html): bool`](method-removeregiontags.md) Remove any <region> or <pw-region> tags present in the markup, leaving their innerHTML contents
- [`hasRegions(string &$html): bool`](method-hasregions.md) Is the given HTML markup likely to have regions?
- [`hasRegionActions(string &$html): bool`](method-hasregionactions.md) Does the given HTML markup have references to any pw-actions?
- [`fileRegions(): WireMarkupFileRegions`](method-fileregions.md) Get instance of WireMarkupFileRegions

Constants:
- [`debug`](const-debug.md)
- [`debugLandmark`](const-debuglandmark.md)
