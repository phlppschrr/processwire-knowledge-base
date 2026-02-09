# $page->localName($language = null, $useDefaultWhenEmpty = false): string

Source: `wire/core/Page.php`

Return the page name in the current user’s language, or specify $language argument (Language object, name, or ID), or TRUE to use default page name when blank (instead of 2nd argument).

## Usage

~~~~~
// basic usage
$string = $page->localName();

// usage with all arguments
$string = $page->localName($language = null, $useDefaultWhenEmpty = false);
~~~~~
