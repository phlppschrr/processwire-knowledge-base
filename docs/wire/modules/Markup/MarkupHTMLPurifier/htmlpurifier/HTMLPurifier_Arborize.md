# HTMLPurifier_Arborize

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Converts a stream of HTMLPurifier_Token into an HTMLPurifier_Node,
and back again.

@note This transformation is not an equivalence.  We mutate the input
token stream to make it so; see all [MUT] markers in code.
