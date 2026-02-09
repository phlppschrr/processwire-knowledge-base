# $templates->getNumPages(Template $tpl): int

Source: `wire/core/Templates.php`

Return the number of pages using the provided Template

## Usage

~~~~~
// basic usage
$int = $templates->getNumPages($tpl);

// usage with all arguments
$int = $templates->getNumPages(Template $tpl);
~~~~~

## Arguments

- `$tpl` `Template` Template you want to get count for

## Return value

- `int` Total number of pages in use by given Template
