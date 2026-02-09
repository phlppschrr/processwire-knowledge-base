# $page->getLanguages(): PageArray|null

Source: `wire/core/Page.php`

Get languages active for this page and viewable by current user

## Usage

~~~~~
// basic usage
$items = $page->getLanguages();
~~~~~

## Return value

- `PageArray|null` Returns PageArray of languages, or null if language support is not active.
