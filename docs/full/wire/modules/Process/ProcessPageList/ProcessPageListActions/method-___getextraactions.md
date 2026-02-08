# $processPageListActions->getExtraActions(Page $page): array

Source: `wire/modules/Process/ProcessPageList/ProcessPageListActions.php`

Get an array of available extra Page actions

$returnValue = [
  'actionName' => [
     'cn' => 'ClassName',
     'name => 'action label',
     'url' => 'URL',
     'ajax' => true
   ],
  'actionName' => [
     …
  ],
];

## Usage

~~~~~
// basic usage
$array = $processPageListActions->getExtraActions($page);

// usage with all arguments
$array = $processPageListActions->getExtraActions(Page $page);
~~~~~

## Hookable

- Hookable method name: `getExtraActions`
- Implementation: `___getExtraActions`
- Hook with: `$processPageListActions->getExtraActions()`

## Arguments

- `$page` `Page`

## Return value

- `array` of $label => $url
