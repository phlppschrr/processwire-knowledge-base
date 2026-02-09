# MarkupQA

Source: `wire/core/MarkupQA.php`

Inherits: `Wire`

HTML Markup Quality Assurance

Provides runtime quality assurance for markup stored in [textarea] field values.

1. Ensures URLs referenced in <a> and <img> tags are relative to actual site root.
2. Ensures local page URLs referenced in <a> tags up-to-date with current $page URL.
3. Identifies and logs <img> tags that point to non-existing files in PW's file system.
4. Re-creates image variations that don't exist, when the original still exists.
5. Populates blank 'alt' attributes with actual file description.

- For #1 use the wakeupUrls($value) and sleepUrls($value) methods.
- For #2 use the wakeupHrefs($value) and sleepHrefs($value) methods.
- For #3-5 use the checkImgTags($value, $options) method, where $options specifies 3-5.

Runtime errors are logged to: /site/assets/logs/markup-qa-errors.txt

Methods:
- [`__construct(?Page $page = null, ?Field $field = null)`](method-__construct.md)
- [`setPage(Page $page)`](method-setpage.md)
- [`setField(Field $field)`](method-setfield.md)
- [`ignorePaths(array|string|null $paths = null, bool $replace = false): array`](method-ignorepaths.md)
- [`debug(bool|null $set = null): bool`](method-debug.md)
- [`verbose(bool|null $set = null): bool`](method-verbose.md)
- [`wakeupUrls(&$value)`](method-wakeupurls.md)
- [`sleepUrls(&$value)`](method-sleepurls.md)
- [`checkUrls(string &$value, bool $sleep = false)`](method-checkurls.md)
- [`relativeToAbsolutePath(string $path): string`](method-relativetoabsolutepath.md)
- [`sleepLinks(string &$value)`](method-sleeplinks.md)
- [`wakeupLinks(&$value): array`](method-wakeuplinks.md)
- [`findLinks(?Page $page = null, array $fieldNames = array(), string $selector = '', array $options = array()): PageArray|array|int`](method-findlinks.md)
- [`linkWarning(string $path, bool $logWarning = true)`](method-linkwarning.md)
- [`checkImgTags(string &$value, array $options = array())`](method-checkimgtags.md)
- [`checkImgTag(string &$value, string $img, array $options = array())`](method-checkimgtag.md)
- [`checkImgExists(Pageimage $pagefile, $img, $src, &$value): int`](method-checkimgexists.md)
- [`error(string $text, int $flags = 0): $this`](method-error.md)
- [`setVerbose($verbose): string|array|int|null|$this`](method-setverbose.md)
- [`getPagePathFromId(int $pageID, Language|null $language = null): string`](method-getpagepathfromid.md)
- [`isPagePathHooked(): bool`](method-ispagepathhooked.md)
