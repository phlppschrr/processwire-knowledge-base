# $page->addUrl($url, $language = null): bool

Source: `wire/core/Page.php`

Add a new URL that redirects to this page and save immediately (returns false if already taken).

## Usage

~~~~~
// basic usage
$bool = $page->addUrl($url);

// usage with all arguments
$bool = $page->addUrl($url, $language = null);
~~~~~
