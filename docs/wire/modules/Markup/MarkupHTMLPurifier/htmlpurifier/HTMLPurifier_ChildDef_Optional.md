# HTMLPurifier_ChildDef_Optional

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Definition that allows a set of elements, and allows no children.
@note This is a hack to reuse code from HTMLPurifier_ChildDef_Required,
      really, one shouldn't inherit from the other.  Only altered behavior
      is to overload a returned false with an array.  Thus, it will never
      return false.
