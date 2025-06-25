import React, { useState } from 'react';
import axios from 'axios';

function KeyGenerator() {
  const [user, setUser] = useState('');
  const [message, setMessage] = useState('');

  const handleGenerate = async () => {
    if (!user) return alert("Enter a user name");

    const formData = new FormData();
    formData.append("user", user);

    try {
      const res = await axios.post("http://localhost:5000/generate_keys", formData);
      setMessage(res.data.message);
    } catch (err) {
      setMessage("Key generation failed");
    }
  };

  return (
    <div className="key-gen">
      <h3>🔐 Generate RSA Keys</h3>
      <input type="text" placeholder="Username (e.g. alice)" value={user} onChange={e => setUser(e.target.value)} />
      <button onClick={handleGenerate}>Generate Keys</button>
      {message && <p>{message}</p>}
    </div>
  );
}

export default KeyGenerator;
