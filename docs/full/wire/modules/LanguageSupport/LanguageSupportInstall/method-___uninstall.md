# $languageSupportInstall->uninstall()

Source: `wire/modules/LanguageSupport/LanguageSupportInstall.php`

Uninstall the module and related modules

## Usage

~~~~~
// basic usage
$result = $languageSupportInstall->uninstall();
~~~~~

## Hooking

- Hookable method name: `uninstall`
- Implementation: `___uninstall`
- Hook with: `LanguageSupportInstall::uninstall`

### Hooking Before

~~~~~
$this->addHookBefore('LanguageSupportInstall::uninstall', function(HookEvent $event) {
  $languageSupportInstall = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('LanguageSupportInstall::uninstall', function(HookEvent $event) {
  $languageSupportInstall = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
