# $wireTextTools->___wordAlternates($word, array $options): array

Source: `wire/core/WireTextTools.php`

Hookable method to return alternate words for given word

This hookable method is separate from the public getWordAlternates() method so that
we can provide predictable and already-populated $options to whatever is hooking this, as
as provide some additional QA with the return value from modules/hooks.

It is fine if the return value contains duplicates, the original word, or too-short words,
as the calling getWordAlternates() takes care of those before returning words to user.
Basically, hooks can ignore the `$options` argument, unless they need to know the `operator`,
which may or may not be provided by the caller.

In hook implementation, avoid deleting what’s already present in $event->return just in
case multiple hooks are adding words.

~~~~~
// Contrived example of how to implement
$wire->addHookAfter('WireTextTools::wordAlternates', function(HookEvent $event) {
  $word = $event->arguments(0); // string: word requested alternates for
  $words = $event->return; // array: existing return value

  $cats = [ 'cat', 'cats', 'kitty', 'feline', 'felines' ];
  $dogs = [ 'dog', 'dogs', 'doggy', 'canine', 'canines' ];

  if(in_array($word, $cats)) {
    $words = array_merge($words, $cats);
  } else if(in_array($word, $dogs)) {
    $words = array_merge($words, $dogs);
  }

  $event->return = $words;
});

// Test it out
$words = $sanitizer->getTextTools()->getWordAlternates('cat');
echo implode(', ', $words); // outputs: cats, kitty, kitten, feline, felines
~~~~~

## Arguments

- `$word` `string`
- `$options` `array` - `operator` (string): Operator being used, if applicable (default='')

## Return value

array

## Since

3.0.162
