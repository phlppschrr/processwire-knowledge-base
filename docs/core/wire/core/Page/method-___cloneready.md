# $page->cloneReady(Page $copy)

Source: `wire/core/Page.php`

Called right before this page is cloned

## Example

~~~~~
$wire->addHook('Page::cloneReady', function($e) {
 $page = $e->object;
 $e->log->message("Page $page is ready to be cloned");
});
~~~~~

## Usage

~~~~~
// basic usage
$result = $page->cloneReady($copy);

// usage with all arguments
$result = $page->cloneReady(Page $copy);
~~~~~

## Hookable

- Hookable method name: `cloneReady`
- Implementation: `___cloneReady`
- Hook with: `$page->cloneReady()`

## Arguments

- `$copy` `Page` The copy of this page that it will be cloned to

## Since

3.0.253
