# Template: identification

Source: `wire/core/Template.php`

- $id: int Numeric database ID.
- $name: string Name of template.
- $label: string Optional short text label to describe Template.
- $flags: int Flags (bitmask) assigned to this template. See the flag constants.
- $ns: string Namespace found in the template file, or blank if not determined.
- $pageClass: string Class for instantiated page objects. Page assumed if blank, or specify class name.
