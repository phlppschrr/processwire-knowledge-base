# $processPageListActions->getExtraActions(Page $page): array

Source: `wire/modules/Process/ProcessPageList/ProcessPageListActions.php`

Get an array of available extra Page actions

$returnValue = [
  'actionName' => [
     'cn' => 'ClassName',
     'name => 'action label',
     'url' => 'URL',
     'ajax' => true
   ],
  'actionName' => [
     …
  ],
];

## Usage

~~~~~
// basic usage
$array = $processPageListActions->getExtraActions($page);

// usage with all arguments
$array = $processPageListActions->getExtraActions(Page $page);
~~~~~

## Hookable

- Hookable method name: `getExtraActions`
- Implementation: `___getExtraActions`
- Hook with: `$processPageListActions->getExtraActions()`

## Hooking Before

~~~~~
$this->addHookBefore('ProcessPageListActions::getExtraActions', function(HookEvent $event) {
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
$this->addHookAfter('ProcessPageListActions::getExtraActions', function(HookEvent $event) {
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
