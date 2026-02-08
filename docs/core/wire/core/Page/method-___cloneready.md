# $page->___cloneReady(Page $copy)

Source: `wire/core/Page.php`

Called right before this page is cloned

~~~~~
$wire->addHook('Page::cloneReady', function($e) {
 $page = $e->object;
 $e->log->message("Page $page is ready to be cloned");
});
~~~~~

## Arguments

- Page $copy The copy of this page that it will be cloned to

## Meta

- @since 3.0.253
