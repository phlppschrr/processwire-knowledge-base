# HTMLPurifier_ChildDef_Empty

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Definition that disallows all elements.
@warning validateChildren() in this class is actually never called, because
         empty elements are corrected in HTMLPurifier_Strategy_MakeWellFormed
         before child definitions are parsed in earnest by
         HTMLPurifier_Strategy_FixNesting.
