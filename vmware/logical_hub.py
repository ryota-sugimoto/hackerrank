#!/usr/bin/env python

def wire_port2port(d):
  for host in d.keys():
    hubs = d[host]
    for i in range(len(hubs)):
      for j in range(i+1,len(hubs)):
        if hubs[i] == hubs[j]:
          print "PORT_TO_PORT %s %i %i" % (host,i,j)
          print "PORT_TO_PORT %s %i %i" % (host,j,i)

def make_hub_map(d):
  hub_map = {}
  for host in d.keys():
    hubs = d[host]
    for hub in hubs:
      if hub_map.has_key(hub):
        hub_map[hub].add(host)
      else:
        hub_map[hub] = set([host])
  return hub_map

def wire_port2tunnel(d,hub_map):
  for host in d.keys():
    hubs = d[host]
    for i,hub in enumerate(hubs):
      for dst_host in hub_map[hub]:
        if dst_host != host:
          print "PORT_TO_TUNNEL %s %i %s %s" % (host,i,dst_host,hub)

def wire_tunnel2port(d,hub_map):
  if len(d.keys()) > 1:
    for host in d.keys():
      hubs = d[host]
      for i,hub in enumerate(hubs):
        if len(hub_map[hub]) > 1:
          print "TUNNEL_TO_PORT %s %s %i" % (host,hub,i)

import sys
hosts = {}
for s in sys.stdin:
  l = s.strip().split()
  host = l[0]
  hosts[host] = []
  for hub in l[1:]:
    hosts[host].append(hub)
  
hub_map = make_hub_map(hosts)

wire_port2port(hosts)
wire_port2tunnel(hosts,hub_map)
wire_tunnel2port(hosts,hub_map)
