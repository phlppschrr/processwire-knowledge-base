# Introduction: Migrations Module

Source: https://processwire.com/blog/posts/introduction-migrations-module/

## Sections


## Introduction: Migrations Module

16 September 2016 by Ryan Cramer [ 6 Comments](/blog/posts/introduction-migrations-module/#comments)

Hey guys, here's Benjamin (LostKobrakai). With Ryan still being on vacation I'll follow up with another guest post for this week.

I'll be talking about the [Migrations](/talk/topic/13045-migrations/) module I release some time ago. I'll give a quick primer on what it does. I'll follow that up with some demo usage and in the end I'll be talking a little bit about what I've planed for the module.


## Introduction

I'm sure most of you know the hassle it can involve to update an already live ProcessWire installation. Initially setting up a locally developed website is quite easily done: Upload the files and clone the database to the live server. But as soon as content is created on that online version and at the same time new features are developed locally those databases get out of sync and when it's time to deploy those changes do need to be merged somehow. The same thing is even more apparent if you're working on a team of developers.

Consider the above scenario. Christine and Jeff are working together on a project and want to merge their changes after finishing their respective work. The workflow without extra tooling would probably be that Christine and Jeff do have to keep track of their changes and then inform each other of them. This is not only a repetitive task but also prone to error especially because of the little mistakes that can happen. If developing a larger feature of a project does take a few weeks of time it's ease for (little) changes to be missed out. The same does apply for a live-server receiving user/editor content and the changes made locally.


### Migrations to the rescue

While it's not possible to avoid the need of keeping track of changes made to the system it can certainly be made a bit more streamlined. Users of one of those various web-frameworks out there probably know the term migrations from database migrations. These are run to setup database tables and their schemas. We can do something similar with the migrations module. We just won't deal with the database directly, this is better left to ProcessWire to care about. We rather want to setup fields, templates or modules. Or we need to run some data conversion on some pages, because e.g. we switched from a single recipient email field to a list of emails.

By having those changes in files we can easily keep track of changes or see what colleagues are up to. The issue of simply forgetting changes is deminished to simply not forgetting to upload the files. For some people this might even be a way to reuse changes between different projects without the need to bundle them in a site profile.

```
class Migration_2015_10_21_12_16 extends Migration {

    public static $description = "Change the blog-post template to use
        it's new alternative template file";

    public function update() {
        $this->insertIntoTemplate('home', 'analytics', 'title');

        $this->editInTemplateContext('home', 'analytics', function($f){
            $f->columnWidth = 50;
        });

        $this->pages->get('/')->setAndSave('analytics', 'UA-XXXXX-XX');
    }

    public function downgrade() {
        $t = $this->templates->get('home');
        $t->fieldgroup->remove('analytics');
        $t->fieldgroup->save();
    }
}
```

Above you can see how such a migration file can look like. It does add the analytics field to the homepage and also fill it with data. But that's not the only thing – it does also remove the field again if a rollback is issued. The ability to rollback migrations might at first seem like wasted time, but it serves two purposes.

- Fast way to undo changes in case something goes south when deploying your code.
- A fast way to iterate on changes. Migrations are run/rolled back in seconds, so it's super easy to e.g. test out if a new setup might behave exactly like before.

There are also some additional classes, which make it a little more easy to setup often needed things in ProcessWire: [FieldMigration, TemplateMigration and ModuleMigration](https://lostkobrakai.github.io/Migrations/examples/#specialized-migration-types). The module does know how to remove those types of data. So extending those classes does allow you to only set the needed properties for those types while the creation and destruction is automatically handled. Also there are some [conveniece helper functions](https://lostkobrakai.github.io/Migrations/#helper-functions) to ease some often needed tasks.


## See it in action

To have the ability to use the cli – without manually installing dependencies – we start of by installing the module through composer. In the console go to your root directory and run `composer require lostkobrakai/migrations:0.2.x-dev`. I've recently decided to switch the cli library, which is not released by now. As soon as it is, you can leave out everything after and including the colon. The examples below already use the new cli syntax, the old one is documented here: [https://lostkobrakai.github.io/Migrations/#cli](https://lostkobrakai.github.io/Migrations/#cli)

Now that all the module files are in the correct place install the module via the admin interface. Also create a new folder at `site/migrations` for your migrations to be stored in.

For the demo I'll replicate the setup of ProcessWire's beginner profile but starting from the blank-profile one. So to work along install a fresh 3.0 installation with the blank profile.


### Add a field

Above I showed you how to create the migration via the admin backend. If you're not scared about using the console – it's faster and I'll use the cli tool in the next examples. So now edit the migration to add all the necessary setting for the body field. Disclaimer: I'm not a vim pro, but I really liked to show not only the code, but also how things are added.

[[asciinema_embed id=ad398yly4pwmnafixqhu63cah]]

With that we’ve build a kind of a blueprint for the body field. That blueprint can now be used to spin up the described field and also to remove it again. Now we can either use the admin backend again to run the migration, but I like to stay in the console for now. The ones of you working with any kind of npm, gulp or other js script will likely have open terminals anyway.

[[asciinema_embed id=5agqv0pxaw9p0y30ltdju6uhy]]

Now to save some time (and space), I'll just link to the recording of me creating and adding all the other fields setup data: [https://asciinema.org/a/22pwr2mvbignbuulzzewwga23](https://asciinema.org/a/22pwr2mvbignbuulzzewwga23) And the migration of those: [https://asciinema.org/a/amsqijnfiopgjrgf6qm7n9gty](https://asciinema.org/a/amsqijnfiopgjrgf6qm7n9gty)


### The templates

With all the fields created we’re going to add those fields to their templates. The first two we need are already installed by the blank profile: home & basic-page. As those will also get the same fields assigned it’s the simplest to use just a single migration file. As we’ll edit already existing items we’ll use default migrations.

[[asciinema_embed id=90x6qk486e1at8dyp0vypz3cw]]

(Let’s see if you can spot the typo in the code =)

The other template's I've created by using the convenient TemplateMigrations. You can again watch that here: [https://asciinema.org/a/cmik6uio1ny04iz6lyorudt4b ](https://asciinema.org/a/cmik6uio1ny04iz6lyorudt4b) And to show off the migration process in the admin backend as well:


## Future Ideas

I can see that creating those migrations does initially require a good amount of knowledge about the ProcessWire API – and not the one, which is well documented. I also had a few requests to allow fields and templates to be exported from the backend directly. It does sound like a good idea, but there is a big caveat. Exporting would only allow the current state of e.g. a field to be exported, but not only the single change you made to a field. Therefore my idea is rather to expand the [documentation](https://lostkobrakai.github.io/Migrations/) for the module. Having example migrations for all the core fieldtypes and for templates would probably easy the burden of entry considerably. So you guys can simple lookup the settings you need if you're not experience enough to look in directly in the codebase. Maybe the effort can also be made available via the [3.0 api docs](../api-full/index.md).

For more information on the module see the [documentation](https://lostkobrakai.github.io/Migrations/) or the [forum topic](/talk/topic/13045-migrations/#comment-118150). Also feel free to ask on the forums if you've questions regarding the module. I'd really like to know more about what people think of it.

To finish up I'll wish you all a nice weekend and a great week until Ryan will be back with the new blogpost.
