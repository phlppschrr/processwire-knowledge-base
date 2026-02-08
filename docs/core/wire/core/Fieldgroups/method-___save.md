# Fieldgroups::___save()

Source: `wire/core/Fieldgroups.php`

Save the Fieldgroup to DB

If fields were removed from the Fieldgroup, then track them down and remove them from the associated field_* tables

@param Saveable $item Fieldgroup to save

@return bool True on success, false on failure

@throws WireException
