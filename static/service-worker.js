self.addEventListener("install", (event) => {
    // Immediately take control
    self.skipWaiting();
  });
  
  self.addEventListener("activate", (event) => {
    self.clients.claim();
  });
  
  // No fetch handler — we don't cache anything!
  