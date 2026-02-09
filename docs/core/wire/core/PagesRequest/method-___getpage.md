# $pagesRequest->getPage(array $options = array()): Page|NullPage

Source: `wire/core/PagesRequest.php`

Get the requested page

- Populates identified urlSegments or page numbers to $input.
- Returns NullPage for error, call getResponseCode() and/or getResponseMessage() for details.
- Returned page should be validated with getPageForUser() method before rendering it.
- Call getFile() method afterwards to see if request resolved to file managed by returned page.

## Usage

~~~~~
// basic usage
$page = $pagesRequest->getPage();

// usage with all arguments
$page = $pagesRequest->getPage(array $options = array());
~~~~~

## Hookable

- Hookable method name: `getPage`
- Implementation: `___getPage`
- Hook with: `$pagesRequest->getPage()`

## Hooking Before

~~~~~
$this->addHookBefore('PagesRequest::getPage', function(HookEvent $event) {
  $pagesRequest = $event->object;

  // Get arguments
  $options = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $options);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('PagesRequest::getPage', function(HookEvent $event) {
  $pagesRequest = $event->object;

  // Get arguments
  $options = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$options` (optional) `array`

## Return value

- `Page|NullPage`
