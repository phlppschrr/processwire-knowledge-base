# HTMLPurifier_IDAccumulator

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Component of HTMLPurifier_AttrContext that accumulates IDs to prevent dupes
@note In Slashdot-speak, dupe means duplicate.
@note The default constructor does not accept $config or $context objects:
      use must use the static build() factory method to perform initialization.

## add()

Add an ID to the lookup table.
@param string $id ID to be added.
@return bool status, true if success, false if there's a dupe

## load()

Load a list of IDs into the lookup table
@param $array_of_ids Array of IDs to load
@note This function doesn't care about duplicates
