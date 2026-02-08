# $wireTextTools->markupToText($str, array $options = array()): string

Source: `wire/core/WireTextTools.php`

Convert HTML markup to readable text

Like PHP’s strip_tags but with some small improvements in HTML-to-text conversion that
improves the readability of the text.

In 3.0.197+ inner content of script, style and object tags is now removed, rather than just the tags.
To revert this behavior or to remove content of additional tags, see the `clearTags` option.

Note that this method differs from the `Sanitizer::markupToText()` method in that this method is newer,
more powerful and has more options. But the two methods differ in how they perform markup-to-text
conversion so you may want to review and try both to determine which one better suits your needs.

## Usage

~~~~~
// basic usage
$string = $wireTextTools->markupToText($str);

// usage with all arguments
$string = $wireTextTools->markupToText($str, array $options = array());
~~~~~

## Arguments

- `$str` `string` String to convert to text
- `$options` (optional) `array` - `keepTags` (array): Tag names to keep in returned value, i.e. [ "em", "strong" ]. (default=none) - `clearTags` (array): Tags that should also have their content cleared. (default=[ "script", "style", "object" ]) Since 3.0.197 - `splitBlocks` (string): String to split paragraph and header elements. (default="\n\n") - `convertEntities` (bool): Convert HTML entities to plain text equivalents? (default=true) - `listItemPrefix` (string): Prefix for converted list item `<li>` elements. (default='• ') - `linksToUrls` (bool): Convert links to `(url)` rather than removing? (default=true) Since 3.0.132 - `linksToMarkdown` (bool): Convert links to `[text](url)` rather than removing? (default=false) Since 3.0.197 - `uppercaseHeadlines` (bool): Convert headline tags to uppercase? (default=false) Since 3.0.132 - `underlineHeadlines` (bool): Underline headlines with "=" or "-"? (default=true) Since 3.0.132 - `collapseSpaces` (bool): Collapse extra/redundant extra spaces to single space? (default=true) Since 3.0.132 - `replacements` (array): Associative array of strings to manually replace. (default=['&nbsp;' => ' '])

## Return value

- `string`

## See Also

- [Sanitizer::markupToText()](../Sanitizer/method-markuptotext.md)
