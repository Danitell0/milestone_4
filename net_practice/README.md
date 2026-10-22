*This project has been created as part of the 42 curriculum by danmorei.*
 
# NetPractice
 
## Description
 
NetPractice is an introduction to computer networking. The project is made of
10 levels, each showing a small simulated network (hosts, routers, switches and
the internet) that does not work. The goal of every level is to fix the
configuration so that the listed hosts can talk to each other.
 
Solving the levels means working with:
 
- IPv4 addresses and how they are split into a network part and a host part
- Subnet masks, written in dotted form or CIDR form.
- Routing tables and default gateways on hosts and routers
- The difference between a switch (same network, no routing) and a router
  (connects different networks)
- Reserved and private address ranges
The networks are fictional and run entirely in the browser; nothing touches a
real network.
 
## Instructions
 
### Running the training interface
 
1. Download the archive attached to the project page on the intranet.
2. Extract it into any folder.
3. From that folder, run:
```sh
   ./run.sh
```
 
   This starts a local web server and opens the interface in your browser.
 
If `run.sh` does not work, start the server by hand and open the page yourself:
 
```sh
python3 -m http.server 49242
```
 
Then go to <http://localhost:49242> (any free port works).
 
## Resources
 
### Networking concepts studied
 
- **TCP/IP addressing** — IPv4 address structure, network and host portions
- **Subnet masks and CIDR** — calculating network address, broadcast address and
  usable host range
- **Default gateways** — where a host sends traffic for destinations outside its
  own network
- **Routing tables** — how hosts and routers choose the next hop
- **Routers and switches** — layer 3 vs. layer 2 devices
- **OSI model** — the layers involved, mainly layers 2 (data link) and 3 (network)
- **Private and reserved address ranges** — e.g. `10.0.0.0/8`,
  `172.16.0.0/12`, `192.168.0.0/16`, `127.0.0.0/8`

### References
 
- [RFC 791 — Internet Protocol](https://www.rfc-editor.org/rfc/rfc791)
- [RFC 1918 — Address Allocation for Private Internets](https://www.rfc-editor.org/rfc/rfc1918)
- [RFC 4632 — Classless Inter-domain Routing (CIDR)](https://www.rfc-editor.org/rfc/rfc4632)
- [Wikipedia — Subnetwork](https://en.wikipedia.org/wiki/Subnetwork)
- [Wikipedia — OSI model](https://en.wikipedia.org/wiki/OSI_model)
- [Wikipedia — Default gateway](https://en.wikipedia.org/wiki/Default_gateway)
 
### Use of AI
 
 Claude by Anthropic was used in this project for the following:

 - **README** - Helped drafting this README file, later edited by hand;
 - **Debugging** - Helped read logs;
