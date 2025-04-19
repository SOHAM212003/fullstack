import React from 'react';

function App() {
  const someObject = { name: "Farm", type: "Sustainable" };

  // Fix: Render object properties or stringify the object
  return (
    <div>
      <h1>Welcome to Sustainable Farming</h1>
      <p>{someObject.name}</p> {/* Correct */}
      {/* <p>{someObject}</p> This would cause the error */}
    </div>
  );
}

export default App;