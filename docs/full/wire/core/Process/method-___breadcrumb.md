# $process->breadcrumb($href, $label): $this

Source: `wire/core/Process.php`

Add a breadcrumb

## Example

~~~~~
$this->breadcrumb("../", "Widgets");
~~~~~

## Usage

~~~~~
// basic usage
$result = $process->breadcrumb($href, $label);
~~~~~

## Hookable

- Hookable method name: `breadcrumb`
- Implementation: `___breadcrumb`
- Hook with: `$process->breadcrumb()`

## Hooking Before

~~~~~
$this->addHookBefore('Process::breadcrumb', function(HookEvent $event) {
  $process = $event->object;

  // Get arguments
  $href = $event->arguments(0);
  $label = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $href);
  $event->arguments(1, $label);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Process::breadcrumb', function(HookEvent $event) {
  $process = $event->object;

  // Get arguments
  $href = $event->arguments(0);
  $label = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$href` `string` URL of breadcrumb
- `$label` `string` Label for breadcrumb

## Return value

- `$this`
