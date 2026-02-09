# $pagesRequest->getPageForUser(Page $page, User $user): Page|NullPage

Source: `wire/core/PagesRequest.php`

Update/get page for given user

Must be called once the current $user is known as it may change the $page.
Returns NullPage if user lacks access or page out of bounds.
Returns different page if it should be substituted due to lack of access (like login page).

## Usage

~~~~~
// basic usage
$page = $pagesRequest->getPageForUser($page, $user);

// usage with all arguments
$page = $pagesRequest->getPageForUser(Page $page, User $user);
~~~~~

## Arguments

- `$page` `Page`
- `$user` `User`

## Return value

- `Page|NullPage`

## Hooking

- Hookable method name: `getPageForUser`
- Implementation: `___getPageForUser`
- Hook with: `PagesRequest::getPageForUser`

### Hooking Before

~~~~~
$this->addHookBefore('PagesRequest::getPageForUser', function(HookEvent $event) {
  $pagesRequest = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $user = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
  $event->arguments(1, $user);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('PagesRequest::getPageForUser', function(HookEvent $event) {
  $pagesRequest = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $user = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
