import React, { useState } from 'react';
import axios from 'axios';

function KeyMetadataFetcher() {
  const [form, setForm] = useState({ file_id: '', receiver: '' });
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');

  const handleFetch = async (e) => {
    e.preventDefault();
    setError('');
    setResult(null);

    const formData = new FormData();
    formData.append('file_id', form.file_id);
    formData.append('receiver', form.receiver);

    try {
      const res = await axios.post('http://localhost:5000/get_key_metadata', formData);
      setResult(res.data.metadata);
    } catch (err) {
      setError(err.response?.data?.error || 'Request failed');
    }
  };

  return (
    <div className="section-card">
      <h2>📂 Retrieve File Key Metadata</h2>
      <form onSubmit={handleFetch}>
        <input
          type="text"
          placeholder="file_id (e.g. document.pdf)"
          value={form.file_id}
          onChange={(e) => setForm({ ...form, file_id: e.target.value })}
          required
        />
        <input
          type="text"
          placeholder="receiver (e.g. bob)"
          value={form.receiver}
          onChange={(e) => setForm({ ...form, receiver: e.target.value })}
          required
        />
        <button type="submit">Get Metadata</button>
      </form>

      {error && <p style={{ color: 'red' }}>❌ {error}</p>}

      {result && (
        <div style={{ marginTop: '1rem', textAlign: 'left' }}>
          <h4>🔑 Metadata:</h4>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default KeyMetadataFetcher;
