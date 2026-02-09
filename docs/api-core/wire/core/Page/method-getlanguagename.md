# $page->getLanguageName($language = []): array|string

Source: `wire/core/Page.php`

Get page name for language(s). If given a Language object, it returns a string. If given array of language names, or argument omitted, it returns an array like `[ 'default' => 'hello', 'es' => 'hola' ];`. @since 3.0.236

## Usage

~~~~~
// basic usage
$array = $page->getLanguageName();

// usage with all arguments
$array = $page->getLanguageName($language = []);
~~~~~
