# $processTemplateExportImport->buildExport(): InputfieldForm

Source: `wire/modules/Process/ProcessTemplate/ProcessTemplateExportImport.php`

Execute export

## Usage

~~~~~
// basic usage
$inputfieldForm = $processTemplateExportImport->buildExport();
~~~~~

## Return value

- `InputfieldForm`

## Hooking

- Hookable method name: `buildExport`
- Implementation: `___buildExport`
- Hook with: `ProcessTemplateExportImport::buildExport`

### Hooking Before

~~~~~
$this->addHookBefore('ProcessTemplateExportImport::buildExport', function(HookEvent $event) {
  $processTemplateExportImport = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('ProcessTemplateExportImport::buildExport', function(HookEvent $event) {
  $processTemplateExportImport = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
