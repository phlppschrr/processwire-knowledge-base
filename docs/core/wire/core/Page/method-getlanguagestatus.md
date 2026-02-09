# $page->getLanguageStatus($language = []): array|bool

Source: `wire/core/Page.php`

Get active status for language(s). If given a $language (Language or name of language) it returns a boolean. If given multiple language names (array), or argument omitted, it returns array like `[ 'default' => true, 'fr' => false ];`. @since 3.0.236

## Usage

~~~~~
// basic usage
$array = $page->getLanguageStatus();

// usage with all arguments
$array = $page->getLanguageStatus($language = []);
~~~~~
