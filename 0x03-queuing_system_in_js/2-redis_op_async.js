import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient()
  .on('error', (error) => console.log(`Redis client not connected to the server: ${error}`))
  .on('connect', () => console.log(('Redis client connected to the server')));

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, print);
};

const displaySchoolValue = async (schoolName) => {
  const get = promisify(client.get).bind(client);
  try {
    const value = await get(schoolName);
    console.log(value);
  } catch (e) {
    console.log(e);
  }
};

(async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
