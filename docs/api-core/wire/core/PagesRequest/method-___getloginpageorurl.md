# $pagesRequest->getLoginPageOrUrl(?Page $page = null): string|Page|null

Source: `wire/core/PagesRequest.php`

Get login Page object or URL to redirect to for login needed to access given $page

- When a Page is returned, it is suggested the Page be rendered in this request.
- When a string/URL is returned, it is suggested you redirect to it.
- When null is returned no login page or URL could be identified and 404 should render.

## Usage

~~~~~
// basic usage
$string = $pagesRequest->getLoginPageOrUrl();

// usage with all arguments
$string = $pagesRequest->getLoginPageOrUrl(?Page $page = null);
~~~~~

## Arguments

- `$page` (optional) `Page|null` Page that access was requested to or omit to get admin login page

## Return value

- `string|Page|null` Login page object or string w/redirect URL, null if 404

## Hooking

- Hookable method name: `getLoginPageOrUrl`
- Implementation: `___getLoginPageOrUrl`
- Hook with: `PagesRequest::getLoginPageOrUrl`

### Hooking Before

~~~~~
$this->addHookBefore('PagesRequest::getLoginPageOrUrl', function(HookEvent $event) {
  $pagesRequest = $event->object;

  // Get arguments
  $page = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('PagesRequest::getLoginPageOrUrl', function(HookEvent $event) {
  $pagesRequest = $event->object;

  // Get arguments
  $page = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
