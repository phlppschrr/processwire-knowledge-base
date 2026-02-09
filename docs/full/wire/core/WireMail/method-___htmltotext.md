# $wireMail->htmlToText($html): string

Source: `wire/core/WireMail.php`

Convert HTML mail body to TEXT mail body

## Usage

~~~~~
// basic usage
$string = $wireMail->htmlToText($html);
~~~~~

## Hookable

- Hookable method name: `htmlToText`
- Implementation: `___htmlToText`
- Hook with: `$wireMail->htmlToText()`

## Hooking Before

~~~~~
$this->addHookBefore('WireMail::htmlToText', function(HookEvent $event) {
  $wireMail = $event->object;

  // Get arguments
  $html = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $html);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('WireMail::htmlToText', function(HookEvent $event) {
  $wireMail = $event->object;

  // Get arguments
  $html = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$html` `string`

## Return value

- `string`
