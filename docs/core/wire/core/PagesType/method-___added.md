# $pagesType->added(Page $page)

Source: `wire/core/PagesType.php`

Hook called when a new page of this type has been added

## Usage

~~~~~
// basic usage
$result = $pagesType->added($page);

// usage with all arguments
$result = $pagesType->added(Page $page);
~~~~~

## Hookable

- Hookable method name: `added`
- Implementation: `___added`
- Hook with: `$pagesType->added()`

## Hooking Before

~~~~~
$this->addHookBefore('PagesType::added', function(HookEvent $event) {
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
$this->addHookAfter('PagesType::added', function(HookEvent $event) {
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
