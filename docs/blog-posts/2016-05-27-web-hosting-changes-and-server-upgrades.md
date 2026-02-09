# Web hosting changes and server upgrades

Source: https://processwire.com/blog/posts/web-hosting-changes-and-server-upgrades/

## Sections


## Web hosting changes and server upgrades

27 May 2016 by Ryan Cramer [ 10 Comments](/blog/posts/web-hosting-changes-and-server-upgrades/#comments)

**This week our focus was on the server side of things rather than on the code side.** Sometimes you've got to open the hood and change the oil in order to keep things running smoothly. But rather than just changing the oil, we opted to replace the entire car, moving from our compact family sedan to a turbocharged supercar, so to speak. Basically, we've had some major server upgrades this week!


### Server changes

We've been slowly outgrowing our dedicated server at [ServInt](http://servint.com), but I've been reluctant to do much about it because it has been very reliable, and ServInt has been a good fit for us.

Rather than asking for more from ServInt, we've been optimizing the site to get more out of the resources that we had. For example, we use [ProCache](/blog/categories/procache/), which makes a big difference. Plus, in the last year we've added some fairly aggressive .htaccess rules for client side caching, and we've moved delivery of all static assets to Amazon's [CDN](/api/modules/procache/cdn/), CloudFront. This has enabled us to get a lot more out of the server, as pretty much everything but the forums are now delivered via ProCache static HTML files and CloudFront.

Despite all that, we still were getting reports from users about general slowness of the site at times, especially in the forums. And our server load was often higher than it should be, leaving us with little room for handling spikes in traffic. We've had a great server, but we'd outgrown it.


### A call from ServInt

Earlier this month, I got a call from someone at ServInt who asked how we had obtained the server we had with them. I got the impression we had been forgotten for a few years, and re-discovered during a cleanup or something. I told them about ProcessWire and that ServInt had been our hero in supporting our hosting, as they had made a strong commitment to supporting open source back in 2012. But this was no donation, as you are probably very familiar with ServInt from our site (it's been on almost every page displayed in the site since 2012, over roughy 14-million pageviews and 1.5 million users). Many of you reading this learned of ServInt from us and host your web sites there as a result, and we are glad about that. They've been absolutely solid over the 12 years I've had servers there. The fact that they were able to support us, and we were able to support them, has been a great thing.

However, great things don't last forever. It sounds like they've been through some ownership changes (I'm not sure when) and are no longer sponsoring open source projects. The people we established the relationship with are no longer there (as far as I can tell), and it seems we may have been forgotten in the shuffle. They asked that we pay a higher monthly amount, or move the sites somewhere else. No faults there, and it's completely understandable. But we need more resources, and the amount they wanted–while reasonable–was about double what we could budget. Such is the dilemma of a growing open source project.

Despite our great experiences with and fondness for ServInt, there's not a workable match there between cost and resources for our case. Even if they are no longer a good match for us, I still think they are great for most other cases and continue to highly recommend them. ServInt is one of the reasons ProcessWire has been able to grow where it is today and we are hugely thankful for their support all of these years. I believe they still have the best managed VPS products that I've come across. So long as the service, support and reliability remain as great as they have, I will continue to keep my client sites with ServInt.


### IBM Softlayer enters the picture

When it became apparent we had to move, I wasn't quite sure what to do. I get contacts pretty much every week from hosting companies wanting to sponsor, but these are most often the low budget / high volume hosting companies. While the interest is always appreciated, it's just not a good match for us or most of our users. ProcessWire is a tool people use for serious work and big projects, and I want any relationships we establish to be with hosts that also work in this area.

When it comes to questions like these, I'm lucky to know [Jan VandenHengel](/talk/user/3131-jan-v/). He's a good friend that I work with just about every week, as I'm part of the team at [Tripsite](https://www.tripsite.com), a company that he helps to lead. He lives in San Francisco and regularly converses with people from Google, Salesforce and other big players, so I always learn something new when I talk to him. Jan also manages dozens of servers for other enterprise clients and really knows what he's doing in this area. So he was the first person that I talked to about our needs for processwire.com.

Jan keeps a lot of the servers that he manages at [IBM Softlayer](https://www.softlayer.com). They aren't a web host per se, but more of an enterprise infrastructure. This is not a place people go to host their blog, for example. This is a place people go to build the infrastructure to launch the next Facebook or Twitter.

I already had a little familiarity with Softlayer because Tripsite runs on it. And to be honest, it's the fastest server I've ever dealt with, so this is the first thing I asked him about. I explained our budget to him. He said that from a budget perspective, we should probably be looking at Amazon AWS instead, something that he's also an expert in. With AWS, we could spend around $100/month and get something that would serve our resource needs better than the ServInt server we were on. The catch is that this is unmanaged hosting, and you need somebody to set things up and maintain it. Lucky for me Jan was enthusiastic about helping us solve this need.

On a whim, I decided to email Softlayer, just in case. I got a response 15 minutes later, asking me to fill out a form explaining who we were, what we did, and so on. I guess they like us because two days later, I was informed that they would be sponsoring our needs for 1-year. They asked me to go ahead and start configuring a server. How great is that?


### Server specifications

At Softlayer, you pretty much tell them exactly what you need in terms of hardware, and 1-4 hours later, they've got it setup ready for you to use. The trouble is, I didn't know exactly what we needed. Thankfully Jan did. He took a look at our traffic and put together the specs for the server that would enable us to easily accommodate current needs and any spikes in traffic that come up. The specs of the server are:

- **OS:** CentOS7.0-64
- **RAM:** 2x8GB Kingston 8GB DDR3 2rx8
- **Processor:** 3.5GHz Intel Xeon-Haswell (E3-1270-V3-Quadcore)
- **Motherboard:** SuperMicro X10SLH-LN6TF
- **Security Device:** SuperMicro AOM-TPM-9655V
- **Remote Mgmt Card:** Aspeed AST2400 - Onboard
- **Power Supply:** SuperMicro PWS-504P-1R (two of these)
- **Backplane:** SuperMicro BPN-SAS-815TQ
- **Drive Controller:** LSI LSI00451
- **Storage:** 2 x 960GB SanDisk CloudSpeed 1000 SSD in RAID 1 config

So that's the server that the ProcessWire network of sites are now running from. Jan spent much of this week configuring the new server for us. I pretty much just watched and learned. We switched it over on Wednesday. Notice the difference? We sure do. The new server has breathed new life into our site, and made it faster than ever before. In fact, this is now the fastest server I've ever worked with!


### Backups

Jan also devised an awesome backup solution for us that makes use of Amazon S3 and keeps multiple dated copies of the entire server, ready to restore. Here's a little more info about that from Jan:

For live on the fly MySQL backups ProcessWire is now using [Percona XTRABackup](https://www.percona.com/software/mysql-database/percona-xtrabackup). This free DB backup tool makes a working snapshot of a database that can be copied in place on a backup server or in the event of a disaster recovery.

Percona XTRABackup can easily be used on many terabyte size databases running tens of thousands of queries per second. You can view a copy of the shell script utilizing Percona [here](/blog/posts/web-hosting-changes-and-server-upgrades/dbbackup.sh/). Once we have a snapshot of the DB, we use [AWS CLI tools](http://docs.aws.amazon.com/cli/latest/userguide/installing.html) to push zipped tar files of the DB and other key data directories to S3. A very simple version of our S3 backup script (kicked off nightly via cron) is [here](/blog/posts/web-hosting-changes-and-server-upgrades/backup-shell-script/).

If the server were running in AWS we'd probably only do snapshots of the filesystem but as this is a baremetal server inside Softlayer's infrastructure this was not an option. However, even with volume snapshots in AWS pushing tar files is never a bad idea as a fail safe backup.


### DNS

I've typically just used whatever DNS tools came with the domain registrar. But looking back over any outages we've had over the years, at least half of them had to do with DNS outages rather than server outages. The domain registrar DNS servers are always DDOS targets, and since they are essentially free, there's not much fallback. I think we often overlook just how important reliable DNS is. One of the things Jan did is switch our DNS over to Amazon's [Route 53 DNS](https://aws.amazon.com/route53/), which is just about the most geographically diverse, complete and reliable DNS you can get. Granted it's not free, but it's not expensive either. A small price to pay for a lot of insurance.


### CDN

One of the things that Softlayer also provides is a CDN, but we've opted to stick with Amazon's CloudFront for now, as we've been so happy with it over the last year. When it comes to geographic diversity, it's pretty hard to beat Amazon's CDN. Whether using processwire.com from Atlanta, London, San Francisco or Frankfurt, or anywhere else, the assets are delivered to you from a server that's likely just a few miles (ahem, kilometers) from your location. That makes everything so much faster, and ProCache makes it so simple to get going with a CDN.


### SSL

We've also taken this opportunity to purchase a wildcard SSL certificate so that all of the ProcessWire subdomains can support https, rather than just the main site. While we don't have this operational just yet, it should be soon. When we get to that point, we'll be making all of our internal links https links by default.


### Automatic Failover

Something we have planned for the future is an automatic failover should the server ever go down. What that means is that if processwire.com goes down for any reason, the DNS would automatically switch to a duplicate copy of the site running on another server (in this case, at Amazon AWS).

Jan setup just such a fallback for the Tripsite.com server. I'll ask him to explain how it works below:

In my view, Amazon has actually succeeded in making DNS sexy with their Route53 platform. Route53--if properly configured--can play a huge role in managing and distributing the traffic to major web portals. Latency based routing, geo based routing, weighted routing, a combination of all of them...the sky is the limit. You can read more about some of the many features [here](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html).

For [Tripsite.com](https://www.tripsite.com) we make use of one of the simplest and elegant Route53 features--DNS failover. The primary Tripsite server, like the new processwire server, lives in Softlayer. We have a backup mirror of this server running in AWS. This server--DB, code tree, etc--gets fully synced from the master every evening.

Tripsite's DNS is Route53. In this setup we have a health check that checks the uptime of Tripsite.com by loading the home page from 24 locations around the world. If this Route53 health check determines Tripsite primary (hosted in Softlayer) is offline it changes the primary A record to point to the Tripsite AWS instance. The TTL (Time to Live) on the primary A record is only 60 seconds so this change is basically unnoticed by the world.

Besides being awesome for failover, we also use this for upgrades on the primary server. You can, for instance, trick the health check into failing by telling it to load the home page from port 81. Once it fails over to the AWS instance you can do your work on the primary server. When that is done you simply fix the health check, Route53 sees the primary server is back, DNS gets cut back to primary, all is well in the world.


### Wrapping up

We got really lucky having both Jan and Softlayer supporting us this week. We're now running in an entirely new class of server and management. This helps us serve our audience better, and it helps us grow. I've been on Jan's Tripsite team for several years now, and now Jan is part of the ProcessWire team too, as he's going to be helping us maintain the new server going forward. If you see [him](/talk/user/3131-jan-v/) around (like in the forums) be sure to thank him. Likewise, if you ever want to get away from the computer and go on any kind of [bike tour](http://www.tripsite.com/bike/) or maybe a [bike and boat tour in Europe](http://www.tripsite.com/bike-boat/), please support [Tripsite](https://www.tripsite.com) since they support us!

Jan also runs his own consulting business called [Perago Solutions](http://peragosolutions.com/)* where he helps clients devise solutions like the one he did for us. He is an Amazon AWS expert and also works a lot with Salesforce. So if you ever come across a project where you need this level of stuff, I'd definitely recommend checking in with Jan.

*Yes that is the default ProcessWire profile, and yes I am going to be making him a new site. :)


### Next week

With the server situation now figured out, we'll be getting back into the core next week. GitHub issue reports and PRs are starting to build up, so we'll be putting focus there. Horst has also come up with some nice improvements to our ImageSizer engines, so we'll be bringing that in as well. Like most weeks, we should have the next version ready by the end of next week. Remember to read the [ProcessWire Weekly](http://weekly.pw) this weekend, and have a great weekend and week ahead!
