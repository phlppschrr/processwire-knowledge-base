# $page->___cloned(Page $copy)

Source: `wire/core/Page.php`

Called right after this page has been cloned

~~~~~
$wire->addHook('Page::cloned', function($e) {
  $page = $e->object;
  $copy = $e->arguments(1);
  $e->log->message("Page $page has been closed to page $copy");
});
~~~~~

## Arguments

- Page $copy The new cloned copy of the page

## Meta

- @since 3.0.253
