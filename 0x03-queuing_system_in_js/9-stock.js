import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const app = express();
const client = createClient();

const listProducts = [
  {"itemId":1,"itemName":"Suitcase 250","price":50,"initialAvailableQuantity":4},
  {"itemId":2,"itemName":"Suitcase 450","price":100,"initialAvailableQuantity":10},
  {"itemId":3,"itemName":"Suitcase 650","price":350,"initialAvailableQuantity":2},
  {"itemId":4,"itemName":"Suitcase 1050","price":550,"initialAvailableQuantity":5}
]

client.on('error', (err) => {
  console.log(err);
});

client.on('connect', () => {
  console.log('Client connected');
});

function getItemById(id) {
  return listProducts.find((product) => (
    product.itemId === id
  ));
}

function reserveStockById(itemId, stock) {
  client.HSET('item', itemId, stock);
}

async function getCurrentReservedStockById(itemId) {
  return await promisify(client.HGET).bind(client)('item', itemId);
}

app.get('/list_products', (req, res) => {
  res.json(listProducts).end();
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = Number.parseInt(req.params.itemId);
  const product = getItemById(itemId);
  const inventory = await getCurrentReservedStockById(itemId);

  if (product) {
    product.currentQuantity = inventory;
    res.json(product).end();
  } else {
    res.json({status: 'Product not found'}).end();
  }
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = Number.parseInt(req.params.itemId);
  const product = getItemById(itemId);

  if (product) {
    if (product.initialAvailableQuantity > 0) {
      reserveStockById(itemId, product.initialAvailableQuantity);
      product.initialAvailableQuantity -= 1;
      res.json({status: 'Reservation confirmed', itemId: itemId}).end();
    } else {
      res.json({status: 'Not enough stock available', itemId: itemId}).end();
    }
  } else {
    res.json({status: 'Product not found'}).end();
  }
});

app.listen(1245, () => {
  console.log('...');
});
