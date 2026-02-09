# $inputfieldTinyMCESettings->prepareSettingsForOutput(array $settings): array

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCESettings.php`

Prepare given settings ready for output

This converts relative URLs to absolute, etc.

## Usage

~~~~~
// basic usage
$array = $inputfieldTinyMCESettings->prepareSettingsForOutput($settings);

// usage with all arguments
$array = $inputfieldTinyMCESettings->prepareSettingsForOutput(array $settings);
~~~~~

## Hookable

- Hookable method name: `prepareSettingsForOutput`
- Implementation: `___prepareSettingsForOutput`
- Hook with: `$inputfieldTinyMCESettings->prepareSettingsForOutput()`

## Hooking Before

~~~~~
$this->addHookBefore('InputfieldTinyMCESettings::prepareSettingsForOutput', function(HookEvent $event) {
  $inputfieldTinyMCESettings = $event->object;

  // Get arguments
  $settings = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $settings);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('InputfieldTinyMCESettings::prepareSettingsForOutput', function(HookEvent $event) {
  $inputfieldTinyMCESettings = $event->object;

  // Get arguments
  $settings = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$settings` `array`

## Return value

- `array`
