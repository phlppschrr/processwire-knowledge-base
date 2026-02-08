# ProcessPageListActions::___getExtraActions()

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

@param Page $page

@return array of $label => $url
