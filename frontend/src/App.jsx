import { useState } from "react";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [summary, setSummary] = useState(null);
  const [error, setError] = useState(null);
  const [status, setStatus] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setSummary(null);
    setError(null);
    setStatus(null);
  };

  const handleImport = async () => {
    if (!file) {
      setError("Please select a file first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);
      setError(null);
      setSummary(null);
      setStatus({ type: "loading", message: "Import in progress..." });

      const response = await fetch(
        "http://127.0.0.1:8000/import/products",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      if (data.error) {
        setError(data.error);
        setStatus({ type: "error", message: "Import failed." });
      } else {
        setSummary(data.summary);
        setStatus({ type: "success", message: "Import completed." });
      }
    } catch (err) {
      setError("Something went wrong while importing.");
      setStatus({ type: "error", message: "Import failed." });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <h1 className="app-title">Matrixify-Lite</h1>
      <p className="app-subtitle">
        Standalone Shopify Product Import Engine
      </p>

      <div className="card">
        <input
          type="file"
          accept=".csv,.xlsx,.xls"
          onChange={handleFileChange}
        />

        <span className="file-name">
          {file ? file.name : "No file selected"}
        </span>

        <button onClick={handleImport} disabled={loading}>
          {loading ? "Importing..." : "Start Import"}
        </button>
      </div>

      {status && (
        <div className={`status-box ${status.type}`} role="status" aria-live="polite">
          <h3>Status</h3>
          <p>{status.message}</p>
        </div>
      )}

      {error && (
        <div className="summary-box" style={{ borderLeft: "4px solid red" }}>
          <h3>Error</h3>
          <p>{error}</p>
        </div>
      )}

      {summary && (
        <div className="summary-box">
          <h3>Import Summary</h3>
          <p>✅ Created: {summary.created}</p>
          <p>🔄 Updated: {summary.updated}</p>
        </div>
      )}
    </div>
  );
}

export default App;
