# $languagesPageFieldValue->getStringValue(): string

Source: `wire/modules/LanguageSupport/LanguagesPageFieldValue.php`

Get string value (for hooks)

## Usage

~~~~~
// basic usage
$string = $languagesPageFieldValue->getStringValue();
~~~~~

## Return value

- `string`

## Hooking

- Hookable method name: `getStringValue`
- Implementation: `___getStringValue`
- Hook with: `LanguagesPageFieldValue::getStringValue`

### Hooking Before

~~~~~
$this->addHookBefore('LanguagesPageFieldValue::getStringValue', function(HookEvent $event) {
  $languagesPageFieldValue = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('LanguagesPageFieldValue::getStringValue', function(HookEvent $event) {
  $languagesPageFieldValue = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
