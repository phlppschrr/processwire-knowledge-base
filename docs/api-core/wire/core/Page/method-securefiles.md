# $page->secureFiles(): bool|null

Source: `wire/core/Page.php`

Does this Page use secure Pagefiles?

See also `$template->pagefileSecure` and `$config->pagefileSecure` which determine the return value.

## Usage

~~~~~
// basic usage
$bool = $page->secureFiles();
~~~~~

## Return value

- `bool|null` Returns boolean true if yes, false if no, or null if not known

## Since

3.0.166
