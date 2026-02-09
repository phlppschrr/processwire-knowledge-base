# MarkupQA

Source: `wire/core/MarkupQA.php`

Inherits: `Wire`

## Summary

HTML Markup Quality Assurance

Common methods:
- [`setPage()`](method-setpage.md)
- [`setField()`](method-setfield.md)
- [`ignorePaths()`](method-ignorepaths.md)
- [`debug()`](method-debug.md)
- [`verbose()`](method-verbose.md)

Provides runtime quality assurance for markup stored in [textarea] field values.

1. Ensures URLs referenced in <a> and <img> tags are relative to actual site root.
2. Ensures local page URLs referenced in <a> tags up-to-date with current `$page` URL.
3. Identifies and logs <img> tags that point to non-existing files in PW's file system.
4. Re-creates image variations that don't exist, when the original still exists.
5. Populates blank 'alt' attributes with actual file description.

- For #1 use the wakeupUrls(`$value`) and sleepUrls(`$value`) methods.
- For #2 use the wakeupHrefs(`$value`) and sleepHrefs(`$value`) methods.
- For #3-5 use the checkImgTags(`$value`, `$options`) method, where `$options` specifies 3-5.

Runtime errors are logged to: /site/assets/logs/markup-qa-errors.txt

## Methods
- [`__construct(?Page $page = null, ?Field $field = null)`](method-__construct.md) Construct
- [`setPage(Page $page)`](method-setpage.md) Set the current Page
- [`setField(Field $field)`](method-setfield.md) Set the current Field
- [`ignorePaths(array|string|null $paths = null, bool $replace = false): array`](method-ignorepaths.md) Get or set paths to ignore for link abstraction
- [`debug(bool|null $set = null): bool`](method-debug.md) Get or set debug status
- [`verbose(bool|null $set = null): bool`](method-verbose.md) Get or set verbose state
- [`wakeupUrls(&$value)`](method-wakeupurls.md) Wakeup URLs in href or src attributes for presentation
- [`sleepUrls(&$value)`](method-sleepurls.md) Sleep URLs in href or src attributes for storage
- [`checkUrls(string &$value, bool $sleep = false)`](method-checkurls.md) Wake URLs for wakeup or sleep, converting root URLs as necessary
- [`relativeToAbsolutePath(string $path): string`](method-relativetoabsolutepath.md) Convert a relative path to be absolute
- [`sleepLinks(string &$value)`](method-sleeplinks.md) Sleep href attributes, adding a data-pwid attribute to <a> tags that resolve to a Page
- [`wakeupLinks(&$value): array`](method-wakeuplinks.md) Wakeup href attributes, using the data-pwid attribute to update the href attribute as necessary
- [`findLinks(?Page $page = null, array $fieldNames = array(), string $selector = '', array $options = array()): PageArray|array|int`](method-findlinks.md) Find pages linking to another
- [`linkWarning(string $path, bool $logWarning = true)`](method-linkwarning.md) Display and log a warning about a path that didn't resolve
- [`checkImgTags(string &$value, array $options = array())`](method-checkimgtags.md) Quality assurance for <img> tags
- [`checkImgTag(string &$value, string $img, array $options = array())`](method-checkimgtag.md) Quality assurance for one <img> tag
- [`checkImgExists(Pageimage $pagefile, $img, $src, &$value): int`](method-checkimgexists.md) Attempt to re-create images that don't exist, when possible
- [`error(string $text, int $flags = 0): $this`](method-error.md) Record error message to image-errors log
- [`setVerbose($verbose): string|array|int|null|$this`](method-setverbose.md) Get or set a setting
- [`getPagePathFromId(int $pageID, Language|null $language = null): string`](method-getpagepathfromid.md) Given page ID return the path to it
- [`isPagePathHooked(): bool`](method-ispagepathhooked.md) Is the Page::path method hooked in a manner that might affect MarkupQA?
