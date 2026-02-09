# $process->installPage($name = '', $parent = null, $title = '', $template = 'admin', $extras = array()): Page

Source: `wire/core/Process.php`

Install a dedicated page for this Process module and assign it this Process

To be called by Process module's ___install() method.

## Usage

~~~~~
// basic usage
$page = $process->installPage();

// usage with all arguments
$page = $process->installPage($name = '', $parent = null, $title = '', $template = 'admin', $extras = array());
~~~~~

## Hookable

- Hookable method name: `installPage`
- Implementation: `___installPage`
- Hook with: `$process->installPage()`

## Hooking Before

~~~~~
$this->addHookBefore('Process::installPage', function(HookEvent $event) {
  $process = $event->object;

  // Get arguments
  $name = $event->arguments(0);
  $parent = $event->arguments(1);
  $title = $event->arguments(2);
  $template = $event->arguments(3);
  $extras = $event->arguments(4);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $name);
  $event->arguments(1, $parent);
  $event->arguments(2, $title);
  $event->arguments(3, $template);
  $event->arguments(4, $extras);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Process::installPage', function(HookEvent $event) {
  $process = $event->object;

  // Get arguments
  $name = $event->arguments(0);
  $parent = $event->arguments(1);
  $title = $event->arguments(2);
  $template = $event->arguments(3);
  $extras = $event->arguments(4);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$name` (optional) `string` Desired name of page, or omit (or blank) to use module name
- Page|string|int|null Parent for the page, with one of the following: - name of parent, relative to admin root, i.e. "setup" - Page object of parent - path to parent - parent ID - Or omit and admin root is assumed
- `$title` (optional) `string` Omit or blank to pull title from module information
- string|Template Template to use for page (omit to assume 'admin')
- `$extras` (optional) `array` Any extra properties to assign (like status)

## Return value

- `Page` Returns the page that was created

## Exceptions

- `WireException` if page can't be created
