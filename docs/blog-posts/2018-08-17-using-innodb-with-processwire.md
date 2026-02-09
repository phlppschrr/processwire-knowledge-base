# Using InnoDB with ProcessWire

Source: https://processwire.com/blog/posts/using-innodb-with-processwire/

## Sections


## Using InnoDB with ProcessWire

17 August 2018 by Ryan Cramer [ 4 Comments](/blog/posts/using-innodb-with-processwire/#comments)

During most weeks, development time here is focused on the ProcessWire core. This week I've been focused on a client project, developing with ProcessWire, rather than developing it. I think it's important to stay closely connected with doing client work like this—using ProcessWire as a tool, rather than just developing the tool. Though there always ends up being crossover—whenever I use ProcessWire as a tool, there's always the “wouldn't it be fun if…” moments, and corresponding updates to the core ensue. This is how much of ProcessWire was developed early-on, and often still is.

On the particular site I'm working on right now, we are working at a scale where there are several million pieces of data that we have to keep track of, and potentially hundreds of people submitting forms at once that can manipulate that data. So I've had to consider things like competing requests, race conditions, etc. a little more than usual. This is where it starts to matter a little more (or a lot more) what database engine is in place. So while I don't have core updates to discuss this week, I thought it would be worthwhile to write a bit about this topic here.

ProcessWire uses MySQL/MariaDB, and when installing ProcessWire, you have a choice of database engine: MyISAM or InnoDB. The default choice is MyISAM because it's known to work on the broadest amount of servers and MySQL versions. Versions of MySQL prior to 5.6.4 didn't support the kind of [fulltext] indexes with InnoDB that ProcessWire needs. Luckily, those are now pretty old versions of MySQL, and it's pretty likely that your web host will be running newer versions. So we're now in a place where InnoDB might be a better default choice for many of us to make during installation, especially when you might be working at larger scale.


## Why use InnoDB in PW?

I'm going to just focus in on two differences here. There are of course numerous other differences (and you can find them all over), but in my experience, we aren't likely to notice them on as many installations. Whereas, the two items mentioned here are the two most likely to provide immediate benefits in ProcessWire (depending on the case).


### Row locking versus table locking

If there are a lot of updates being made to your site, this is a big one. MyISAM is really optimized for read operations, and not so much for write operations. When selecting data out of the database, it'll make other insert and update operations to any tables wait until the select is done. Likewise, most insert operations and all update operations to a table will make any other select operations wait till they are done. MyISAM locks the entire table for these operations, so nothing else can touch it until the operation is done. So while there might be 100 people hitting your site at once, if both read and write operations are taking place, they are all operating on a single prioritized queue in MySQL, as it relates to each table. If only read operations are taking place, no problem. But if it's a mixture of read and write operations, this is where it can become a bottleneck.

InnoDB on the other hand doesn't lock the entire table, it only locks the row. So if your table has a million rows it in, only one of them needs to be locked at a time (during a write operation), rather than the whole million lot of them. If your website does a lot of data manipulation, like importing data from feeds into pages, while others are browsing the site, chances are you'd see a real performance improvement by using InnoDB as your MySQL database engine. On the other hand, if your site/application is one where a couple people are using the ProcessWire admin to make updates, while the rest of the traffic is largely front-end (read-only) traffic, then it probably won't make that much difference whether you use InnoDB or MyISAM (at least in my experience). But who knows what's down the road? It doesn't hurt to start with InnoDB even if you may not need row-level locking immediately.


### Using transactions

When using InnoDB, you have transaction support, which is something that you don't have in MyISAM. Transactions allow you to make multiple updates and commit them all at once, so that either the entire batch of updates gets committed at the same time, or none of them do.

If you are manipulating pages in ProcessWire and updates on one page are directly tied to updates on another, this is a good use case for transactions. It ensures that your manipulations are all committed together as a group, and there's no chance of some manipulations going in place without the others. While a bit of a contrived example, this may help to demonstrate what I'm talking about:

```
$foo = new Page();
$foo->template = 'basic-page';
$foo->parent = '/';
$foo->name = 'foo';
$foo->save();

$bar = new Page();
$bar->template = 'basic-page';
$bar->parent = '/';
$bar->name = 'bar';
$bar->save();
```

The code above would create two pages under the homepage, /foo/ and /bar/. But let's say that there is already a page named /bar/ there, and it's for something entirely different. We don't want any of the operations above to complete if they can't all complete. Yet if we ran the code above, we'd end up with our /foo/ page getting created, but the code to create our /bar/ page would throw an Exception since there's already some other unrelated page named /bar/ there. So we'd be left with /foo/ and the wrong /bar/, and we've now got a foobar problem.

But what if we did this in a transaction?

```
try {
  $database->beginTransaction();

  $foo = new Page();
  $foo->template = 'basic-page';
  $foo->parent = '/';
  $foo->name = 'foo';
  $foo->save();

  $bar = new Page();
  $bar->template = 'basic-page';
  $bar->parent = '/';
  $bar->name = 'bar';
  $bar->save();

  $database->commit();

} catch(\Exception $e) {
  $database->rollBack();
}
```

With the code above, now our /foo/ page won't get created unless our /bar/ page is also created. If an Exception occurs during the process, everything after our `$database->beginTransaction()` gets rolled-back to the original state, per the `$database->rollBack()` call in our `catch` statement.

Maybe we could solve this other ways, like checking for the existence of /foo/ and /bar/ pages before creating them. The point of this example is simply to demonstrate transactions in the simplest way possible. Despite that, consider this: if your site was handling all kinds of requests with a lot of traffic, it's possible that another /bar/ page could have been created from another request in the time between when you checked for the existence of it, and actually created it. You'd end up with the original problem, your /foo/ page, with the wrong /bar/ page, despite your best efforts—the foobar problem again! As a result, even this simple and contrived example has a use case.

These transactions have been present in ProcessWire’s [$database](http://processwire.com/blog/categories/database/) API variable for as long as the $database API variable has existed, so there's nothing new here. Though if you've not experimented with them before, it's good to know about for when and if the need arises. All that's necessary to use them is that your database engine is InnoDB.

Next time you install a new copy of ProcessWire, consider choosing the InnoDB option for these benefits, and more. If you think you might benefit from InnoDB on an existing installation, and are using MySQL 5.6.4 or newer, you can do so by exporting the database, searching/replacing the "ENGINE=MyISAM" statements with "ENGINE=InnoDB" statements, and then re-importing it. The ProcessDatabaseBackups module can be helpful here. Though be sure to test things out in a development/staging environment ahead of time.

Thanks for reading, have a great weekend and enjoy the [ProcessWire Weeky](http://weekly.pw)!
