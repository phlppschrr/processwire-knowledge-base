# DatabaseQuery

Source: `wire/core/DatabaseQuery.php`

ProcessWire DatabaseQuery

Serves as a base class for other DatabaseQuery classes

The intention behind these classes is to have a query that can safely
be passed between methods and objects that add to it without knowledge
of what other methods/objects have done to it. It also means being able
to build a complex query without worrying about correct syntax placement.

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com

This file is licensed under the MIT license
https://processwire.com/about/license/mit/

Groups:
Group: [other](group-other.md)

Methods:
Method: [__construct()](method-__construct.md)
Method: [bindOption()](method-bindoption.md)
Method: [bindValue()](method-bindvalue.md)
Method: [bindValueGetKey()](method-bindvaluegetkey.md)
Method: [getUniqueBindKey()](method-getuniquebindkey.md)
Method: [getBindValues()](method-getbindvalues.md)
Method: [copyBindValuesTo()](method-copybindvaluesto.md)
Method: [copyTo()](method-copyto.md)
Method: [__call()](method-__call.md)
Method: [__set()](method-__set.md)
Method: [__get()](method-__get.md)
Method: [getQuery()](method-getquery.md)
Method: [getDebugQuery()](method-getdebugquery.md)
Method: [getSQL()](method-getsql.md)
Method: [getQueryMethod()](method-getquerymethod.md)
Method: [prepare()](method-prepare.md)
Method: [prepare()](method-prepare.md)
Method: [pdoParamType()](method-pdoparamtype.md)
Method: [execute()](method-execute.md)
