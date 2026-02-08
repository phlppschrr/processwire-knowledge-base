# Notices::move()

Source: `wire/core/Notices.php`

Move notices from one Wire instance to another

@param Wire $from

@param Wire $to

@param array $options Additional options:
 - `types` (array): Types to move (default=['messages','warnings','errors'])
 - `prefix` (string): Optional prefix to add to moved notices text (default='')
 - `suffix` (string): Optional suffix to add to moved notices text (default='')

@return int Number of notices moved
