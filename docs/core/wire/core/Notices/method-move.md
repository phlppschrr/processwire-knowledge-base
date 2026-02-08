# $notices->move(Wire $from, Wire $to, array $options = array()): int

Source: `wire/core/Notices.php`

Move notices from one Wire instance to another

## Arguments

- `$from` `Wire`
- `$to` `Wire`
- `$options` (optional) `array` Additional options: - `types` (array): Types to move (default=['messages','warnings','errors']) - `prefix` (string): Optional prefix to add to moved notices text (default='') - `suffix` (string): Optional suffix to add to moved notices text (default='')

## Return value

int Number of notices moved
