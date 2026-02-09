# $pagesType->saveReady(Page $page): array

Source: `wire/core/PagesType.php`

Hook called just before a page of this type is saved

## Usage

~~~~~
// basic usage
$array = $pagesType->saveReady($page);

// usage with all arguments
$array = $pagesType->saveReady(Page $page);
~~~~~

## Hookable

- Hookable method name: `saveReady`
- Implementation: `___saveReady`
- Hook with: `$pagesType->saveReady()`

## Hooking Before

~~~~~
$this->addHookBefore('PagesType::saveReady', function(HookEvent $event) {
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
$this->addHookAfter('PagesType::saveReady', function(HookEvent $event) {
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

- `$page` `Page` The page about to be saved

## Return value

- `array` Optional extra data to add to pages save query.

## Since

3.0.128
