const http = require('http');

http.createServer((req, res) => {
  res.writeHead(200);
  res.end("Lab 23 Jenkins CI/CD is LIVE 🚀");
}).listen(3000);

console.log("Server running on port 3000");
