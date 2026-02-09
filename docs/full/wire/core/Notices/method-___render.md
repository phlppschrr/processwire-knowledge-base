# $notices->render(array $options = []): string

Source: `wire/core/Notices.php`

Render these notices as HTML

## Usage

~~~~~
// basic usage
$string = $notices->render();

// usage with all arguments
$string = $notices->render(array $options = []);
~~~~~

## Hookable

- Hookable method name: `render`
- Implementation: `___render`
- Hook with: `$notices->render()`

## Hooking Before

~~~~~
$this->addHookBefore('Notices::render', function(HookEvent $event) {
  $notices = $event->object;

  // Get arguments
  $options = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $options);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Notices::render', function(HookEvent $event) {
  $notices = $event->object;

  // Get arguments
  $options = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$options` (optional) `array` - `groupByType` (bool): Group notices by type? (default=true) - `messageClass` (string): Class for messages (default=NoticeMessage) - `messageIcon` (string): Default icon to show with notices (default: check-square) - `warningClass` (string): Class for warnings (default=NoticeWarning) - `warningIcon` (string): Default icon to show with warnings (default=exclamation-circle) - `errorClass` (string): Class for errors (default=NoticeError) - `errorIcon` (string): Default icon to show with errors (default=exclamation-triangle) - `debugClass` (string): Class for debug items (default=NoticeDebug) - `debugIcon` (string): Default icon for debug notices (default=bug) - `closeClass` (string): Class for close-notices link (default=pw-notice-remove) - `closeIcon` (string): 'Icon for close notices link (default=times) - `listMarkup` (string): List markup (default=`<ul class='pw-notices'>{out}</ul>`) - `itemMarkup` (string): Item markup (default=`<li class='{class}'><div>{remove}{icon}{text}</div></li>`)

## Return value

- `string`

## Since

3.0.254
