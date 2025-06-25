import React, { useState } from 'react';
import axios from 'axios';

function VerifyForm() {
  const [fileId, setFileId] = useState('');
  const [result, setResult] = useState(null);

  const handleVerify = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("file_id", fileId);

    try {
      const res = await axios.post("http://localhost:5000/verify", formData);
      setResult(res.data);
    } catch (err) {
      setResult({ error: err.message });
    }
  };

  return (
    <div>
      {/* <h2>Verify File Integrity</h2> */}
      <form onSubmit={handleVerify}>
        <input type="text" placeholder="file_id" value={fileId} onChange={e => setFileId(e.target.value)} />
        <button type="submit">Verify</button>
      </form>
      {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
    </div>
  );
}

export default VerifyForm;
