# $process->browserTitle($title): $this

Source: `wire/core/Process.php`

Set the current browser title tag

## Example

~~~~~
$this->browserTitle("Hello World");
~~~~~

## Usage

~~~~~
// basic usage
$result = $process->browserTitle($title);
~~~~~

## Arguments

- `$title` `string`

## Return value

- `$this`

## Hooking

- Hookable method name: `browserTitle`
- Implementation: `___browserTitle`
- Hook with: `Process::browserTitle`

### Hooking Before

~~~~~
$this->addHookBefore('Process::browserTitle', function(HookEvent $event) {
  $process = $event->object;

  // Get arguments
  $title = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $title);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Process::browserTitle', function(HookEvent $event) {
  $process = $event->object;

  // Get arguments
  $title = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
