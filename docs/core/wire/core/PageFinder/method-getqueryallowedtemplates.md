# $pageFinder->getQueryAllowedTemplates(DatabaseQuerySelect $query, $options)

Source: `wire/core/PageFinder.php`

Determine which templates the user is allowed to view

## Usage

~~~~~
// basic usage
$result = $pageFinder->getQueryAllowedTemplates($query, $options);

// usage with all arguments
$result = $pageFinder->getQueryAllowedTemplates(DatabaseQuerySelect $query, $options);
~~~~~

## Arguments

- `$query` `DatabaseQuerySelect`
- `$options` `array`
