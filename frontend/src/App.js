import './App.css';
import UploadForm from './components/UploadForm';
import DownloadForm from './components/DownloadForm';
import VerifyForm from './components/VerifyForm';
import KeyGenerator from './components/KeyGenerator';
import KeyMetadataFetcher from './components/KeyMetadataFetcher';
// import KeyDocDownload from './components/KeyDocDownload'; //

function App() {
  return (
    <div className="container">
      <header>
        <h1>🔐 Blockchain-Based Secure File Sharing</h1>
        <p className="subtitle">Encrypt • Sign • Store • Verify</p>
      </header>

      <div className="section-card">
        <h2>🧾 Generate RSA Keys</h2>
        <p>Generate sender/receiver keys before uploading or downloading files.</p>
        <KeyGenerator />
      </div>

      <div className="section-card">
        <h2>📤 Upload Secure File</h2>
        <UploadForm />
      </div>

      <div className="section-card">
        <h2>📥Download & 🔐 Decrypt Secure File</h2>
        <DownloadForm />
      </div>

      <div className="section-card">
        <h2>✅ Verify File Integrity</h2>
        <VerifyForm />
      </div>

      <div className="section-card">
        <h2>🔑 Fetch Key Metadata</h2>
        <p>Query MongoDB to retrieve encrypted file key metadata (stored at upload time).</p>
        <KeyMetadataFetcher />
      </div>

      {/* <div className="section-card">
        <h2>📄 Decrypt Key Document from Cloud</h2>
        <p>Provide the KeyDoc URL and receiver to view decrypted AES metadata.</p>
        <KeyDocDownload />
      </div> */}

      <footer>
        <p>🔒 Built with AES, RSA, and Blockchain</p>
      </footer>
    </div>
  );
}

export default App;
