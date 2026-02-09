# ProcessPageListerBookmarks

Source: `wire/modules/Process/ProcessPageLister/ProcessPageListerBookmarks.php`

Inherits: `Wire`

## Summary

Class ProcessPageListerBookmarks

Common methods:
- [`bookmarks()`](method-bookmarks.md)
- [`setPage()`](method-setpage.md)
- [`setUser()`](method-setuser.md)
- [`buildBookmarkListForm()`](method-buildbookmarklistform.md)
- [`buildBookmarkDeleteForm()`](method-buildbookmarkdeleteform.md)

Helper class for managing ProcessPageLister bookmarks

## Methods
- [`__construct(ProcessPageLister $lister)`](method-__construct.md) Construct
- [`bookmarks(): ListerBookmarks`](method-bookmarks.md)
- [`setPage(Page $page)`](method-setpage.md) Set the Lister page that bookmarks will be for
- [`setUser(User $user)`](method-setuser.md) Set user that bookmarks will be for
- [`buildBookmarkListForm(): InputfieldForm`](method-buildbookmarklistform.md) Build the bookmarks tab and form contained within it
- [`buildBookmarkDeleteForm(int $bookmarkID): InputfieldFieldset`](method-buildbookmarkdeleteform.md) Build form for deleting a bookmark
- [`buildBookmarkEditForm(int $bookmarkID = 0): InputfieldWrapper`](method-buildbookmarkeditform.md) Build the form needed to edit/add bookmarks
- [`executeEditBookmark(): string`](method-executeeditbookmark.md) Implementation for editing a bookmark, URL segment: ./edit-bookmark/?n=bookmarkID
- [`executeSaveBookmark()`](method-executesavebookmark.md) Save a bookmark posted by ./edit-bookmark/
