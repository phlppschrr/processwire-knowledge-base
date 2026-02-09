# $pagesVersions->allowPageVersions(Page $page): bool

Source: `wire/modules/Pages/PagesVersions/PagesVersions.module.php`

Is given page allowed to have versions?

## Usage

~~~~~
// basic usage
$bool = $pagesVersions->allowPageVersions($page);

// usage with all arguments
$bool = $pagesVersions->allowPageVersions(Page $page);
~~~~~

## Hookable

- Hookable method name: `allowPageVersions`
- Implementation: `___allowPageVersions`
- Hook with: `$pagesVersions->allowPageVersions()`

## Hooking Before

~~~~~
$this->addHookBefore('PagesVersions::allowPageVersions', function(HookEvent $event) {
  $pagesVersions = $event->object;

  // Get arguments
  $page = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('PagesVersions::allowPageVersions', function(HookEvent $event) {
  $pagesVersions = $event->object;

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

- `bool`
