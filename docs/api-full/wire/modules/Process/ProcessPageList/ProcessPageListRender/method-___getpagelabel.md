# $processPageListRender->getPageLabel(Page $page, array $options = array()): string

Source: `wire/modules/Process/ProcessPageList/ProcessPageListRender.php`

Return the Page's label text, whether that originates from the Page's name, headline, title, etc.

## Usage

~~~~~
// basic usage
$string = $processPageListRender->getPageLabel($page);

// usage with all arguments
$string = $processPageListRender->getPageLabel(Page $page, array $options = array());
~~~~~

## Arguments

- `$page` `Page`
- `$options` (optional) `array` - `noTags` (bool): If true, HTML will be excluded [other than for icon] in returned text value (default=false) - `noIcon` (bool): If true, icon markup will be excluded from returned value (default=false)

## Return value

- `string`

## Hooking

- Hookable method name: `getPageLabel`
- Implementation: `___getPageLabel`
- Hook with: `ProcessPageListRender::getPageLabel`

### Hooking Before

~~~~~
$this->addHookBefore('ProcessPageListRender::getPageLabel', function(HookEvent $event) {
  $processPageListRender = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $options = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
  $event->arguments(1, $options);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('ProcessPageListRender::getPageLabel', function(HookEvent $event) {
  $processPageListRender = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $options = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
