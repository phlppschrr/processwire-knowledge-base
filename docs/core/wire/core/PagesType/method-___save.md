# $pagesType->save(Page $page): bool

Source: `wire/core/PagesType.php`

Save a page object and its fields to database.

- This is the same as calling $page->save()
- If the page is new, it will be inserted. If existing, it will be updated.
- If you want to just save a particular field in a Page, use `$page->save($fieldName)` instead.

Hook note:
If you want to hook this method, please hook the `saveReady`, `saved`, or one of
the `Pages::save*` methods instead, as hooking this method will not hook relevant pages
saved directly through $pages->save().

## Usage

~~~~~
// basic usage
$bool = $pagesType->save($page);

// usage with all arguments
$bool = $pagesType->save(Page $page);
~~~~~

## Hookable

- Hookable method name: `save`
- Implementation: `___save`
- Hook with: `$pagesType->save()`

## Hooking Before

~~~~~
$this->addHookBefore('PagesType::save', function(HookEvent $event) {
  $pagesType = $event->object;

  // Get arguments
  $page = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('PagesType::save', function(HookEvent $event) {
  $pagesType = $event->object;

  // Get arguments
  $page = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$page` `Page`

## Return value

- `bool` True on success

## Exceptions

- `WireException`
