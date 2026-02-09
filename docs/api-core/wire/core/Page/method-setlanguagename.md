# $page->setLanguageName($language, $name = null): Page

Source: `wire/core/Page.php`

Set page name for language with `$page->setLanguageName('es', 'hola');` or set multiple with `$page->setLanguageName([ 'default' => 'hello', 'es' => 'hola' ]);` @since 3.0.236

## Usage

~~~~~
// basic usage
$page = $page->setLanguageName($language);

// usage with all arguments
$page = $page->setLanguageName($language, $name = null);
~~~~~
