import { createClient } from 'redis';

createClient()
  .on('error', (error) => console.log(`Redis client not connected to the server: ${error}`))
  .on('connect', () => console.log(('Redis client connected to the server')));
