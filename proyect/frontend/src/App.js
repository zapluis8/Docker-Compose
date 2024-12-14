import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [characters, setCharacters] = useState([]);
  const [name, setName] = useState('');
  const [game, setGame] = useState('');

  // Fetch los personajes desde el backend
  const fetchCharacters = async () => {
    const response = await axios.get('http://localhost:8000/caracteres/');
    setCharacters(response.data);
  };

  // Crear un nuevo personaje
  const createCharacter = async () => {
    await axios.post('http://localhost:8000/caracteres/', { name, game });
    setName('');
    setGame('');
    fetchCharacters();
  };

  // Eliminar un personaje
  const deleteCharacter = async (id) => {
    await axios.delete(`http://localhost:8000/caracteres/${id}`);
    fetchCharacters();
  };

  // Llamar a fetchCharacters cuando el componente se monta
  useEffect(() => {
    fetchCharacters();
  }, []);

  return (
    <div>
      <h1>Video Game Characters</h1>
      <div>
        <input
          type="texto"
          placeholder="Nombre"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <input
          type="texto"
          placeholder="Juego"
          value={game}
          onChange={(e) => setGame(e.target.value)}
        />
        <button onClick={createCharacter}>Add Character</button>
      </div>
      <ul>
        {characters.map((character) => (
          <li key={character.id}>
            {character.name} from {character.game}
            <button onClick={() => deleteCharacter(character.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
