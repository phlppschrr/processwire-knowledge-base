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
Method: [__construct()](method-__construct.md)
Method: [setPage()](method-setpage.md)
Method: [setField()](method-setfield.md)
Method: [ignorePaths()](method-ignorepaths.md)
Method: [debug()](method-debug.md)
Method: [verbose()](method-verbose.md)
Method: [wakeupUrls()](method-wakeupurls.md)
Method: [sleepUrls()](method-sleepurls.md)
Method: [checkUrls()](method-checkurls.md)
Method: [relativeToAbsolutePath()](method-relativetoabsolutepath.md)
Method: [sleepLinks()](method-sleeplinks.md)
Method: [wakeupLinks()](method-wakeuplinks.md)
Method: [findLinks()](method-findlinks.md)
Method: [linkWarning()](method-linkwarning.md)
Method: [checkImgTags()](method-checkimgtags.md)
Method: [checkImgTag()](method-checkimgtag.md)
Method: [checkImgExists()](method-checkimgexists.md)
Method: [error()](method-error.md)
Method: [setVerbose()](method-setverbose.md)
Method: [getPagePathFromId()](method-getpagepathfromid.md)
Method: [isPagePathHooked()](method-ispagepathhooked.md)
