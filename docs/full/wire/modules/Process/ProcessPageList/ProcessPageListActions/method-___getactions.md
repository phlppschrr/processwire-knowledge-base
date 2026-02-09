# $processPageListActions->getActions(Page $page): array

Source: `wire/modules/Process/ProcessPageList/ProcessPageListActions.php`

Get an array of available Page actions, indexed by $label => $url

## Usage

~~~~~
// basic usage
$array = $processPageListActions->getActions($page);

// usage with all arguments
$array = $processPageListActions->getActions(Page $page);
~~~~~

## Hookable

- Hookable method name: `getActions`
- Implementation: `___getActions`
- Hook with: `$processPageListActions->getActions()`

## Hooking Before

~~~~~
$this->addHookBefore('ProcessPageListActions::getActions', function(HookEvent $event) {
  $processPageListActions = $event->object;

  // Get arguments
  $page = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('ProcessPageListActions::getActions', function(HookEvent $event) {
  $processPageListActions = $event->object;

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

- `array` of $label => $url
