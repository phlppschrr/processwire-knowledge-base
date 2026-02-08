# $inputfieldWrapper->insertAfter($item, $existingItem): $this

Source: `wire/core/InputfieldWrapper.php`

Insert one Inputfield after one that’s already there.

Note: string or array values for either argument require 3.0.196+.

~~~~~
// example 1: Get existing Inputfields, insert last_name after first_name
$lastName = $form->getByName('last_name');
$firstName = $form->getByName('first_name');
$form->insertAfter($lastName, $firstName);

// example 2: Same as above but use Inputfield names (3.0.196+)
$form->insertBefore('last_name', 'first_name');

// example 3: Create new Inputfield and insert after first_name (3.0.196+)
$form->insertAfter([ 'type' => 'text', 'name' => 'last_name' ], 'first_name');
~~~~~

## Arguments

- Inputfield|array|string $item Item to insert
- Inputfield|string $existingItem Existing item you want to insert after.

## Return value

$this
