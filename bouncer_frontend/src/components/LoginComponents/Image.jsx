import React from 'react'
import './style.css'

function Image({url}) {
    return (
            <div className="left-container"> 
                 <img className="image-url" src={url}  alt="laptop"/> 
            </div>
      
    )
}

export default Image;
