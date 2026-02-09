# $pagesRequest->getClosestPage(): Page|NullPage

Source: `wire/core/PagesRequest.php`

Get closest matching page when getPage() returns an error/NullPage

This is useful for a 404 page to suggest if maybe the user intended a different page
and give them a link to it. For instance, you might have the following code in the
template file used by your 404 page:

## Example

~~~~~
echo "<h1>404 Page Not Found</h1>";
$p = $pages->request()->getClosestPage();
if($p->id) {
  echo "<p>Are you looking for <a href='$p->url'>$p->title</a>?</p>";
}
~~~~~

## Usage

~~~~~
// basic usage
$page = $pagesRequest->getClosestPage();
~~~~~

## Return value

- `Page|NullPage`

## Hooking

- Hookable method name: `getClosestPage`
- Implementation: `___getClosestPage`
- Hook with: `PagesRequest::getClosestPage`

### Hooking Before

~~~~~
$this->addHookBefore('PagesRequest::getClosestPage', function(HookEvent $event) {
  $pagesRequest = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('PagesRequest::getClosestPage', function(HookEvent $event) {
  $pagesRequest = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
