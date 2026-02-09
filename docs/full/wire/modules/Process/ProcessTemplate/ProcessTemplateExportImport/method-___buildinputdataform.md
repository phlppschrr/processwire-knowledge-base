# $processTemplateExportImport->buildInputDataForm(): InputfieldForm

Source: `wire/modules/Process/ProcessTemplate/ProcessTemplateExportImport.php`

Build Textarea input form to past JSON data into

## Usage

~~~~~
// basic usage
$inputfieldForm = $processTemplateExportImport->buildInputDataForm();
~~~~~

## Hookable

- Hookable method name: `buildInputDataForm`
- Implementation: `___buildInputDataForm`
- Hook with: `$processTemplateExportImport->buildInputDataForm()`

## Hooking Before

~~~~~
$this->addHookBefore('ProcessTemplateExportImport::buildInputDataForm', function(HookEvent $event) {
  $processTemplateExportImport = $event->object;

  // Your code here
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('ProcessTemplateExportImport::buildInputDataForm', function(HookEvent $event) {
  $processTemplateExportImport = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Return value

- `InputfieldForm`
