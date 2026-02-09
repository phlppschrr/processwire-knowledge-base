# $page->localPath($language = null): string

Source: `wire/core/Page.php`

Return the page path in the current user's language, or specify $language argument (Language object, name, or ID).

## Usage

~~~~~
// basic usage
$string = $page->localPath();

// usage with all arguments
$string = $page->localPath($language = null);
~~~~~
