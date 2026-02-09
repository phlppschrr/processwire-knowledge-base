# PagesNames

Source: `wire/core/PagesNames.php`

Inherits: `Wire`

ProcessWire Pages Names

Pages Names
$pages->names
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

Methods:
- [`__construct(Pages $pages)`](method-__construct.md)
- [`setupNewPageName(Page $page, string $format = ''): string`](method-setupnewpagename.md)
- [`hasAutogenName(Page $page): string|bool`](method-hasautogenname.md)
- [`hasAdjustedName(Page $page, bool|null $set = null): bool`](method-hasadjustedname.md)
- [`isUntitledPageName(string $name): bool`](method-isuntitledpagename.md)
- [`nameAndNumber(string $name, string $delimiter = ''): array`](method-nameandnumber.md)
- [`hasNumberSuffix(string|Page $name, bool $getNamePrefix = false): int|bool|string`](method-hasnumbersuffix.md)
- [`defaultPageNameFormat(Page $page, array $options = array()): string`](method-defaultpagenameformat.md)
- [`pageNameFromFormat(Page $page, string|array $format = '', array $options = array()): string`](method-pagenamefromformat.md)
- [`uniquePageName(string|Page|array $name = '', $page = null, array $options = array()): string`](method-uniquepagename.md)
- [`adjustNameLength(string $name, int $maxLength = 0): string`](method-adjustnamelength.md)
- [`incrementName(string $name, int|null $num = null): string`](method-incrementname.md)
- [`pageNameExists(string $name, array $options = array()): int`](method-pagenameexists.md)
- [`uniqueRandomPageName(array $options = array()): string`](method-uniquerandompagename.md)
- [`untitledPageName(): string`](method-untitledpagename.md)
- [`pageNameHasConflict(Page $page): string|bool`](method-pagenamehasconflict.md)
- [`checkNameConflicts(Page $page)`](method-checknameconflicts.md)
