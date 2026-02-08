# $inputfield->renderReady(?Inputfield $parent = null, $renderValueMode = false): bool

Source: `wire/core/Inputfield.php`

Method called right before Inputfield markup is rendered, so that any dependencies can be loaded as well.

Called before `Inputfield::render()` or `Inputfield::renderValue()` method by the parent `InputfieldWrapper`
instance. If you are calling either of those methods yourself for some reason, make sure that you call this
`renderReady()` method first.

The default behavior of this method is to populate Inputfield-specific CSS and JS file assets into
`$config->styles` and `$config->scripts`.

The return value is true if assets were just added, and false if assets have already been added in a previous
call. This distinction probably doesn't matter in most usages, but here just in case a descending class needs
to know when/if to add additional assets (i.e. when this method returns true).

## Arguments

- Inputfield|null The parent InputfieldWrapper that is rendering it, or null if no parent.
- `$renderValueMode` (optional) `bool` Specify true only if this is for `Inputfield::renderValue()` rather than `Inputfield::render()`.

## Return value

bool True if assets were just added, false if already added.
