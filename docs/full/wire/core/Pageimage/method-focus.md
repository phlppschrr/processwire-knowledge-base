# $pageimage->focus($top = null, $left = null, $zoom = null): array|bool|Pageimage

Source: `wire/core/Pageimage.php`

Get or set focus area for crops to use

These settings are used by $this->size() calls that specify BOTH width AND height. Focus helps to
ensure that the important subject of the photo is not cropped out when the requested size proportion
differs from the original image proportion. For example, not chopping off someone’s head in a photo.

Default behavior is to return an array containing "top" and "left" indexes, representing percentages
from top and left. When arguments are specified, you are either setting the top/left percentages, or
unsetting focus, or getting focus in different ways, described in arguments below.

A zoom argument/property is also present here for future use, but not currently supported.

## Arguments

- `$top` (optional) `null|float|int|array|false` Omit to get focus array, or specify one of the following: - GET: Omit all arguments to get focus array (default behavior). - GET: Specify boolean TRUE to return TRUE if focus data is present or FALSE if not. - GET: Specify integer 1 to make this method return pixel dimensions rather than percentages. - SET: Specify both $top and $left arguments to set (values assumed to be percentages). - SET: Specify array containing "top" and "left" indexes to set (percentages). - SET: Specify array where index 0 is top and index 1 is left (percentages). - SET: Specify string in the format "top left", i.e. "25 70" or "top left zoom", i.e. "25 70 30" (percentages). - SET: Specify CSV key=value string in the format "top=25%, left=70%, zoom=30%" in any order - UNSET: Specify boolean false to remove any focus values.
- `$left` (optional) `null|float|int` Set left value (when $top value is float|int) - This argument is only used when setting focus and should be omitted otherwise.
- `$zoom` (optional) `null|int` Zoom percent (not currently supported)

## Return value

array|bool|Pageimage Returns one of the following: - When getting returns array containing top, left and default properties. - When TRUE was specified for the $top argument, it returns either TRUE (has focus) or FALSE (does not have). - When setting or unsetting returns $this.
