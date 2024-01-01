# VPN - Virtual Private Network


## IPSEC

- Works on layer 3

1. Integration with Network Layer: IPsec operates at the network layer of the OSI model, providing security for IP packets. It can be used to secure communication at the IP layer without the need for additional software at higher layers.
2. Widely Supported: IPsec is a standard that is widely supported by many operating systems and network devices. It is often built into the operating system kernel, which can enhance its performance.
3. Strong Encryption: IPsec supports strong encryption algorithms, providing a high level of security when properly configured.
4. Site-to-Site and Remote Access: IPsec is commonly used for both site-to-site VPNs and remote access VPNs.

### ESP-Protected packets with sequence numbers

![](images/VPN/IMG_0299.jpeg)


- As TLS is based on TCP records cannot arrive in the wrong order unless theres an attack or a serious error has happened -> clsoe with error

## Open VPN

- Runs on top of UDP or TCP
- Usually uses UDP, as TCP over TCP results in poor performance
- Software on the VPN endpoints run in the user space
- Protect IP Packets between the VPN endpoints
-  Uses TLS handshake protocol for mutual authentication and key exchange


1. SSL/TLS-Based: OpenVPN is based on the SSL/TLS protocol and operates at the application layer. It encapsulates VPN traffic in a secure tunnel over UDP or TCP.
2. Flexibility: OpenVPN is known for its flexibility and can be easily configured to work over different ports and protocols. This can be advantageous in situations where certain types of traffic are restricted.
3. Portability: OpenVPN is available on various platforms, including Windows, Linux, macOS, and mobile platforms, making it a versatile solution.
4. Adaptability: OpenVPN is often considered more adaptable to different network conditions, such as traversing NAT (Network Address Translation) without the need for additional configurations.

### Protocol Stack

![](images/VPN/IMG_0301.jpeg)

### Packet format

![](images/VPN/IMG_0302.jpeg)

## Wireguard

- Works on layer 3
- Very little configurability, deliberately no cipher and protocol agility
    - much smaller attack surface
- uses modern crypto primitives (ChaCha20, Ruve25519)
- Has a 1-RTT handshake
- Has perfect forward secrcy (PFS)
- Has DoS mitigation techniques

### Message Flow

![](images/VPN/IMG_0303.jpeg)