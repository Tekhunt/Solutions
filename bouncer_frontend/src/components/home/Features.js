import React from 'react'
import { FeatureWrapper } from './FeatureStyled';

function Features() {
    return (
        <FeatureWrapper>
            <div className="container-new">
                <h1>FEATURED PRODUCTS</h1>
                <div className="featured-products">
                    <div className="featured-sub">
                        <div>
                            <img src="img/feature1.ce5ad103.png" alt="feature_pic" />
                        </div>
                        <div>
                            <p>Beats Solo 2 On Ear
                                Headphones-Black
                            </p>
                            <div className="star-rating">
                                <i className="fas fa-star"></i>
                                <i className="fas fa-star"></i>
                                <i className="fas fa-star"></i>
                                <i className="fas fa-star"></i>
                                <i className="fas fa-star"></i>
                                <i className="fas fa-star"></i>
                            </div>
                            <p><span className="actual-price">$499</span> <span class="price-tag">$599</span></p>
                        </div>
                    </div>
                    <div className="featured-sub">
                        <div>
                            <img src="img/feature2.fa7b3d70.png" alt="feature_pic" />
                        </div>
                        <div>
                            <p>Beats Solo 2 On Ear 
                                Headphones-Black
                            </p>
                            <div className="star-rating">
                                <i className="fas fa-star"></i>
                                <i className="fas fa-star"></i>
                                <i className="fas fa-star"></i>
                                <i className="fas fa-star"></i>
                                <i className="fas fa-star"></i>
                                <i className="fas fa-star"></i>
                            </div>
                            <p><span className="actual-price">$499</span> <span class="price-tag">$599</span></p>
                        </div>
                    </div>
                    <div className="featured-sub">
                        <div>
                            <img src="img/item3_sjz14g.png" alt="featured_image" />
                        </div>
                        <div>
                            <p>Beats Solo 2 On Ear
                                Headphones-Black
                            </p>
                            <div className="star-rating">
                                <i className="fas fa-star"></i>
                                <i className="fas fa-star"></i>
                                <i className="fas fa-star"></i>
                                <i className="fas fa-star"></i>
                                <i className="fas fa-star"></i>
                                <i className="fas fa-star"></i>
                            </div>
                            <p><span className="actual-price">$499</span> <span class="price-tag">$599</span></p>
                        </div>
                    </div>
                </div>
            </div>
        </FeatureWrapper>
    )
}

export default Features
