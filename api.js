const express = require('express');
const app = express();
const PORT = 3000;

app.use(express.json());

// lista de tarefas simples banco de dados
const tarefas = [
  { id: 1, descricao: 'Fazer o café da manhã' },
  { id: 2, descricao: 'Estudar API' }
];

// Ve todas as tarefas
app.get('/tarefas', (req, res) => {
  res.json(tarefas);
});

// Adiciona uma nova tarefa
app.post('/tarefas', (req, res) => {
  const novaTarefa = req.body;
  tarefas.push(novaTarefa);
  res.status(201).json(novaTarefa);
});

// Inicia o servidor
app.listen(PORT, () => {
  console.log(`API rodando em http://localhost:${PORT}`);
});
