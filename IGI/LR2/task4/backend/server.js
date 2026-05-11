const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

mongoose.connect(process.env.MONGO_URI)
  .then(() => console.log("MongoDB connected"));

const Item = mongoose.model("Item", { name: String });

app.get("/items", async (req, res) => {
  res.json(await Item.find());
});

app.post("/items", async (req, res) => {
  const item = new Item({ name: req.body.name });
  await item.save();
  res.json(item);
});

app.listen(5000, () => console.log("Server running"));