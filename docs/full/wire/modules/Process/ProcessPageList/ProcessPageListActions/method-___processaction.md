# $processPageListActions->processAction(Page $page, $action): array

Source: `wire/modules/Process/ProcessPageList/ProcessPageListActions.php`

Process action

## Usage

~~~~~
// basic usage
$array = $processPageListActions->processAction($page, $action);

// usage with all arguments
$array = $processPageListActions->processAction(Page $page, $action);
~~~~~

## Hookable

- Hookable method name: `processAction`
- Implementation: `___processAction`
- Hook with: `$processPageListActions->processAction()`

## Hooking Before

~~~~~
$this->addHookBefore('ProcessPageListActions::processAction', function(HookEvent $event) {
  $processPageListActions = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $action = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
  $event->arguments(1, $action);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('ProcessPageListActions::processAction', function(HookEvent $event) {
  $processPageListActions = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $action = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$page` `Page`
- `$action` `string`

## Return value

- `array`

## Exceptions

- `WireException`
