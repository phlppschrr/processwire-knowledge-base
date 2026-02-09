# $inputfieldPageTableAjax->sortItems(Page $page, Field $field, $sort)

Source: `wire/modules/Inputfield/InputfieldPageTable/InputfieldPageTableAjax.php`

Update items to make sure they are in same order specified in GET var InputfieldPageTableSort

## Usage

~~~~~
// basic usage
$result = $inputfieldPageTableAjax->sortItems($page, $field, $sort);

// usage with all arguments
$result = $inputfieldPageTableAjax->sortItems(Page $page, Field $field, $sort);
~~~~~

## Arguments

- `$page` `Page`
- `$field` `Field`
- `$sort` `string` CSV string
