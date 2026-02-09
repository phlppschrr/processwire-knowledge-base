# $templates->getExportData(Template $template): array

Source: `wire/core/Templates.php`

Export Template data for external use

## Usage

~~~~~
// basic usage
$array = $templates->getExportData($template);

// usage with all arguments
$array = $templates->getExportData(Template $template);
~~~~~

## Arguments

- `$template` `Template` Template you want to export

## Return value

- `array` Associative array of export data

## Hooking

- Hookable method name: `getExportData`
- Implementation: `___getExportData`
- Hook with: `Templates::getExportData`

### Hooking Before

~~~~~
$this->addHookBefore('Templates::getExportData', function(HookEvent $event) {
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
$this->addHookAfter('Templates::getExportData', function(HookEvent $event) {
  $templates = $event->object;

  // Get arguments
  $template = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
