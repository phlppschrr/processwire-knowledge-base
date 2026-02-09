# PageBookmarks

Source: `wire/modules/Process/ProcessPageEdit/PageBookmarks.php`

Inherits: `Wire`

Class PageBookmarks

Class for managing Page bookmarks, currently used by ProcessPageEdit and ProcessPageList

Methods:
- [`__construct(Process $process)`](method-__construct.md)
- [`initNavJSON(array $options = array()): array`](method-initnavjson.md) Initialize/create the $options array for executeNavJSON() in Process modules
- [`listBookmarks(): string`](method-listbookmarks.md) Render list of current bookmarks
- [`editBookmarksForm(): InputfieldForm`](method-editbookmarksform.md) Provides the editor for bookmarks and returns InputfieldForm
- [`editBookmarks(): string`](method-editbookmarks.md) Provides the editor or list for bookmarks and returns rendered markup
- [`checkProcessPage(Page $page)`](method-checkprocesspage.md) Check and update the given process page for hidden/visible status depending on useBookmarks setting
- [`addConfigInputfields(InputfieldWrapper $inputfields)`](method-addconfiginputfields.md) Populate any configuration inputfields to the given $inputfields wrapper for $process
