import React from 'react';
import './Legend.css';

const Legend = () => {
  return (
    <div className="legend">
      <span>⭐ &lt; 3: Not Relevant</span>
      <span>⭐ &ge; 3: Relevant</span>
    </div>
  );
};

export default Legend;
