from pwn import *
#imports duh

HOST = input("IP?")
PORT = input here
#input stuff here

context.arch = 'amd64'
context.os = 'linux'
#dont need to change this


r = remote(HOST, PORT)
r.sendline("ls")
r.interactive
#remotes into the host and sends ls if it was sucessful 
