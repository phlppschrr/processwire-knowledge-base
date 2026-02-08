# ProcessPageListActions

Source: `wire/modules/Process/ProcessPageList/ProcessPageListActions.php`

Actions manager for ProcessPageList

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## other

@method array getExtraActions(Page $page)

@method array getActions(Page $page)

@method array processAction(Page $page, $action)

## setActionLabels()

Set action labels

@param array $actionLabels Assoc array of [ name => label ]

## setUseTrash()

Set whether or not to use trash

@param bool $useTrash

## ___getActions()

Get an array of available Page actions, indexed by $label => $url

@param Page $page

@return array of $label => $url

## ___getExtraActions()

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

## ___processAction()

Process action

@param Page $page

@param string $action

@return array

@throws WireException
