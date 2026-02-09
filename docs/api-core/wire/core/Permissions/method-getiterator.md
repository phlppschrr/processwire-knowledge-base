# $permissions->getIterator(): array|PageArray|\Traversable

Source: `wire/core/Permissions.php`

Returns all installed Permission pages and enables foreach() iteration of $permissions

## Example

~~~~~
// Example of listing all permissions
foreach($permissions as $permission) {
  echo "<li>$permission->name</li>";
}
~~~~~

## Usage

~~~~~
// basic usage
$array = $permissions->getIterator();
~~~~~

## Return value

- `array|PageArray|\Traversable`
