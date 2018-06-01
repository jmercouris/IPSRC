IP-Source
========================================================================
IP-Source is a program that allows you to keep track of your home
computer's IP via usage of a public (or private) Git repository
service.

Client
------------------------------------------------------------------------
The client will use its private key to decrypt the IP address uploaded
to the Git repository.

Server
------------------------------------------------------------------------
The server will periodically encrypt its IP and upload it to Git. The
server will use your computer's public key to encrypt its IP address.
