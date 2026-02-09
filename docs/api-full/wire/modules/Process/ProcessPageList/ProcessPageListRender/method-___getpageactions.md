# $processPageListRender->getPageActions(Page $page): array

Source: `wire/modules/Process/ProcessPageList/ProcessPageListRender.php`

Get an array of available Page actions, indexed by $label => $url

## Usage

~~~~~
// basic usage
$array = $processPageListRender->getPageActions($page);

// usage with all arguments
$array = $processPageListRender->getPageActions(Page $page);
~~~~~

## Arguments

- `$page` `Page`

## Return value

- `array` of $label => $url

## Hooking

- Hookable method name: `getPageActions`
- Implementation: `___getPageActions`
- Hook with: `ProcessPageListRender::getPageActions`

### Hooking Before

~~~~~
$this->addHookBefore('ProcessPageListRender::getPageActions', function(HookEvent $event) {
  $processPageListRender = $event->object;

  // Get arguments
  $page = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('ProcessPageListRender::getPageActions', function(HookEvent $event) {
  $processPageListRender = $event->object;

  // Get arguments
  $page = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
