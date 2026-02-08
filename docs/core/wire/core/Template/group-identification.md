# Template: identification

Source: `wire/core/Template.php`

@property int $id Numeric database ID.

@property string $name Name of template.

@property string $label Optional short text label to describe Template.

@property int $flags Flags (bitmask) assigned to this template. See the flag constants.

@property string $ns Namespace found in the template file, or blank if not determined.

@property string $pageClass Class for instantiated page objects. Page assumed if blank, or specify class name.
