# $notices->___render(array $options = []): string

Source: `wire/core/Notices.php`

Render these notices as HTML

## Arguments

- `$options` (optional) `array` - `groupByType` (bool): Group notices by type? (default=true) - `messageClass` (string): Class for messages (default=NoticeMessage) - `messageIcon` (string): Default icon to show with notices (default: check-square) - `warningClass` (string): Class for warnings (default=NoticeWarning) - `warningIcon` (string): Default icon to show with warnings (default=exclamation-circle) - `errorClass` (string): Class for errors (default=NoticeError) - `errorIcon` (string): Default icon to show with errors (default=exclamation-triangle) - `debugClass` (string): Class for debug items (default=NoticeDebug) - `debugIcon` (string): Default icon for debug notices (default=bug) - `closeClass` (string): Class for close-notices link (default=pw-notice-remove) - `closeIcon` (string): 'Icon for close notices link (default=times) - `listMarkup` (string): List markup (default=`<ul class='pw-notices'>{out}</ul>`) - `itemMarkup` (string): Item markup (default=`<li class='{class}'><div>{remove}{icon}{text}</div></li>`)

## Return value

string

## Since

3.0.254
