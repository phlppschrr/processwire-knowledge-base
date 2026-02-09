# $pagesAccess->updateTemplate(Template $template)

Source: `wire/core/PagesAccess.php`

Update the pages_access table for the given Template

To be called when a `$template->useRoles` property has changed.

## Usage

~~~~~
// basic usage
$result = $pagesAccess->updateTemplate($template);

// usage with all arguments
$result = $pagesAccess->updateTemplate(Template $template);
~~~~~

## Arguments

- `$template` `Template`

## Hooking

- Hookable method name: `updateTemplate`
- Implementation: `___updateTemplate`
- Hook with: `PagesAccess::updateTemplate`

### Hooking Before

~~~~~
$this->addHookBefore('PagesAccess::updateTemplate', function(HookEvent $event) {
  $pagesAccess = $event->object;

  // Get arguments
  $template = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $template);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('PagesAccess::updateTemplate', function(HookEvent $event) {
  $pagesAccess = $event->object;

  // Get arguments
  $template = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
