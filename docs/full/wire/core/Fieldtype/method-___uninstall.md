# Fieldtype::___uninstall()

Source: `wire/core/Fieldtype.php`

Uninstall this Fieldtype, consistent with optional Module interface

- Checks to make sure it's safe to uninstall this Fieldtype. If not, throw an Exception indicating such.
- It's safe to uninstall a Fieldtype only if it's not being used by any Fields.
- If a Fieldtype overrides this to perform additional uninstall functions, it would be good to call this
  parent uninstall method first to make sure uninstall is okay.


@throws WireException Should throw an Exception if uninstall can't be completed.
