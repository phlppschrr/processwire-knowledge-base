# WireTextTools::getWordAlternates()

Source: `wire/core/WireTextTools.php`

Get alternate words for given word

This method does not do anything unless an implementation is provided by a module (or something else)
hooking the protected `WireTextTools::wordAlternates($word, $options)` method. Implementation should
populate $event->return with any or all of the following (as available):

- Word plural(s)
- Word singular(s)
- Word Lemmas
- Word Synonyms
- Anything else applicable to current $user->language

See the protected WireTextTools::wordAlternates() method for hook instructions and an example.

@param string $word

@param array $options
 - `operator` (string): Operator being used, if applicable (default='')
 - `minLength` (int): Minimum word length to return in alternates (default=2)
 - `lowercase` (bool): Convert words to lowercase, if not already (default=false)

@return array

@since 3.0.162

@see WireTextTools::getWordStem()
