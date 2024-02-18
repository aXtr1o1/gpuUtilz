import React, { useEffect, useState } from 'react';

const GPUInfoComponent = () => {
  const [gpuInfo, setGPUInfo] = useState(null);

  useEffect(() => {
    // Check for WebGL support
    const canvas = document.createElement('canvas');
    const gl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl');
    if (!gl) {
      console.error('WebGL is not supported in this browser.');
      return;
    }

    // Get GPU renderer and vendor
    const renderer = gl.getParameter(gl.RENDERER);
    const vendor = gl.getParameter(gl.VENDOR);

    setGPUInfo({ renderer, vendor });

  }, []);

  return (
    <div>
      {gpuInfo ? (
        <div>
          <h2>GPU Details</h2>
          <p>Renderer: {gpuInfo.renderer}</p>
          <p>Vendor: {gpuInfo.vendor}</p>
        </div>
      ) : (
        <p>Loading GPU information...</p>
      )}
    </div>
  );
};

export default GPUInfoComponent;
