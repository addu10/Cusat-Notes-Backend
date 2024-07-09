import React, { useEffect, useState } from 'react';
/*
function Index() {
  const [message, setMessage] = useState("Loading.....");
  const [fileName, setFileName] = useState("");
  const [download, setDownload] = useState(false);

  useEffect(() => {
    fetch('http://localhost:8080/api/home')
     .then((response) => response.json())
     .then((data) => {
        setMessage(data.message);
      });
  }, []);

  useEffect(() => {
    if (download) {
      fetch('http://localhost:8080/api/download', {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name: fileName
        }),
      })
       .then((response) => response.json())
       .then((data) => {
          const result = data.result;
          console.log(result);
        })
       .finally(() => setDownload(false));
    }
  }, [download]);

  const handleDownload = () => {
    setDownload(true);
  };

  return (
    <div className="flex items-center justify-center h-screen">
      <div className="bg-white p-8 rounded-lg shadow-md">
        <div className="text-center mb-6">
          <h1 className="text-2xl text-gray-500 font-bold mb-2">Download File</h1>
          <p className="text-gray-500">Enter the name of the file you want to download</p>
        </div>
        <input
  type="text"
  value={fileName}
  onChange={(e) => setFileName(e.target.value)}
  placeholder="Enter file name"
  className="block w-full p-2 mb-4 rounded-md border border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-500 text-black"
/>
        <button
          onClick={handleDownload}
          className="bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600"
        >
          Download
        </button>
      </div>
    </div>
  );
}

export default Index;*/