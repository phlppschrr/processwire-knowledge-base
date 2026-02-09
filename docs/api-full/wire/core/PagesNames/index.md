# PagesNames

Source: `wire/core/PagesNames.php`

Inherits: `Wire`

## Summary

ProcessWire Pages Names

Common methods:
- [`setupNewPageName()`](method-setupnewpagename.md)
- [`hasAutogenName()`](method-hasautogenname.md)
- [`hasAdjustedName()`](method-hasadjustedname.md)
- [`isUntitledPageName()`](method-isuntitledpagename.md)
- [`nameAndNumber()`](method-nameandnumber.md)

Pages Names
`$pages->names`
This class includes methods for generating and modifying page names.
While these methods are mosty for internal core use, some may at times be useful from the public API as well.
You can access methods from this class via the Pages API variable at `$pages->names()`.
~~~~~
if($pages->names()->pageNameExists('something')) {
  // A page named “something” exists
}

// generate a globally unique random page name
$name = $pages->names()->uniqueRandomPageName();
~~~~~

## Methods
- [`__construct(Pages $pages)`](method-__construct.md) Construct
- [`setupNewPageName(Page $page, string $format = ''): string`](method-setupnewpagename.md) Assign a name to given Page (if it doesn’t already have one)
- [`hasAutogenName(Page $page): string|bool`](method-hasautogenname.md) Does the given page have an auto-generated name (during this request)?
- [`hasAdjustedName(Page $page, bool|null $set = null): bool`](method-hasadjustedname.md) Does the given page have a modified “name” during this request?
- [`isUntitledPageName(string $name): bool`](method-isuntitledpagename.md) Does the given page have an untitled page name?
- [`nameAndNumber(string $name, string $delimiter = ''): array`](method-nameandnumber.md) If given name has a numbered suffix, return array with name (excluding suffix) and the numbered suffix
- [`hasNumberSuffix(string|Page $name, bool $getNamePrefix = false): int|bool|string`](method-hasnumbersuffix.md) Does the given name or Page have a number suffix? Returns the number if yes, or false if not
- [`defaultPageNameFormat(Page $page, array $options = array()): string`](method-defaultpagenameformat.md) Get the name format string that should be used for given $page if no name was assigned
- [`pageNameFromFormat(Page $page, string|array $format = '', array $options = array()): string`](method-pagenamefromformat.md) Create a page name from the given format
- [`uniquePageName(string|Page|array $name = '', $page = null, array $options = array()): string`](method-uniquepagename.md) Get a unique page name
- [`adjustNameLength(string $name, int $maxLength = 0): string`](method-adjustnamelength.md) If name exceeds maxLength, truncate it, while keeping any numbered suffixes in place
- [`incrementName(string $name, int|null $num = null): string`](method-incrementname.md) Increment the suffix of a page name, or add one if not present
- [`pageNameExists(string $name, array $options = array()): int`](method-pagenameexists.md) Is the given name is use by a page?
- [`uniqueRandomPageName(array $options = array()): string`](method-uniquerandompagename.md) Get a random, globally unique page name
- [`untitledPageName(): string`](method-untitledpagename.md) Return the untitled page name string
- [`pageNameHasConflict(Page $page): string|bool`](method-pagenamehasconflict.md) Does given page have a name that has a conflict/collision?
- [`checkNameConflicts(Page $page)`](method-checknameconflicts.md) Check given page’s name for conflicts and increment as needed while also triggering a warning notice
