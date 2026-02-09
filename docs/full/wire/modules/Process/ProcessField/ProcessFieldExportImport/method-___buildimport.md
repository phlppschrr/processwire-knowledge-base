# $processFieldExportImport->buildImport(): InputfieldForm

Source: `wire/modules/Process/ProcessField/ProcessFieldExportImport.php`

Execute import

## Usage

~~~~~
// basic usage
$inputfieldForm = $processFieldExportImport->buildImport();
~~~~~

## Return value

- `InputfieldForm`

## Hooking

- Hookable method name: `buildImport`
- Implementation: `___buildImport`
- Hook with: `ProcessFieldExportImport::buildImport`

### Hooking Before

~~~~~
$this->addHookBefore('ProcessFieldExportImport::buildImport', function(HookEvent $event) {
  $processFieldExportImport = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('ProcessFieldExportImport::buildImport', function(HookEvent $event) {
  $processFieldExportImport = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Exceptions

- `WireException` if given invalid import data
