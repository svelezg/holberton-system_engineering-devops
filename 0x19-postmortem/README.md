-- Postmortem example --
# memonto.co Postmortem (incident #001)
![alt text](https://github.com/svelezg/holberton-system_engineering-devops/blob/master/0x19-postmortem/solve.jpg)

## Date

2020-02-20

## Authors

* Santiago Vélez García

## Status

Complete

## Summary

memonto.co website down for 59 minutes.

The event started at 17:51 UTC and ended at 18:50 UTC affecting 100% of the service.

## Impact

Estimated 2300 queries lost, no revenue impact.

## Root Causes

The load balancer went down due to exceptionally high load combined with power failure of the load balancer server.


## Trigger

A sudden traffic increase when a celebrity promoted the service trough his tweeter account.

## Resolution

The first measure was to suppress the load balancer from the web infrastructure architecture, setting up a pass-through configuration, 
where the requests were directly served by the web-servers. Once the service was again online, 
a new load balancer was set up and added to the infrastructure.

## Detection

The datadog monitoring system installed on the servers sent an automated email alert.


## Timeline

2020-02-20 (*all times UTC*)

| Time  | Description |
| ----- | ----------- |
| 17:40 | J Balvin Tweeter posts about memonto.co the website suddenly went viral |
| 17:47 | Traffic increased by 50x after post |
| 17:51 | **OUTAGE BEGINS** -- the temperature in the load balancer increases so fast and some user cannot access to the website|
| 17:55 | most of the users receive pager storm, `ManyHttp500s`  |
| 17:57 | All traffic failing|
| 18:01 | **INCIDENT BEGINS** the monitoring system sends email alert |
| 18:02 | DevOps Engineer Cesar receives the notification, initiates the analysis and inform the VevOps team|
| 18:03 | Santiago, the backend dev is notified |
| 18:04 | Ping test from different locations shows that the server is isolated |
| 18:06 | Cesar contacts the datacenter service provider. They inform that there is no issue in the datacenter  |
| 18:07 | Juan A insists that we cannot connect with the load balancer |
| 18:10 | The data center informs that apparently the server where the load balancer is located lost power supply |
| 18:12 | Cesar modifies the configuration to by-pass the load balancer  |
| 18:18 | Cesar runs a puppet manifest that contains the new configuration |
| 18:25 | The new configuration is now up |
| 18:30 | the service is partially running. Still some users cannot connect with the server, but ~70% of the traffic is ok|
| 18:39 | A new server (hardware) is set aside and installed in the datacenter|
| 18:45 | The new server is set up as a load balacer|
| 18:50 | **OUTAGE ENDS**, all traffic is ok, the new load balancer is online |
| 19:20 | **INCIDENT ENDS**, reached exit criterion of 30 minutes nominal performance |

## Corrective and preventative measures
Lessons Learned

 	Single points of failure are the biggest risk

* Monitoring system promptly  alerted of a high rate (reaching ~100%) of HTTP 500s
* Quick temporary configuration set up

Action Items

| Action Item | Type | Owner | Bug |
| ----------- | ---- | ----- | --- |
| Handbook update  with instructions for load balancer failure response | mitigate | Juan Alberto | n/a **DONE** |
| Puppet manifests with different configurations | prevent | Santiago | Bug 5234823 **TODO** |
| Schedule infrastructure stress tests | process | Pablo | n/a **TODO** |
| Single point of failures assessment  | prevent | Fredy | **DONE** |
| Load balancer cluster set up | prevent | Cesar | **DONE** |

## Supporting Information

* Monitoring dashboard
