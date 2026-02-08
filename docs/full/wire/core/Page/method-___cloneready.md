# $page->___cloneReady(Page $copy)

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
$result = $page->___cloneReady($copy);

// usage with all arguments
$result = $page->___cloneReady(Page $copy);
~~~~~

## Arguments

- `$copy` `Page` The copy of this page that it will be cloned to

## Since

3.0.253
