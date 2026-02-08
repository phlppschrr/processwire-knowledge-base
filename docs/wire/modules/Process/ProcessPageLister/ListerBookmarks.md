# ListerBookmarks

Source: `wire/modules/Process/ProcessPageLister/ListerBookmarks.php`


## typePublic

Indicates public bookmark stored in module settings

## typeOwned

Indicates user-owned bookmark stored in user meta data

## __construct()

Construct

@param Page $page

@param User $user

## setPage()

Set the Lister page that bookmarks will be for

@param Page $page

## setUser()

Set user that bookmarks will be for

@param User $user

## getOwnedBookmarks()

Get owned bookmarks

@param int $userID

@return array

## saveOwnedBookmarks()

Save owned bookmarks

@param array $bookmarks

## getUserSettings()

Get user’s lister settings for current page

@param int $userID

@return array

## saveUserSettings()

Save user settings for current page

@param array $settings

@return bool

## getPublicBookmarks()

Get public bookmarks (from module config)

@return array

## savePublicBookmarks()

Save public bookmarks (to module config)

@param array $bookmarks

@return bool

## saveBookmarks()

Save all bookmarks (whether public or owned)

@param array $allBookmarks

## getAllBookmarks()

Get all bookmarks (public and owned)

@return array

## getBookmarks()

Get configured bookmarks allowed for current user, indexed by bookmark ID (int)

@return array

## getBookmark()

Get a bookmark by ID (whether public or owned)

@param string|int $bookmarkID

@param int|null $type

@return array|null

## getBookmarkUrl()

Get the URL for a bookmark

@param string $bookmarkID

@param User|null $user

@return string

## getBookmarkEditUrl()

Get the URL for a bookmark

@param string $bookmarkID

@return string

## getBookmarkTitle()

Get the title for the given bookmark ID or bookmark array

@param int|array $bookmarkID

@return mixed|string

@throws WireException

## deleteBookmarkByID()

Delete a bookmark by ID

@param int $bookmarkID

@return bool

## filterBookmarksByType()

Filter bookmarks, removing those that are not of the requested type

@param array $allBookmarks

@param int $type

@return array

## filterBookmarksByAccess()

Filter bookmarks, removing those user does not have access to

@param array $bookmarks

@return array

## isBookmarkEditable()

Is the given bookmark editable?

@param array $bookmark

@return bool

## isBookmarkViewable()

Is the given bookmark viewable?

@param array $bookmark

@return bool

## isBookmarkDeletable()

Is the given bookmark deletable?

@param array $bookmark

@return bool

## _bookmark()

Get a template array for a bookmark

@param array $bookmark

@return array

## _bookmarkID()

Sanitize a bookmark ID

@param string|array $bookmarkID

@return string

## intID()

Given an id or string key, return an int ID

@param string|int $val

@return int

## strID()

Given an id or string key, return an string ID (with leading underscore)

@param string|int $val

@return int

## bookmarkStrID()

Given an id or string key, return an bookmark string ID

@param string|int $val

@param int $type

@return int

## isID()

Does the given string value represent an ID? If yes, return ID, otherwise return false.

@param string $val

@return bool|int

## idType()

Get the type from the given id string

@param string $val

@return int

## typePrefix()

Get the prefix for the given bookmark type

@param int $type

@return string

## isValidPageKey()

Is the given page ID or key valid and existing?

@param int|string $val

@return bool

## readableBookmarkSelector()

Return a readable selector from bookmark for output purposes

@param array $bookmark

@return string
