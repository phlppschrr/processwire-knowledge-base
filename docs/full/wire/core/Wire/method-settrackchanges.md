# Wire::setTrackChanges()

Source: `wire/core/Wire.php`

Turn change tracking ON or OFF

~~~~~
// Enable change tracking
$page->setTrackChanges(true);

// Disable change tracking
$page->setTrackChanges(false);

// Enable change tracking and remember values
$page->setTrackChanges(Wire::trackChangesValues);
$page->setTrackChanges(true);
~~~~~


@param bool|int $trackChanges Specify one of the following:
  - `true` (bool): Enables change tracking.
  - `false` (bool): Disables change tracking
  - `Wire::trackChangesOn` (constant): Enables change tracking (same as specifying boolean true).
  - `Wire::trackChangesValues` (constant): Enables tracking of changed values when change tracking is already on.
    This uses more memory since it keeps previous values, so it is not enabled by default. Once enabled, the
    setting will persist through boolean true|false arguments.

@return $this
