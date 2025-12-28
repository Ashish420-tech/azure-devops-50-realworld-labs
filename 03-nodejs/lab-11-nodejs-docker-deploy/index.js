const http = require("http");

const server = http.createServer((req, res) => {
  res.end("Lab-11: Docker application deployed successfully 🚀");
});

server.listen(3000, () => {
  console.log("Server running on port 3000");
});
