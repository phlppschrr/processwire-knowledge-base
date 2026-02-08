# HTMLPurifier_HTMLModule_Presentation

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

XHTML 1.1 Presentation Module, defines simple presentation-related
markup. Text Extension Module.
@note The official XML Schema and DTD specs further divide this into
      two modules:
         - Block Presentation (hr)
         - Inline Presentation (b, big, i, small, sub, sup, tt)
      We have chosen not to heed this distinction, as content_sets
      provides satisfactory disambiguation.
