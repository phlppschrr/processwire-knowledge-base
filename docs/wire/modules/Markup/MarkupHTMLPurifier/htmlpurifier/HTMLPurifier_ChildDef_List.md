# HTMLPurifier_ChildDef_List

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Definition for list containers ul and ol.

What does this do?  The big thing is to handle ol/ul at the top
level of list nodes, which should be handled specially by /folding/
them into the previous list node.  We generally shouldn't ever
see other disallowed elements, because the autoclose behavior
in MakeWellFormed handles it.
