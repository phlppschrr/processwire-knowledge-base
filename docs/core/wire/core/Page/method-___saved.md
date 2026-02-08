# Page::___saved()

Source: `wire/core/Page.php`

Called right after this Page is saved

Note that if the `$name` argument is populated then only that field/property was saved.
This is different from the `Pages::saved` hookable method, which is only called
when the entire page is saved.

~~~~~
$wire->addHook('Page:saved', function($e) {
  $page = $e->object;
  $changes = $e->arguments(0);
  $name = $e->arguments(1);
  if($name) {
    $e->message("Saved field $name on page $page");
  } else {
    $e->message("Saved page $page: " . implode(', ', $changes));
  }
});
~~~~~


@param array $changes Names of changed field names and/or properties

@param string|false $name Indicates whether entire page was saved or just a field:
 - Populated with `string` field or property name if `$page->save($name)` was used rather than `$page->save();`
 - Populated with `false` if entire page was saved, i.e. `$page->save()`

@since 3.0.253
