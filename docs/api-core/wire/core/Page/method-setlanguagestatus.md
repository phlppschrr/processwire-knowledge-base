# $page->setLanguageStatus($language, $status = null): Page

Source: `wire/core/Page.php`

Set active status for language(s), can be called as `$page->setLanguageStatus('es', true);` or `$page->setLanguageStatus([ 'es' => true, 'br' => false ]);` to set multiple. @since 3.0.236

## Usage

~~~~~
// basic usage
$page = $page->setLanguageStatus($language);

// usage with all arguments
$page = $page->setLanguageStatus($language, $status = null);
~~~~~
