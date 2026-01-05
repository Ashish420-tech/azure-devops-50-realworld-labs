const http = require('http');

http.createServer((req, res) => {
  res.writeHead(200);
  res.end("Webhook pushed verified🚀");
}).listen(3000);

console.log("Server running on port 3000");
