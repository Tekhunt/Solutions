import React from 'react'
import {  NewWrapper } from './NewsStyled';

function News() {
    return (
        < NewWrapper>
            <div className="container-new">
                <p>LATEST NEWS</p>
                <div className="latest-news">
                    
                        <div className="news-box">
                            <div className="image-new">
                                <img src="img/feature2.fa7b3d70.png" alt="item_object" />
                            </div>
                            <div className="news-text">
                                <p className="news-date">01 Jan, 2015</p>
                                <h4>Typesetting <br /> industry</h4>
                                <p>Lorem ipsum dolor sit amet consectetur, 
                                    adipisicing elit. 
                                </p>
                            </div>
                        </div>
                        <div className="news-box">
                            <div className="image-new">
                                <img src="img/feature2.fa7b3d70.png" alt="item_object" />
                            </div>
                            <div className="news-text">
                                <p className="news-date">01 Jan, 2015</p>
                                <h4>Typesetting <br /> industry</h4>
                                <p>Lorem ipsum dolor sit amet consectetur, 
                                    adipisicing elit. 
                                </p>
                            </div>
                        </div>
                        <div className="news-box">
                            <div className="image-new">
                                <img src="img/feature2.fa7b3d70.png" alt="item_object" />
                            </div>
                            <div className="news-text">
                                <p className="news-date">01 Jan, 2015</p>
                                <h4>Typesetting <br /> industry</h4>
                                <p>Lorem ipsum dolor sit amet consectetur, 
                                    adipisicing elit. 
                                </p>
                            </div>
                        </div>
                    
                </div>
            </div>
        </NewWrapper>
    )
}

export default News
