# $page->localHttpUrl($language = null): string

Source: `wire/core/Page.php`

Return the page URL (including scheme and hostname) in the current user's language, or specify $language argument (Language object, name, or ID).

## Usage

~~~~~
// basic usage
$string = $page->localHttpUrl();

// usage with all arguments
$string = $page->localHttpUrl($language = null);
~~~~~
