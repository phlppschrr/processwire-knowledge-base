# $pages->saveReady(Page $page): array

Source: `wire/core/Pages.php`

Hook called just before a page is saved

May be preferable to a before `Pages::save` hook because you know for sure a save will
be executed immediately after this is called. Whereas you don't necessarily know
that when the before `Pages::save` is called, as an error may prevent it.

## Usage

~~~~~
// basic usage
$array = $pages->saveReady($page);

// usage with all arguments
$array = $pages->saveReady(Page $page);
~~~~~

## Hookable

- Hookable method name: `saveReady`
- Implementation: `___saveReady`
- Hook with: `$pages->saveReady()`

## Hooking Before

~~~~~
$this->addHookBefore('Pages::saveReady', function(HookEvent $event) {
  $pages = $event->object;

  // Get arguments
  $page = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Pages::saveReady', function(HookEvent $event) {
  $pages = $event->object;

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

- `array` Optional extra data to add to pages save query, which the hook can populate.

## See Also

- [Pages::savePageOrFieldReady()](method-___savepageorfieldready.md)
- [Pages::saveFieldReady()](method-___savefieldready.md)
