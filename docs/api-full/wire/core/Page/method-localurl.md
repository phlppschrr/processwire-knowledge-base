# $page->localUrl($language = null): string

Source: `wire/core/Page.php`

Return the page URL in the current user's language, or specify $language argument (Language object, name, or ID).

## Usage

~~~~~
// basic usage
$string = $page->localUrl();

// usage with all arguments
$string = $page->localUrl($language = null);
~~~~~
