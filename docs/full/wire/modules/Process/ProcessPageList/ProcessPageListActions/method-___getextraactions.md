# $processPageListActions->___getExtraActions(Page $page): array

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

## Arguments

- Page $page

## Return value

array of $label => $url
