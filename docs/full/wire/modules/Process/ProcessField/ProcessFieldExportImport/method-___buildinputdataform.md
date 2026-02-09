# $processFieldExportImport->buildInputDataForm(): InputfieldForm

Source: `wire/modules/Process/ProcessField/ProcessFieldExportImport.php`

Build Textarea input form to pass JSON data into

## Usage

~~~~~
// basic usage
$inputfieldForm = $processFieldExportImport->buildInputDataForm();
~~~~~

## Return value

- `InputfieldForm`

## Hooking

- Hookable method name: `buildInputDataForm`
- Implementation: `___buildInputDataForm`
- Hook with: `ProcessFieldExportImport::buildInputDataForm`

### Hooking Before

~~~~~
$this->addHookBefore('ProcessFieldExportImport::buildInputDataForm', function(HookEvent $event) {
  $processFieldExportImport = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('ProcessFieldExportImport::buildInputDataForm', function(HookEvent $event) {
  $processFieldExportImport = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
