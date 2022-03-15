import React from 'react'
import { Link } from 'react-router-dom';
import { DisplayWrapper } from './DisplayProductStyled';

function DisplayProduct() {
    return (
        <DisplayWrapper class="backdrop-image"> 
            <div className="iphone-plus">
                <div>
                    <h1>iPhone 6 Plus</h1>
                    <p>Performance and design. Taken right to the edge</p>
                    <Link href="/">SHOP NOW</Link>
                    <p class="lines"></p>
                </div>
                <div className="iphone-display">
                    <img src="img/pic.35f166b7.png" alt="iphone-display" />
                </div>
            </div>
        </DisplayWrapper>
    )
}

export default DisplayProduct
