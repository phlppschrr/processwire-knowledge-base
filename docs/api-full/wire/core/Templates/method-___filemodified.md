# $templates->fileModified(Template $template)

Source: `wire/core/Templates.php`

Hook called when a Template detects that its file has changed

Note that the hook is not called until something in the system (like a page render) asks for the template’s filename.
That’s because it would not be efficient for PW to check the file for every template in the system on every request.

## Usage

~~~~~
// basic usage
$result = $templates->fileModified($template);

// usage with all arguments
$result = $templates->fileModified(Template $template);
~~~~~

## Arguments

- `$template` `Template`

## Hooking

- Hookable method name: `fileModified`
- Implementation: `___fileModified`
- Hook with: `Templates::fileModified`

### Hooking Before

~~~~~
$this->addHookBefore('Templates::fileModified', function(HookEvent $event) {
  $templates = $event->object;

  // Get arguments
  $template = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $template);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Templates::fileModified', function(HookEvent $event) {
  $templates = $event->object;

  // Get arguments
  $template = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Since

3.0.141
