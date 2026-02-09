# $pagesType->deleted(Page $page)

Source: `wire/core/PagesType.php`

Hook called when a page and its data have been deleted

## Usage

~~~~~
// basic usage
$result = $pagesType->deleted($page);

// usage with all arguments
$result = $pagesType->deleted(Page $page);
~~~~~

## Hookable

- Hookable method name: `deleted`
- Implementation: `___deleted`
- Hook with: `$pagesType->deleted()`

## Hooking Before

~~~~~
$this->addHookBefore('PagesType::deleted', function(HookEvent $event) {
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
$this->addHookAfter('PagesType::deleted', function(HookEvent $event) {
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

## Since

3.0.128
