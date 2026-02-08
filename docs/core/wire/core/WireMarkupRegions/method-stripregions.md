# WireMarkupRegions::stripRegions()

Source: `wire/core/WireMarkupRegions.php`

Strip the given region non-nested tags from the document

Note that this only works on non-nested tags like HTML comments, script or style tags.

@param string $tag Specify "<!--" to remove comments or "<script" to remove scripts, or "<tag" for any other tags.

@param string $markup Markup to remove the tags from

@param bool $getRegions Specify true to return array of the strip regions rather than the updated markup

@return string|array
