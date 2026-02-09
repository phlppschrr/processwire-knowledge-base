# $process->headline($headline): $this

Source: `wire/core/Process.php`

Set the current primary headline to appear in the admin interface

## Example

~~~~~
$this->headline("Hello World");
~~~~~

## Usage

~~~~~
// basic usage
$result = $process->headline($headline);
~~~~~

## Hookable

- Hookable method name: `headline`
- Implementation: `___headline`
- Hook with: `$process->headline()`

## Hooking Before

~~~~~
$this->addHookBefore('Process::headline', function(HookEvent $event) {
  $process = $event->object;

  // Get arguments
  $headline = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $headline);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Process::headline', function(HookEvent $event) {
  $process = $event->object;

  // Get arguments
  $headline = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$headline` `string`

## Return value

- `$this`
