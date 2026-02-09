# $pagefileExtra->noCacheURL($http = false): string

Source: `wire/core/PagefileExtra.php`

Get cache busted URL

## Usage

~~~~~
// basic usage
$string = $pagefileExtra->noCacheURL();

// usage with all arguments
$string = $pagefileExtra->noCacheURL($http = false);
~~~~~

## Hookable

- Hookable method name: `noCacheURL`
- Implementation: `___noCacheURL`
- Hook with: `$pagefileExtra->noCacheURL()`

## Hooking Before

~~~~~
$this->addHookBefore('PagefileExtra::noCacheURL', function(HookEvent $event) {
  $pagefileExtra = $event->object;

  // Get arguments
  $http = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $http);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('PagefileExtra::noCacheURL', function(HookEvent $event) {
  $pagefileExtra = $event->object;

  // Get arguments
  $http = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$http` (optional) `bool`

## Return value

- `string`

## Since

3.0.194
