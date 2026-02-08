# HTMLPurifier_Injector

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Injects tokens into the document while parsing for well-formedness.
This enables "formatter-like" functionality such as auto-paragraphing,
smiley-ification and linkification to take place.

A note on how handlers create changes; this is done by assigning a new
value to the $token reference. These values can take a variety of forms and
are best described HTMLPurifier_Strategy_MakeWellFormed->processToken()
documentation.

@todo Allow injectors to request a re-run on their output. This
      would help if an operation is recursive.

## getRewindOffset()

Retrieves rewind offset, and then unsets it.
@return bool|int

## prepare()

Prepares the injector by giving it the config and context objects:
this allows references to important variables to be made within
the injector. This function also checks if the HTML environment
will work with the Injector (see checkNeeded()).
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@return bool|string Boolean false if success, string of missing needed element/attribute if failure

## checkNeeded()

This function checks if the HTML environment
will work with the Injector: if p tags are not allowed, the
Auto-Paragraphing injector should not be enabled.
@param HTMLPurifier_Config $config
@return bool|string Boolean false if success, string of missing needed element/attribute if failure

## allowsElement()

Tests if the context node allows a certain element
@param string $name Name of element to test for
@return bool True if element is allowed, false if it is not

## forward()

Iterator function, which starts with the next token and continues until
you reach the end of the input tokens.
@warning Please prevent previous references from interfering with this
         functions by setting $i = null beforehand!
@param int $i Current integer index variable for inputTokens
@param HTMLPurifier_Token $current Current token variable.
         Do NOT use $token, as that variable is also a reference
@return bool

## forwardUntilEndToken()

Similar to _forward, but accepts a third parameter $nesting (which
should be initialized at 0) and stops when we hit the end tag
for the node $this->inputIndex starts in.
@param int $i Current integer index variable for inputTokens
@param HTMLPurifier_Token $current Current token variable.
         Do NOT use $token, as that variable is also a reference
@param int $nesting
@return bool

## backward()

Iterator function, starts with the previous token and continues until
you reach the beginning of input tokens.
@warning Please prevent previous references from interfering with this
         functions by setting $i = null beforehand!
@param int $i Current integer index variable for inputTokens
@param HTMLPurifier_Token $current Current token variable.
         Do NOT use $token, as that variable is also a reference
@return bool

## handleText()

Handler that is called when a text token is processed

## handleElement()

Handler that is called when a start or empty token is processed

## handleEnd()

Handler that is called when an end token is processed

## notifyEnd()

Notifier that is called when an end token is processed
@param HTMLPurifier_Token $token Current token variable.
@note This differs from handlers in that the token is read-only
@deprecated
