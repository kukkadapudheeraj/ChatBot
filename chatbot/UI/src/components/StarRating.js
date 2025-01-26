import React from 'react';
import { FaStar } from 'react-icons/fa';

const StarRating = ({ currentRating, onRating }) => {
  const handleRating = (rate) => {
    onRating(rate);
  };

  return (
    <div>
      {[...Array(5)].map((star, i) => {
        const ratingValue = i + 1;
        return (
          <label key={i}>
            <input
              type="radio"
              name="rating"
              value={ratingValue}
              onClick={() => handleRating(ratingValue)}
              style={{ display: 'none' }}
            />
            <FaStar
              className="star"
              size={20}
              color={ratingValue <= currentRating ? "#ffc107" : "#e4e5e9"}
              onMouseEnter={() => {}}
              onMouseLeave={() => {}}
            />
          </label>
        );
      })}
    </div>
  );
};

export default StarRating;
