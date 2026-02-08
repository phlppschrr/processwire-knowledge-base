# $inputfieldWrapper->insertBefore($item, $existingItem): $this

Source: `wire/core/InputfieldWrapper.php`

Insert one Inputfield before one that’s already there.

Note: string or array values for either argument require 3.0.196+.

~~~~~
// example 1: Get existing Inputfields and insert first_name before last_name
$firstName = $form->getByName('first_name');
$lastName = $form->getByName('last_name');
$form->insertBefore($firstName, $lastName);

// example 2: Same as above but use Inputfield names (3.0.196+)
$form->insertBefore('first_name', 'last_name');

// example 3: Create new Inputfield and insert before last_name (3.0.196+)
$form->insertBefore([ 'type' => 'text', 'name' => 'first_name' ], 'last_name');
~~~~~

## Arguments

- Inputfield|array|string $item Item to insert
- Inputfield|string $existingItem Existing item you want to insert before.

## Return value

$this
