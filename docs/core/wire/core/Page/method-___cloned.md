# $page->cloned(Page $copy)

Source: `wire/core/Page.php`

Called right after this page has been cloned

## Example

~~~~~
$wire->addHook('Page::cloned', function($e) {
  $page = $e->object;
  $copy = $e->arguments(1);
  $e->log->message("Page $page has been closed to page $copy");
});
~~~~~

## Usage

~~~~~
// basic usage
$result = $page->cloned($copy);

// usage with all arguments
$result = $page->cloned(Page $copy);
~~~~~

## Hookable

- Hookable method name: `cloned`
- Implementation: `___cloned`
- Hook with: `$page->cloned()`

## Arguments

- `$copy` `Page` The new cloned copy of the page

## Since

3.0.253
