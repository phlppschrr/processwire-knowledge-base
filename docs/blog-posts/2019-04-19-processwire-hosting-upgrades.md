# ProcessWire.com website hosting upgrades

Source: https://processwire.com/blog/posts/processwire-hosting-upgrades/

## Sections


## ProcessWire.com website hosting upgrades

19 April 2019 by Ryan Cramer [ 3 Comments](/blog/posts/processwire-hosting-upgrades/#comments)

Quietly and without interruption this week, our whole website (and all subdomains) moved from a single static server to a load-balanced multi-server environment, giving us even more horsepower and redundancy than before!

Hope you all have had a good week. There have been several updates on the dev branch this week, but I’m going to give it another week and some more updates before bumping up the version number and writing more about it. PW has always been one of the most stable CMS projects out there, but we’re consistently working our way to the most stable version of PW ever.

What's also been really stable is our website and the hosting of it. We've not had a single outage in years. Nevertheless, we're always looking for ways to make it even better. Quietly and without interruption this week, the whole website changed to a different server… rather, make that “servers” (plural). We went from a static Amazon/AWS EC2 instance to an Amazon/AWS EBS load balancer setup with automatic failover. We’ve also switched from our existing RDS instance to a new MySQL compatible Aurora cluster RDS database, also running at Amazon/AWS. HTTPS now comes by way of Amazon's enterprise-grade SSL certificates as well. What this all means is that our website has even more horsepower and redundancy than before.

Our transactional email (like that sent from the forums) has now also moved from Sendgrid to Amazon SES. Sendgrid was alright, but Amazon SES is a huge upgrade for our transactional email. We’ve now got the most reliable email system you can get. The nice thing is that Jan set this up at the OS level, so plain old PHP mail() is all it takes from the PHP side. I’m continuing to use Mailgun for our newsletter distribution sent by ProMailer, as I’ve been really happy with how that’s working, and we are also only signed up for transactional email distribution with Amazon SES at present.

All of these great AWS upgrades are thanks to Jan at [Perago Solutions](https://www.peragosolutions.com/) who keeps everything running smoothly here with his AWS expertise. As many of you know, he also managed our Softlayer setup prior to our AWS switchover more than a year ago. While our setup is pretty small scale relative to most of the clients Jan works with, I feel it’s a huge benefit for the ProcessWire project to have Jan’s expertise and to be operating in this kind of enterprise environment. If any of you come across a need for custom large scale solutions for running PW like this, definitely get in touch with Jan because he’s the real deal.

One of the interesting things about switching from a more traditional static instance web server to a load balanced multi-server setup is that it does change a few things about how you configure ProcessWire. It’s kind of like going through a proxy server in that there’s an intermediary (the load balancer) between the client and the servers, so this affects a few things in the .htaccess file (or Apache config) and how you configure sessions in PW. You also have to consider how to automatically keep the multiple instances up to date with the same files so that you don’t end up with multiple versions of them (Jan set us up with a clever *lsync* solution).

AWS makes the database side of all this redundancy really simple, as they handle it internally. This enables us to to access and treat it as one database while Amazon takes care of the redundancy and failover internally. All this while giving us pretty much infinite scalability. It’s all quite amazing and fun so I’m hoping to cover more tangible details on how to setup PW in this kind of environment in future blog posts as well. If you have specific questions, also feel free to post them here too. Hope that you all have a great weekend and enjoy reading the [ProcessWire Weekly](https://weekly.pw)!
