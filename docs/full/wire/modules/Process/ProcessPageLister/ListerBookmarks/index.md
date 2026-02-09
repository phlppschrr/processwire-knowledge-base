# ListerBookmarks

Source: `wire/modules/Process/ProcessPageLister/ListerBookmarks.php`

Inherits: `Wire`

Methods:
- [`__construct(Page $page, User $user)`](method-__construct.md) Construct
- [`setPage(Page $page)`](method-setpage.md) Set the Lister page that bookmarks will be for
- [`setUser(User $user)`](method-setuser.md) Set user that bookmarks will be for
- [`getOwnedBookmarks(int $userID = 0): array`](method-getownedbookmarks.md) Get owned bookmarks
- [`saveOwnedBookmarks(array $bookmarks)`](method-saveownedbookmarks.md) Save owned bookmarks
- [`getUserSettings(int $userID = 0): array`](method-getusersettings.md) Get user’s lister settings for current page
- [`saveUserSettings(array $settings): bool`](method-saveusersettings.md) Save user settings for current page
- [`getPublicBookmarks(): array`](method-getpublicbookmarks.md) Get public bookmarks (from module config)
- [`savePublicBookmarks(array $bookmarks): bool`](method-savepublicbookmarks.md) Save public bookmarks (to module config)
- [`saveBookmarks(array $allBookmarks)`](method-savebookmarks.md) Save all bookmarks (whether public or owned)
- [`getAllBookmarks(): array`](method-getallbookmarks.md) Get all bookmarks (public and owned)
- [`getBookmarks(): array`](method-getbookmarks.md) Get configured bookmarks allowed for current user, indexed by bookmark ID (int)
- [`getBookmark(string|int $bookmarkID, int|null $type = null): array|null`](method-getbookmark.md) Get a bookmark by ID (whether public or owned)
- [`getBookmarkUrl(string $bookmarkID, User|null $user = null): string`](method-getbookmarkurl.md) Get the URL for a bookmark
- [`getBookmarkEditUrl(string $bookmarkID): string`](method-getbookmarkediturl.md) Get the URL for a bookmark
- [`getBookmarkTitle(int|array $bookmarkID): mixed|string`](method-getbookmarktitle.md) Get the title for the given bookmark ID or bookmark array
- [`deleteBookmarkByID(int $bookmarkID): bool`](method-deletebookmarkbyid.md) Delete a bookmark by ID
- [`filterBookmarksByType(array $allBookmarks, int $type): array`](method-filterbookmarksbytype.md) Filter bookmarks, removing those that are not of the requested type
- [`filterBookmarksByAccess(array $bookmarks): array`](method-filterbookmarksbyaccess.md) Filter bookmarks, removing those user does not have access to
- [`isBookmarkEditable(array $bookmark): bool`](method-isbookmarkeditable.md) Is the given bookmark editable?
- [`isBookmarkViewable(array $bookmark): bool`](method-isbookmarkviewable.md) Is the given bookmark viewable?
- [`isBookmarkDeletable(array $bookmark): bool`](method-isbookmarkdeletable.md) Is the given bookmark deletable?
- [`_bookmark(array $bookmark = array()): array`](method-_bookmark.md) Get a template array for a bookmark
- [`_bookmarkID(string|array $bookmarkID): string`](method-_bookmarkid.md) Sanitize a bookmark ID
- [`intID(string|int $val): int`](method-intid.md) Given an id or string key, return an int ID
- [`strID(string|int $val): int`](method-strid.md) Given an id or string key, return an string ID (with leading underscore)
- [`bookmarkStrID(string|int $val, int $type): int`](method-bookmarkstrid.md) Given an id or string key, return an bookmark string ID
- [`isID(string $val): bool|int`](method-isid.md) Does the given string value represent an ID? If yes, return ID, otherwise return false.
- [`idType(string $val): int`](method-idtype.md) Get the type from the given id string
- [`typePrefix(int $type): string`](method-typeprefix.md) Get the prefix for the given bookmark type
- [`isValidPageKey(int|string $val): bool`](method-isvalidpagekey.md) Is the given page ID or key valid and existing?
- [`readableBookmarkSelector(array $bookmark): string`](method-readablebookmarkselector.md) Return a readable selector from bookmark for output purposes

Constants:
- [`typePublic = 0`](const-typepublic.md)
- [`typeOwned = 1`](const-typeowned.md)
