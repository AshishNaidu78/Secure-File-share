import React, { useState } from 'react';
import axios from 'axios';

function UploadForm() {
  const [file, setFile] = useState(null);
  const [sender, setSender] = useState("alice");
  const [receiver, setReceiver] = useState("bob");
  const [response, setResponse] = useState(null);

  const handleUpload = async (e) => {
    e.preventDefault();
    if (!file || !sender || !receiver) {
      setResponse({ error: "Please select file and provide sender & receiver" });
      return;
    }

    const formData = new FormData();
    formData.append("file", file);
    formData.append("sender", sender);
    formData.append("receiver", receiver);

    try {
      const res = await axios.post("http://localhost:5000/upload", formData);
      setResponse(res.data);
    } catch (err) {
      setResponse({ error: err.message });
    }
  };

  return (
    <div className="upload-form">
      <form onSubmit={handleUpload}>
        <input type="file" onChange={e => setFile(e.target.files[0])} required />
        <input
          type="text"
          placeholder="Sender (e.g. alice)"
          value={sender}
          onChange={e => setSender(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Receiver (e.g. bob)"
          value={receiver}
          onChange={e => setReceiver(e.target.value)}
          required
        />
        <button type="submit">Upload</button>
      </form>

      {response && (
        <div className="response">
          <h4>Upload Result:</h4>
          <pre>{JSON.stringify(response, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default UploadForm;
