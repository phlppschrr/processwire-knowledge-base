# $fieldtype->___install()

Source: `wire/core/Fieldtype.php`

Install this Fieldtype, consistent with optional Module interface

- Called once at time of installation by Modules::install().
- If custom Fieldtype classes need to perform any setup beyond that performed in ___createTable(),
  this method is where they should do it. This is not required, and probably not applicable to most.

## Throws

- WireException Should throw an Exception on failure to install
