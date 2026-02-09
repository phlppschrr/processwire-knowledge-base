# $wireFileTools->include($filename, array $vars = array(), array $options = array()): bool

Source: `wire/core/WireFileTools.php`

Include a PHP file passing it all API variables and optionally your own specified variables

This is the same as PHP’s `include()` function except for the following:

- It receives all API variables and optionally your custom variables
- If your filename is not absolute, it doesn’t look in PHP’s include path, only in the current dir.
- It only allows including files that are part of the PW installation: templates, core modules or site modules
- It will assume a “.php” extension if filename has no extension.

Note this function produces direct output. To retrieve output as a return value, use the
`$files->render()` function instead.

## Usage

~~~~~
// basic usage
$bool = $wireFileTools->include($filename);

// usage with all arguments
$bool = $wireFileTools->include($filename, array $vars = array(), array $options = array());
~~~~~

## Arguments

- `$filename` `string` Filename to include
- `$vars` (optional) `array` Optional variables you want to hand to the include (associative array)
- `$options` (optional) `array` Array of options to modify behavior: - `func` (string): Function to use: include, include_once, require or require_once (default=include) - `autoExtension` (string): Extension to assume when no ext in filename, make blank for no auto assumption (default=php) - `allowedPaths` (array): Array of start paths include files are allowed from. Note current dir is always allowed.

## Return value

- `bool` Always returns true

## Hooking

- Hookable method name: `include`
- Implementation: `___include`
- Hook with: `WireFileTools::include`

### Hooking Before

~~~~~
$this->addHookBefore('WireFileTools::include', function(HookEvent $event) {
  $wireFileTools = $event->object;

  // Get arguments
  $filename = $event->arguments(0);
  $vars = $event->arguments(1);
  $options = $event->arguments(2);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $filename);
  $event->arguments(1, $vars);
  $event->arguments(2, $options);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('WireFileTools::include', function(HookEvent $event) {
  $wireFileTools = $event->object;

  // Get arguments
  $filename = $event->arguments(0);
  $vars = $event->arguments(1);
  $options = $event->arguments(2);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Exceptions

- `WireException` if file doesn’t exist or is not allowed
