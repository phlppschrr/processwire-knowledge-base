# HTMLPurifier_Node

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Abstract base node class that all others inherit from.

Why do we not use the DOM extension?  (1) It is not always available,
(2) it has funny constraints on the data it can represent,
whereas we want a maximally flexible representation, and (3) its
interface is a bit cumbersome.
