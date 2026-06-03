const CACHE = 'maze-v2';
const ASSETS = [
  '/',
  'cover.html', 'index.html', 'directions.html', 'prologue.html', 'contest.html',
  'css/maze.css', 'css/bootstrap.min.css',
  'js/bootstrap.bundle.min.js',
  'manifest.json',
];

// Cache room pages + images on first access
self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)));
});

// Serve from cache, fall back to network
self.addEventListener('fetch', e => {
  e.respondWith(
    caches.match(e.request).then(r => r || fetch(e.request).then(res => {
      if (res.ok) {
        const clone = res.clone();
        caches.open(CACHE).then(c => c.put(e.request, clone));
      }
      return res;
    }))
  );
});
