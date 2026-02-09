# $fieldgroups->getExportData(Fieldgroup $fieldgroup): array

Source: `wire/core/Fieldgroups.php`

Export config data for the given fieldgroup

## Usage

~~~~~
// basic usage
$array = $fieldgroups->getExportData($fieldgroup);

// usage with all arguments
$array = $fieldgroups->getExportData(Fieldgroup $fieldgroup);
~~~~~

## Arguments

- `$fieldgroup` `Fieldgroup`

## Return value

- `array`

## Hooking

- Hookable method name: `getExportData`
- Implementation: `___getExportData`
- Hook with: `Fieldgroups::getExportData`

### Hooking Before

~~~~~
$this->addHookBefore('Fieldgroups::getExportData', function(HookEvent $event) {
  $fieldgroups = $event->object;

  // Get arguments
  $fieldgroup = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $fieldgroup);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Fieldgroups::getExportData', function(HookEvent $event) {
  $fieldgroups = $event->object;

  // Get arguments
  $fieldgroup = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
