
import React from 'react'
import {DeliveryWrapper } from './DeliveryStyled';

function Delivery() {
    return (
        <DeliveryWrapper>
            <div className="container">
                <div className="delivery">
                    <div>
                        <div className="delivery-icon">
                            <img src="img/download (1).png" alt="free shipping_icon" />
                        </div>
                        <h1>FREE SHIPPING</h1>
                        <p>
                            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Vitae voluptas eaque quis minus,
                            ullam odit quod vero repellendus at quo, nisi officiis recusandae quasi odio. Laborum aperiam
                            a eos blanditiis voluptatibus incidunt sequi temporibus sunt sint nisi odio architecto 
                        
                        </p>
                    </div>
                    <div>
                        <div className="delivery-icon">
                            <img src="img/download (2).png" alt="100% shipping_icon" />
                        </div>
                        <h1>100% REFUND</h1>
                        <p>
                            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Vitae voluptas eaque quis minus,
                            ullam odit quod vero repellendus at quo, nisi officiis recusandae quasi odio. Laborum aperiam
                            a eos blanditiis voluptatibus incidunt sequi temporibus sunt sint nisi odio architecto 
                        
                        </p>
                    </div>
                    <div>
                        <div className="delivery-icon">
                            <img src="img/download.png" alt="SUPPORT 24/7 icon" />
                        </div>
                        <h1>SUPPORT 24/7</h1>
                        <p>
                            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Vitae voluptas eaque quis minus,
                            ullam odit quod vero repellendus at quo, nisi officiis recusandae quasi odio. Laborum aperiam
                            a eos blanditiis voluptatibus incidunt sequi temporibus sunt sint nisi odio architecto 
                        
                        </p>
                    </div>
                </div>
            </div>
        </DeliveryWrapper>
    )
}

export default Delivery
