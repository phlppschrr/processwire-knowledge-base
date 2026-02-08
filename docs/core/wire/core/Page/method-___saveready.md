# $page->___saveReady(array $changes, $name = false)

Source: `wire/core/Page.php`

Called right before this Page is saved

If the `$name` argument is populated then only that field/property will be saved.
But if `$name` is false, then the whole page will be saved, including any
changes in the `$changes` array, and any more you make when this method is called.
This is different from the `Pages::saveReady` hookable method, which is only called
when the entire page is saved.

~~~~~
$wire->addHook('Page:saveReady', function($e) {
  $page = $e->object;
  $name = $e->arguments(1);
  if($name) {
    $e->message("Ready to save field $name on page $page");
  } else {
    $e->message("Ready to save page $page");
  }
});
~~~~~

## Arguments

- array $changes Names of changed field names and/or properties
- string|false $name Indicates whether entire page was saved or just a field/property: - Populated with `string` field or property name if `$page->save($name)` was used rather than `$page->save();` - Populated with `false` if entire page is to be saved, i.e. `$page->save()`

## Meta

- @since 3.0.253
