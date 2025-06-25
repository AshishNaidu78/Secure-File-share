import React, { useState } from 'react';
import axios from 'axios';

function DownloadForm() {
  const [form, setForm] = useState({
    cloud_file_url: '',
    sender: 'alice',   // ✅ who signed the file
    receiver: 'bob',   // ✅ who will decrypt the AES key
    enc_key: '',
    nonce: '',
    tag: '',
    signature: ''
  });

  const handleDownload = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    Object.entries(form).forEach(([key, val]) => formData.append(key, val));

    try {
      const res = await axios.post("http://localhost:5000/download", formData, {
        responseType: 'blob'
      });

      const blob = new Blob([res.data]);
      const url = window.URL.createObjectURL(blob);
      const link = document.createElement('a');

      // Dynamically name the downloaded file
      const rawName = form.cloud_file_url.split('/').pop() || "decrypted_file";
      const cleanName = rawName.replace('.enc', '').replace('.bin', '');
      link.href = url;
      link.setAttribute('download', cleanName);
      document.body.appendChild(link);
      link.click();
    } catch (err) {
      alert("Download failed: " + (err.response?.data?.error || err.message));
    }
  };

  return (
    <div className="download-form">
      <form onSubmit={handleDownload}>
        {Object.keys(form).map(key => (
          <input
            key={key}
            type="text"
            placeholder={key}
            value={form[key]}
            onChange={e => setForm({ ...form, [key]: e.target.value })}
            required
          />
        ))}
        <button type="submit">Download</button>
      </form>
    </div>
  );
}

export default DownloadForm;
