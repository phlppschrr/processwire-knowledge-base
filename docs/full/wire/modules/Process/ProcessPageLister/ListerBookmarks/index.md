# ListerBookmarks

Source: `wire/modules/Process/ProcessPageLister/ListerBookmarks.php`

Inherits: `Wire`

Methods:
- [`__construct(Page $page, User $user)`](method-__construct.md)
- [`setPage(Page $page)`](method-setpage.md)
- [`setUser(User $user)`](method-setuser.md)
- [`getOwnedBookmarks(int $userID = 0): array`](method-getownedbookmarks.md)
- [`saveOwnedBookmarks(array $bookmarks)`](method-saveownedbookmarks.md)
- [`getUserSettings(int $userID = 0): array`](method-getusersettings.md)
- [`saveUserSettings(array $settings): bool`](method-saveusersettings.md)
- [`getPublicBookmarks(): array`](method-getpublicbookmarks.md)
- [`savePublicBookmarks(array $bookmarks): bool`](method-savepublicbookmarks.md)
- [`saveBookmarks(array $allBookmarks)`](method-savebookmarks.md)
- [`getAllBookmarks(): array`](method-getallbookmarks.md)
- [`getBookmarks(): array`](method-getbookmarks.md)
- [`getBookmark(string|int $bookmarkID, int|null $type = null): array|null`](method-getbookmark.md)
- [`getBookmarkUrl(string $bookmarkID, User|null $user = null): string`](method-getbookmarkurl.md)
- [`getBookmarkEditUrl(string $bookmarkID): string`](method-getbookmarkediturl.md)
- [`getBookmarkTitle(int|array $bookmarkID): mixed|string`](method-getbookmarktitle.md)
- [`deleteBookmarkByID(int $bookmarkID): bool`](method-deletebookmarkbyid.md)
- [`filterBookmarksByType(array $allBookmarks, int $type): array`](method-filterbookmarksbytype.md)
- [`filterBookmarksByAccess(array $bookmarks): array`](method-filterbookmarksbyaccess.md)
- [`isBookmarkEditable(array $bookmark): bool`](method-isbookmarkeditable.md)
- [`isBookmarkViewable(array $bookmark): bool`](method-isbookmarkviewable.md)
- [`isBookmarkDeletable(array $bookmark): bool`](method-isbookmarkdeletable.md)
- [`_bookmark(array $bookmark = array()): array`](method-_bookmark.md)
- [`_bookmarkID(string|array $bookmarkID): string`](method-_bookmarkid.md)
- [`intID(string|int $val): int`](method-intid.md)
- [`strID(string|int $val): int`](method-strid.md)
- [`bookmarkStrID(string|int $val, int $type): int`](method-bookmarkstrid.md)
- [`isID(string $val): bool|int`](method-isid.md)
- [`idType(string $val): int`](method-idtype.md)
- [`typePrefix(int $type): string`](method-typeprefix.md)
- [`isValidPageKey(int|string $val): bool`](method-isvalidpagekey.md)
- [`readableBookmarkSelector(array $bookmark): string`](method-readablebookmarkselector.md)

Constants:
- [`typePublic`](const-typepublic.md)
- [`typeOwned`](const-typeowned.md)
