const http = require('http');

http.createServer((req, res) => {
  res.writeHead(200);
  res.end("Github webhook triggered Jenkins CI/CD🚀");
}).listen(3000);

console.log("Server running on port 3000");
