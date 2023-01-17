
#include <iostream> 
#include <string> 
#include <cstring> 
#include <sys/socket.h> 
#include <sys/types.h> 
#include <netinet/in.h> 
#include <arpa/inet.h> 
#include <unistd.h> 

int main () { 
  // Create a socket 
  int server_socket; 
  server_socket = socket(AF_INET, SOCK_STREAM, 0); 
  
  // Configure the server address 
  struct sockaddr_in server_address; 
  server_address.sin_family = AF_INET; 
  server_address.sin_port = htons(8080); 
  server_address.sin_addr.s_addr = INADDR_ANY; 
  
  // Bind the socket to our address 
  bind(server_socket, (struct sockaddr*) &server_address, sizeof(server_address)); 
  
  // Listen for connection 
  listen(server_socket, 5); 
  
  // Accept connection 
  int client_socket; 
  client_socket = accept(server_socket, NULL, NULL); 
  
  // Send response 
  char response[] = "Hello World!"; 
  send(client_socket, response, sizeof(response), 0); 

  
  
  // Close the socket 
  close(server_socket); 
  
  return 0; 
}