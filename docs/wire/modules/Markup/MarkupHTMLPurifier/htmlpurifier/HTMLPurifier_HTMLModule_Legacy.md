# HTMLPurifier_HTMLModule_Legacy

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

XHTML 1.1 Legacy module defines elements that were previously
deprecated.

@note Not all legacy elements have been implemented yet, which
      is a bit of a reverse problem as compared to browsers! In
      addition, this legacy module may implement a bit more than
      mandated by XHTML 1.1.

This module can be used in combination with TransformToStrict in order
to transform as many deprecated elements as possible, but retain
questionably deprecated elements that do not have good alternatives
as well as transform elements that don't have an implementation.
See docs/ref-strictness.txt for more details.
