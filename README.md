# Replication of TCP/IP model
#### - Project by Geetesh Gupta & Hiren Chalodiya

The project involves replicating the functionality of data-link and physical layer of tcp/ip model. The implementation has been made on the basis of client-server architecture. The server and the client interact with each other by transferring messages through socket programming. Messages are encoded at the client side when sending them to the server and are decoded at the server side when server receives the message. 

All the functionalities/features are developed in modular fashion so as to allow easy and fast modification/updation without producing any side effects to the working of the application. As a result, different encoding schemes can used for encoding/decoding purposes by just adding the new scheme in a separate file and updating the corresponding environment variable.

Error detection has also been implemented to detect errors occuring when message is transferred from client to server. This module is also modular in nature so that any new eror mechanism can added easily.

Individual detailed implementations of each layer are given below:
## Data-link Layer
Data link layer is responsible for moving frames from one hop (node) to the next i.e Hop-to-Hop delivery. The data link layer ensures that all packets of information are passed on free of errors. The data link layer is the second layer in the OSI Model. The three main functions of the data link layer are to deal with transmission errors, regulate the flow of data, and provide a well-defined interface to the network layer.

Basically, this layer involves dividing the message into packets and then converting them into frames by adding redundant bits for error control, flow control, addressing and source/destination identification. Following are the functionalities implemented in this layer:
-   <details>
    <summary>Framing</summary>
    <ul>
    <li> Frames are the units of digital transmission particularly in computer networks and telecommunications. It provides a way for a sender to transmit a set of bits that are meaningful to the receiver. 
    </li>
    <li> The advantage of using frames is that data is broken up into recoverable chunks that can easily be checked for corruption.
    
    </li>
    <li> Frames can of two types - Fixed-size or Variable-size
    </li>
    <li> In this project, Variable-size framing is used. This allows decreasing the number of frames by increasing the frame size, hence increasing the bandwidth utilisation.
    </li>
    </ul>
    </details>
-   <details>
    <summary>Bit Stuffing</summary>
    <ul>
    <li> Bit stuffing is the mechanism of inserting one or more non-information bits into a message to be transmitted, to break up the message sequence, for synchronization purpose. 
    </li>
    <li> Since we have used variable-length framing, the size of each frame to be transmitted may be different. So, a pattern of bits is used as a delimiter to mark the end of one frame and the beginning of the next frame. However, if the pattern occurs in the message, then mechanisms needs to be incorporated so that this situation is avoided.
    
    </li>
    <li> The delimiting flag sequence generally contains six or more consecutive 1s. In order to differentiate the message from the flag in case of the same sequence, a single bit is stuffed in the message. Whenever a 0 bit is followed by five consecutive 1 bits in the message, an extra 0 bit is stuffed at the end of the five 1s.
    </li>
    <li> When the receiver receives the message, it removes the stuffed 0s after each sequence of five 1s. The un-stuffed message is then sent to the upper layers.
    </li>
    </ul>
    </details> 
-   <details>
    <summary>Cyclic Redundancy Check</summary>
    <ul>
    <li> In this project, we have implemented CRC technique for error detection.
    </li>
    <li> CRC or Cyclic Redundancy Check is a method of detecting accidental changes/errors in communication channel. 
    </li>
    <li> A fixed number of check bits, called a checksum, are appended to the message that needs to be transmitted. Receivers receive the data and inspect the check bits for any errors.
    </li>
    <li> Mathematically, data receivers check on the check value attached by finding the remainder of the polynomial division of the contents transmitted. If it seems that an error has occurred, a negative acknowledgement is transmitted asking for data retransmission.
    </li>
    </ul>
    </details>  

## Physical Layer
Physical layer is the lowest layer of the OSI reference model. It is responsible for sending bits from one computer to another. This layer is not concerned with the meaning of the bits and deals with the setup of physical connection to the network and with transmission and reception of signals.
-   <details>
    <summary>Socket Programming</summary>
    <ul>
    <li>In this project, we have used socket programming architecture so as to mimic the physical layer mechanism. 
    </li>
    <li> Socket programming is a way of connecting two nodes on a network to communicate with each other. 
    </li>
    <li>One socket (node) listens on a particular port at an IP, while other socket reaches out to the other to form a connection. Server forms the listener socket while client reaches out to the server.
    </li>
    </ul>
    </details>
-   <details>
    <summary>Signal Encoding Scheme</summary>
    <ul>
    <li> Encoding is the process of using various patterns of voltage or current levels to represent 1s and 0s of the digital signals on the transmission link.  
    </li>
    <li> The common types of line encoding are Unipolar, Polar, Bipolar, and Manchester.
    </li>
    <li> We have implemented Manchester, NRZ-L and NRZ-L encoding schemes in the project.
    </li>
    <li> By default, Manchester is selected. Any of the above encoding schemes can be used by updating the corresponding environment variable.
    </li>
    </ul>
    </details>

## Setup
To setup the project, run the following command
```
cp .env.example .env
```
To run the server, type the following command
```
python3 manage.py server
```
To run the client, type the following command
```
python3 manage.py client
```
