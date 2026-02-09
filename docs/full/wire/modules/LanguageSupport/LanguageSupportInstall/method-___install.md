# $languageSupportInstall->install()

Source: `wire/modules/LanguageSupport/LanguageSupportInstall.php`

Install the module and related modules

## Usage

~~~~~
// basic usage
$result = $languageSupportInstall->install();
~~~~~

## Hooking

- Hookable method name: `install`
- Implementation: `___install`
- Hook with: `LanguageSupportInstall::install`

### Hooking Before

~~~~~
$this->addHookBefore('LanguageSupportInstall::install', function(HookEvent $event) {
  $languageSupportInstall = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('LanguageSupportInstall::install', function(HookEvent $event) {
  $languageSupportInstall = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
